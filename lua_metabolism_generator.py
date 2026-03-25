"""
Generador y parser de configuraciones de metabolismo (usables) para RedM
Lee/escribe el archivo usables_lhr.cfg.lua con la tabla Usables.itemsLHR
"""
import re

# ============================================================================
# ALMACENAMIENTO (reutiliza el mismo patrón que lua_crafteo_generator)
# ============================================================================
_storage_mode = 'local'
_drive_module = None
_METABOLISM_FILENAME = 'usables_lhr.cfg.lua'


def set_storage_mode(mode: str, drive_module=None):
    global _storage_mode, _drive_module
    _storage_mode = mode
    _drive_module = drive_module


# ============================================================================
# FUNCIONES PARA EXTRAER ANIMACIONES Y PROPS DINÁMICAMENTE DEL ARCHIVO
# ============================================================================

def extract_unique_animations(items: list[dict]) -> list[str]:
    """Extrae las animaciones únicas usadas en los items parseados."""
    anims = set()
    for item in items:
        anim = item.get('effects_animationName', '')
        if anim:
            anims.add(anim)
    return sorted(anims)


def extract_unique_props(items: list[dict]) -> list[str]:
    """Extrae los props únicos usados en los items parseados."""
    props = set()
    for item in items:
        prop = item.get('effects_prop', '')
        if prop:
            props.add(prop)
    return sorted(props)


# ============================================================================
# LECTURA / ESCRITURA DEL ARCHIVO DE METABOLISMOS
# ============================================================================

def read_metabolism_file() -> str | None:
    """Lee el archivo usables_lhr.cfg.lua desde Drive."""
    if _storage_mode == 'drive' and _drive_module:
        try:
            return _drive_module.read_file(_METABOLISM_FILENAME)
        except Exception as e:
            print(f"Error leyendo {_METABOLISM_FILENAME} desde Drive: {e}")
            return None
    return None


def save_metabolism_file(content: str) -> bool:
    """Guarda el archivo usables_lhr.cfg.lua en Drive."""
    if _storage_mode == 'drive' and _drive_module:
        try:
            result = _drive_module.write_file(_METABOLISM_FILENAME, content)
            return bool(result)
        except Exception as e:
            print(f"Error guardando {_METABOLISM_FILENAME} en Drive: {e}")
            return False
    return False


# ============================================================================
# PARSER — Extrae items de Usables.itemsLHR
# ============================================================================

def _find_balanced_brace(text: str, start: int) -> int:
    """Encuentra la posición del cierre de llave balanceado desde start (que apunta a '{')."""
    depth = 0
    i = start
    in_string = False
    in_comment = False
    in_block_comment = False
    while i < len(text):
        c = text[i]
        # Block comments --[[ ... ]]
        if in_block_comment:
            if c == ']' and i + 1 < len(text) and text[i + 1] == ']':
                in_block_comment = False
                i += 2
                continue
            i += 1
            continue
        # Line comments
        if in_comment:
            if c == '\n':
                in_comment = False
            i += 1
            continue
        # Strings
        if in_string:
            if c == '\\':
                i += 2
                continue
            if c == in_string:
                in_string = False
            i += 1
            continue
        # Check for comments
        if c == '-' and i + 1 < len(text) and text[i + 1] == '-':
            if i + 3 < len(text) and text[i + 2] == '[' and text[i + 3] == '[':
                in_block_comment = True
                i += 4
                continue
            in_comment = True
            i += 2
            continue
        if c in ('"', "'"):
            in_string = c
            i += 1
            continue
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                return i
        i += 1
    return -1


def parse_metabolism_items(content: str) -> list[dict]:
    """
    Parsea el contenido de usables_lhr.cfg.lua y extrae todos los items
    (activos y comentados) con sus propiedades.
    Retorna lista de dicts con la info de cada item.
    """
    if not content:
        return []

    items = []
    # Buscar items activos: ["item_id"] = { ... }
    pattern = re.compile(r'^\s*\["([^"]+)"\]\s*=\s*\{', re.MULTILINE)
    for m in pattern.finditer(content):
        item_id = m.group(1)
        brace_start = m.end() - 1  # posición del '{'
        brace_end = _find_balanced_brace(content, brace_start)
        if brace_end == -1:
            continue
        block = content[brace_start:brace_end + 1]
        item_data = _parse_item_block(block)
        item_data['item_id'] = item_id
        item_data['commented'] = False
        item_data['_raw'] = content[m.start():brace_end + 1]
        # Verificar si está dentro de un bloque comentado
        line_start = content.rfind('\n', 0, m.start()) + 1
        prefix = content[line_start:m.start()]
        if prefix.strip().startswith('--'):
            item_data['commented'] = True
        items.append(item_data)

    # Buscar items comentados: -- ["item_id"] = { ... }
    pattern_commented = re.compile(
        r'^(\s*-- \s*)\["([^"]+)"\]\s*=\s*\{',
        re.MULTILINE
    )
    for m in pattern_commented.finditer(content):
        item_id = m.group(2)
        # Evitar duplicados (ya capturados arriba)
        if any(i['item_id'] == item_id and i['commented'] for i in items):
            continue
        # Para items comentados, extraer el bloque completo
        # Buscar el final del bloque comentado (línea con solo "-- },")
        start_pos = m.start()
        block_lines = []
        pos = start_pos
        found_end = False
        while pos < len(content):
            line_end = content.find('\n', pos)
            if line_end == -1:
                line_end = len(content)
            line = content[pos:line_end]
            block_lines.append(line)
            stripped = line.strip()
            # Fin del bloque: "-- }," o "-- }"
            if re.match(r'^--\s*\},?\s*$', stripped):
                found_end = True
                pos = line_end + 1
                break
            pos = line_end + 1
        if not found_end:
            continue
        raw_block = '\n'.join(block_lines)
        # Eliminar prefijo de comentario para parsear
        uncommented = re.sub(r'^(\s*)--\s?', r'\1', raw_block, flags=re.MULTILINE)
        # Intentar parsear
        brace_match = re.search(r'\{', uncommented)
        if brace_match:
            brace_end = _find_balanced_brace(uncommented, brace_match.start())
            if brace_end != -1:
                block = uncommented[brace_match.start():brace_end + 1]
                item_data = _parse_item_block(block)
                item_data['item_id'] = item_id
                item_data['commented'] = True
                item_data['_raw'] = raw_block
                # No añadir si ya existe como activo
                if not any(i['item_id'] == item_id and not i['commented'] for i in items):
                    items.append(item_data)

    return items


def _parse_item_block(block: str) -> dict:
    """Parsea un bloque Lua de un item y extrae sus propiedades."""
    data = {
        'name': '',
        'hunger': 0.0,
        'thirst': 0.0,
        'stress': 0.0,
        'urine': 0.0,
        'keepWhenUse': False,
        'snakePoisonAntidote': False,
        'tempModifier_value': 0.0,
        'tempModifier_duration': 25000,
        'player_healthCore': 0.0,
        'player_staminaCore': 0.0,
        'player_healthOuter': 0.0,
        'player_boostHealth': [0, 0],
        'player_boostStamina': [0, 0],
        'horse_healthCore': 0.0,
        'horse_staminaCore': 0.0,
        'horse_healthOuter': 0.0,
        'horse_boostHealth': [0, 0],
        'horse_boostStamina': [0, 0],
        'effects_enabled': True,
        'effects_animationName': 'eat',
        'effects_screenFx': '',
        'effects_prop': '',
        'effects_buffEffect_name': '',
        'effects_buffEffect_duration': 0,
        'drunk_min': 0,
        'drunk_max': 0,
        'drunk_intensity': 0,
        'cooldown': 0,
        'useOnMount': True,
        'returnItems': [],
        'requiredItems': [],
        'has_tempModifier': False,
        'has_player': False,
        'has_horse': False,
        'has_effects': False,
        'has_drunk': False,
        'has_returnItems': False,
        'has_requiredItems': False,
        'has_clientAction': False,
        'clientAction_code': '',
    }

    # name
    m = re.search(r'name\s*=\s*"([^"]*)"', block)
    if m:
        data['name'] = m.group(1)

    # Simple numeric/bool fields
    for field in ('hunger', 'thirst', 'stress', 'urine'):
        m = re.search(rf'{field}\s*=\s*([-\d.]+)', block)
        if m:
            data[field] = float(m.group(1))

    # keepWhenUse
    if re.search(r'keepWhenUse\s*=\s*true', block):
        data['keepWhenUse'] = True

    # snakePoisonAntidote
    if re.search(r'snakePoisonAntidote\s*=\s*true', block):
        data['snakePoisonAntidote'] = True

    # cooldown
    m = re.search(r'cooldown\s*=\s*(false|\d+)', block)
    if m:
        data['cooldown'] = 0 if m.group(1) == 'false' else int(m.group(1))

    # useOnMount
    m = re.search(r'useOnMount\s*=\s*(true|false)', block)
    if m:
        data['useOnMount'] = m.group(1) == 'true'

    # tempModifier
    tm_match = re.search(r'tempModifier\s*=\s*\{', block)
    if tm_match:
        data['has_tempModifier'] = True
        m = re.search(r'tempModifier\s*=\s*\{[^}]*value\s*=\s*([-\d.]+)', block)
        if m:
            data['tempModifier_value'] = float(m.group(1))
        m = re.search(r'tempModifier\s*=\s*\{[^}]*duration\s*=\s*(\d+)', block)
        if m:
            data['tempModifier_duration'] = int(m.group(1))

    # player
    player_match = re.search(r'player\s*=\s*\{', block)
    if player_match:
        data['has_player'] = True
        player_end = _find_balanced_brace(block, player_match.end() - 1)
        if player_end != -1:
            player_block = block[player_match.end() - 1:player_end + 1]
            for field in ('healthCore', 'staminaCore', 'healthOuter'):
                m = re.search(rf'{field}\s*=\s*([-\d.]+)', player_block)
                if m:
                    data[f'player_{field}'] = float(m.group(1))
            for field in ('boostHealth', 'boostStamina'):
                m = re.search(rf'{field}\s*=\s*\{{\s*([-\d.]+)\s*,\s*([-\d.]+)\s*\}}', player_block)
                if m:
                    data[f'player_{field}'] = [float(m.group(1)), float(m.group(2))]

    # horse
    horse_match = re.search(r'horse\s*=\s*\{', block)
    if horse_match:
        data['has_horse'] = True
        horse_end = _find_balanced_brace(block, horse_match.end() - 1)
        if horse_end != -1:
            horse_block = block[horse_match.end() - 1:horse_end + 1]
            for field in ('healthCore', 'staminaCore', 'healthOuter'):
                m = re.search(rf'{field}\s*=\s*([-\d.]+)', horse_block)
                if m:
                    data[f'horse_{field}'] = float(m.group(1))
            for field in ('boostHealth', 'boostStamina'):
                m = re.search(rf'{field}\s*=\s*\{{\s*([-\d.]+)\s*,\s*([-\d.]+)\s*\}}', horse_block)
                if m:
                    data[f'horse_{field}'] = [float(m.group(1)), float(m.group(2))]

    # effects
    effects_match = re.search(r'effects\s*=\s*\{', block)
    if effects_match:
        data['has_effects'] = True
        effects_end = _find_balanced_brace(block, effects_match.end() - 1)
        if effects_end != -1:
            effects_block = block[effects_match.end() - 1:effects_end + 1]
            m = re.search(r'enabled\s*=\s*(true|false)', effects_block)
            if m:
                data['effects_enabled'] = m.group(1) == 'true'
            m = re.search(r'animationName\s*=\s*"([^"]*)"', effects_block)
            if m:
                data['effects_animationName'] = m.group(1)
            m = re.search(r'screenFx\s*=\s*"([^"]*)"', effects_block)
            if m:
                data['effects_screenFx'] = m.group(1)
            m = re.search(r'prop\s*=\s*"([^"]*)"', effects_block)
            if m:
                data['effects_prop'] = m.group(1)
            m = re.search(r'buffEffect\s*=\s*\{\s*"([^"]*)"\s*,\s*(\d+)', effects_block)
            if m:
                data['effects_buffEffect_name'] = m.group(1)
                data['effects_buffEffect_duration'] = int(m.group(2))

    # drunk
    drunk_match = re.search(r'drunk\s*=\s*\{', block)
    if drunk_match:
        data['has_drunk'] = True
        drunk_end = _find_balanced_brace(block, drunk_match.end() - 1)
        if drunk_end != -1:
            drunk_block = block[drunk_match.end() - 1:drunk_end + 1]
            for field in ('min', 'max', 'intensity'):
                m = re.search(rf'{field}\s*=\s*([-\d.]+)', drunk_block)
                if m:
                    data[f'drunk_{field}'] = int(float(m.group(1)))

    # returnItems
    ri_match = re.search(r'returnItems\s*=\s*\{', block)
    if ri_match:
        data['has_returnItems'] = True
        ri_end = _find_balanced_brace(block, ri_match.end() - 1)
        if ri_end != -1:
            ri_block = block[ri_match.end() - 1:ri_end + 1]
            for item_m in re.finditer(r'name\s*=\s*"([^"]*)".*?amount\s*=\s*(\d+)', ri_block, re.DOTALL):
                data['returnItems'].append({
                    'name': item_m.group(1),
                    'amount': int(item_m.group(2)),
                })

    # requiredItems
    rq_match = re.search(r'requiredItems\s*=\s*\{', block)
    if rq_match:
        data['has_requiredItems'] = True
        rq_end = _find_balanced_brace(block, rq_match.end() - 1)
        if rq_end != -1:
            rq_block = block[rq_match.end() - 1:rq_end + 1]
            for item_m in re.finditer(r'name\s*=\s*"([^"]*)".*?amount\s*=\s*(\d+)', rq_block, re.DOTALL):
                data['requiredItems'].append({
                    'name': item_m.group(1),
                    'amount': int(item_m.group(2)),
                })

    # ClientAction
    ca_match = re.search(r'ClientAction\s*=\s*function\s*\(\)', block)
    if ca_match:
        data['has_clientAction'] = True
        # Extraer el cuerpo hasta "end,"
        end_match = re.search(r'end\s*,', block[ca_match.end():])
        if end_match:
            data['clientAction_code'] = block[ca_match.end():ca_match.end() + end_match.start()].strip()

    return data


# ============================================================================
# GENERADOR — Genera bloque Lua para un item
# ============================================================================

def generate_metabolism_block(data: dict) -> str:
    """Genera el bloque Lua para un item de metabolismo."""
    item_id = data.get('item_id', 'new_item')
    lines = []
    lines.append(f'    ["{item_id}"] = {{')
    lines.append(f'        name = "{data.get("name", item_id)}",')

    # keepWhenUse
    if data.get('keepWhenUse'):
        lines.append('        keepWhenUse = true,')

    # Stats base
    lines.append(f'        hunger = {_fmt_num(data.get("hunger", 0))},')
    lines.append(f'        thirst = {_fmt_num(data.get("thirst", 0))},')

    if data.get('urine', 0) != 0:
        lines.append(f'        urine = {_fmt_num(data["urine"])},')

    lines.append(f'        stress = {_fmt_num(data.get("stress", 0))},')

    # snakePoisonAntidote
    if data.get('snakePoisonAntidote'):
        lines.append('        snakePoisonAntidote = true,')

    # tempModifier
    if data.get('has_tempModifier'):
        lines.append('        tempModifier = {')
        lines.append(f'            value = {_fmt_num(data.get("tempModifier_value", 0))},')
        lines.append(f'            duration = {int(data.get("tempModifier_duration", 25000))}')
        lines.append('        },')

    # player
    if data.get('has_player'):
        lines.append('        player = {')
        player_fields = []
        for field, key in [('healthCore', 'player_healthCore'),
                           ('staminaCore', 'player_staminaCore'),
                           ('healthOuter', 'player_healthOuter')]:
            val = data.get(key, 0)
            if val != 0 or field in ('healthCore', 'staminaCore'):
                player_fields.append(f'            {field} = {_fmt_num(val)}')
        # boosts
        for field, key in [('boostHealth', 'player_boostHealth'),
                           ('boostStamina', 'player_boostStamina')]:
            val = data.get(key, [0, 0])
            if val != [0, 0]:
                player_fields.append(f'            {field} = {{ {_fmt_num(val[0])}, {_fmt_num(val[1])} }}')
        lines.append(',\n'.join(player_fields))
        lines.append('        },')

    # horse
    if data.get('has_horse'):
        lines.append('        horse = {')
        horse_fields = []
        for field, key in [('healthCore', 'horse_healthCore'),
                           ('staminaCore', 'horse_staminaCore'),
                           ('healthOuter', 'horse_healthOuter')]:
            val = data.get(key, 0)
            if val != 0 or field in ('healthCore', 'staminaCore'):
                horse_fields.append(f'            {field} = {_fmt_num(val)}')
        for field, key in [('boostHealth', 'horse_boostHealth'),
                           ('boostStamina', 'horse_boostStamina')]:
            val = data.get(key, [0, 0])
            if val != [0, 0]:
                horse_fields.append(f'            {field} = {{ {_fmt_num(val[0])}, {_fmt_num(val[1])} }}')
        lines.append(',\n'.join(horse_fields))
        lines.append('        },')

    # effects
    if data.get('has_effects'):
        lines.append('        effects = {')
        lines.append(f'            enabled = {"true" if data.get("effects_enabled", True) else "false"},')
        lines.append(f'            animationName = "{data.get("effects_animationName", "eat")}"')
        if data.get('effects_screenFx'):
            # Replace last line's ending to add comma
            lines[-1] = lines[-1].rstrip() + ','
            lines.append(f'            screenFx = "{data["effects_screenFx"]}"')
        if data.get('effects_prop'):
            lines[-1] = lines[-1].rstrip() + ','
            lines.append(f'            prop = "{data["effects_prop"]}"')
        if data.get('effects_buffEffect_name'):
            lines[-1] = lines[-1].rstrip() + ','
            lines.append(f'            buffEffect = {{"{data["effects_buffEffect_name"]}", {int(data.get("effects_buffEffect_duration", 10))}}}')
        lines.append('        }')

    # drunk
    if data.get('has_drunk'):
        lines.append(',')  # close effects with comma
        lines[-2] = lines[-2]  # effects closing brace already there
        # Actually we need a comma after effects block
        # Fix: ensure previous block ends with comma
        _ensure_trailing_comma(lines)
        lines.append('        drunk = {')
        if data.get('drunk_min', 0):
            lines.append(f'            min = {int(data["drunk_min"])},')
        if data.get('drunk_max', 0):
            lines.append(f'            max = {int(data["drunk_max"])},')
        if data.get('drunk_intensity', 0):
            lines.append(f'            intensity = {int(data["drunk_intensity"])}')
        lines.append('        }')

    # returnItems
    if data.get('has_returnItems') and data.get('returnItems'):
        _ensure_trailing_comma(lines)
        lines.append('        returnItems = {')
        for ri in data['returnItems']:
            lines.append(f'            {{ name = "{ri["name"]}", amount = {ri["amount"]} }},')
        lines.append('        }')

    # requiredItems
    if data.get('has_requiredItems') and data.get('requiredItems'):
        _ensure_trailing_comma(lines)
        lines.append('        requiredItems = {')
        for ri in data['requiredItems']:
            lines.append(f'            {{ name = "{ri["name"]}", amount = {ri["amount"]} }},')
        lines.append('        }')

    # cooldown
    if data.get('cooldown', 0):
        _ensure_trailing_comma(lines)
        lines.append(f'        cooldown = {int(data["cooldown"])},')

    # useOnMount
    if not data.get('useOnMount', True):
        _ensure_trailing_comma(lines)
        lines.append('        useOnMount = false,')

    # ClientAction
    if data.get('has_clientAction') and data.get('clientAction_code'):
        _ensure_trailing_comma(lines)
        lines.append('        ClientAction = function()')
        for code_line in data['clientAction_code'].split('\n'):
            lines.append(f'            {code_line.strip()}')
        lines.append('        end,')

    lines.append('    },')
    return '\n'.join(lines)


def _fmt_num(val) -> str:
    """Formatea un número para Lua: entero si no tiene decimal, float si sí."""
    if isinstance(val, float):
        if val == int(val) and abs(val) < 1000:
            return str(int(val))
        return f"{val:.1f}" if val == round(val, 1) else str(val)
    return str(int(val))


def _ensure_trailing_comma(lines: list):
    """Asegura que la última línea significativa tenga una coma al final."""
    for i in range(len(lines) - 1, -1, -1):
        stripped = lines[i].rstrip()
        if stripped and not stripped.endswith(',') and not stripped.endswith('{'):
            lines[i] = stripped + ','
            break
        elif stripped.endswith(',') or stripped.endswith('{'):
            break


# ============================================================================
# OPERACIONES SOBRE EL ARCHIVO COMPLETO
# ============================================================================

def add_item_to_config(content: str, item_block: str) -> str:
    """Añade un nuevo item al final de Usables.itemsLHR (antes del cierre })."""
    # Buscar la última llave de cierre de la tabla
    last_brace = content.rfind('}')
    if last_brace == -1:
        return content + '\n' + item_block
    # Insertar antes del cierre
    before = content[:last_brace].rstrip()
    after = content[last_brace:]
    # Asegurar coma en el item anterior
    if not before.endswith(','):
        before += ','
    return before + '\n' + item_block + '\n' + after


def replace_item_in_config(content: str, item_id: str, new_block: str) -> str | None:
    """Reemplaza un item existente por su nuevo bloque."""
    # Buscar el item activo
    pattern = re.compile(
        rf'^(\s*)\["{re.escape(item_id)}"\]\s*=\s*\{{',
        re.MULTILINE
    )
    m = pattern.search(content)
    if not m:
        return None
    brace_start = content.index('{', m.start() + len(m.group(0)) - 1)
    brace_end = _find_balanced_brace(content, brace_start)
    if brace_end == -1:
        return None
    # Incluir la coma y/o espacio después del cierre
    end_pos = brace_end + 1
    if end_pos < len(content) and content[end_pos] == ',':
        end_pos += 1
    return content[:m.start()] + new_block + content[end_pos:]


def delete_item_from_config(content: str, item_id: str) -> str | None:
    """Elimina un item del config."""
    pattern = re.compile(
        rf'^(\s*)\["{re.escape(item_id)}"\]\s*=\s*\{{',
        re.MULTILINE
    )
    m = pattern.search(content)
    if not m:
        return None
    brace_start = content.index('{', m.start() + len(m.group(0)) - 1)
    brace_end = _find_balanced_brace(content, brace_start)
    if brace_end == -1:
        return None
    end_pos = brace_end + 1
    if end_pos < len(content) and content[end_pos] == ',':
        end_pos += 1
    # Eliminar también la línea vacía siguiente si existe
    if end_pos < len(content) and content[end_pos] == '\n':
        end_pos += 1
    return content[:m.start()] + content[end_pos:]


def comment_item_in_config(content: str, item_id: str) -> str | None:
    """Comenta un item (lo desactiva)."""
    pattern = re.compile(
        rf'^(\s*)\["{re.escape(item_id)}"\]\s*=\s*\{{',
        re.MULTILINE
    )
    m = pattern.search(content)
    if not m:
        return None
    brace_start = content.index('{', m.start() + len(m.group(0)) - 1)
    brace_end = _find_balanced_brace(content, brace_start)
    if brace_end == -1:
        return None
    end_pos = brace_end + 1
    if end_pos < len(content) and content[end_pos] == ',':
        end_pos += 1
    original = content[m.start():end_pos]
    commented = '\n'.join('    -- ' + line.lstrip() if line.strip() else line
                          for line in original.split('\n'))
    return content[:m.start()] + commented + content[end_pos:]


def uncomment_item_in_config(content: str, item_id: str) -> str | None:
    """Descomenta un item (lo reactiva)."""
    # Buscar bloque comentado
    pattern = re.compile(
        rf'^\s*--\s*\["{re.escape(item_id)}"\]\s*=\s*\{{',
        re.MULTILINE
    )
    m = pattern.search(content)
    if not m:
        return None
    # Encontrar todas las líneas del bloque comentado
    start_pos = m.start()
    pos = start_pos
    block_lines = []
    while pos < len(content):
        line_end = content.find('\n', pos)
        if line_end == -1:
            line_end = len(content)
            line = content[pos:line_end]
            block_lines.append(line)
            pos = line_end
            break
        line = content[pos:line_end]
        block_lines.append(line)
        stripped = line.strip()
        if re.match(r'^--\s*\},?\s*$', stripped):
            pos = line_end + 1
            break
        pos = line_end + 1
    original = '\n'.join(block_lines)
    uncommented = re.sub(r'^(\s*)--\s?', r'\1', original, flags=re.MULTILINE)
    return content[:start_pos] + uncommented + content[start_pos + len(original):]


def sort_items_alphabetically(content: str) -> str | None:
    """Ordena los items dentro de Usables.itemsLHR alfabéticamente."""
    # Encontrar inicio y fin de la tabla itemsLHR
    table_match = re.search(r'Usables\.itemsLHR\s*=\s*\{', content)
    if not table_match:
        return None
    brace_start = content.index('{', table_match.start())
    brace_end = _find_balanced_brace(content, brace_start)
    if brace_end == -1:
        return None

    inner = content[brace_start + 1:brace_end]
    items = parse_metabolism_items(content)
    if not items:
        return content

    # Separar por secciones: items activos y comentados
    active = [i for i in items if not i['commented']]
    commented = [i for i in items if i['commented']]
    active.sort(key=lambda x: x['item_id'].lower())
    commented.sort(key=lambda x: x['item_id'].lower())

    # Regenerar
    new_lines = []
    # Preservar comentarios de sección del original
    for item in active:
        new_lines.append(generate_metabolism_block(item))
    if commented:
        new_lines.append('')
        for item in commented:
            block = generate_metabolism_block(item)
            commented_block = '\n'.join('    -- ' + line.lstrip() if line.strip() else line
                                        for line in block.split('\n'))
            new_lines.append(commented_block)

    header = content[:brace_start + 1]
    footer = content[brace_end:]
    return header + '\n' + '\n'.join(new_lines) + '\n' + footer
