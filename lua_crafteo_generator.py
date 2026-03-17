"""
Generador de bloques de código Lua para VORP Crafting
Lectura, escritura, parseo y validación de configs de crafteo.
"""
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent
CONFIGS_PATH = BASE_DIR / "configs"

# ============================================================================
# MODO DE ALMACENAMIENTO (local / drive)
# ============================================================================
_storage_mode = 'local'
_drive_module = None


def set_storage_mode(mode: str, drive_module=None):
    global _storage_mode, _drive_module
    _storage_mode = mode
    _drive_module = drive_module


def get_storage_mode() -> str:
    return _storage_mode


# ============================================================================
# NOMBRES DE CONFIG
# ============================================================================
_NAME_MAP = {
    'agricultor': 'Agricultor', 'armero': 'Armero', 'artesano': 'Artesano',
    'bandas': 'Bandas', 'cocinaDulce': 'CocinaDulce', 'cocinaMixta': 'CocinaMixta',
    'cocinaPacks': 'CocinaPacks', 'cocinaTier1': 'CocinaTier1',
    'cocinaTier2': 'CocinaTier2', 'cocinaTier3': 'CocinaTier3',
    'destilador': 'Destilador', 'distribuidora': 'Distribuidora',
    'establo': 'Establo', 'ganadero': 'Ganadero', 'medicos': 'Medicos',
    'perista': 'Perista', 'pescadero': 'Pescadero', 'tabacalero': 'Tabacalero',
}


def get_config_name(job_key: str) -> str:
    """Obtiene el nombre del config para Lua (Config.X) basado en la clave del job."""
    if job_key in _NAME_MAP:
        return _NAME_MAP[job_key]
    content = get_config_file_content(job_key)
    if content:
        m = re.match(r'Config\.(\w+)\s*=', content)
        if m:
            return m.group(1)
    return job_key[0].upper() + job_key[1:] if job_key else job_key


def register_config_name(job_key: str, config_name: str):
    """Registra un nuevo mapeo job_key -> Config.Name."""
    _NAME_MAP[job_key] = config_name


# ============================================================================
# LECTURA / ESCRITURA DE ARCHIVOS
# ============================================================================

def get_config_file_content(job_key: str) -> str:
    """Lee el contenido de un archivo de configuración desde Drive."""
    filename = f"config_{job_key}.lua"
    if _storage_mode == 'drive' and _drive_module:
        try:
            return _drive_module.read_file(filename)
        except Exception as e:
            print(f"Error leyendo config desde Drive: {e}")
            return None
    return None


def save_config_file(job_key: str, content: str) -> bool:
    """Guarda el contenido de un archivo de configuración en Drive."""
    filename = f"config_{job_key}.lua"
    if _storage_mode == 'drive' and _drive_module:
        try:
            result = _drive_module.write_file(filename, content)
            return bool(result)
        except Exception as e:
            import traceback
            traceback.print_exc()
            raise
    return False


def get_available_configs() -> list:
    """Obtiene la lista de claves de jobs disponibles desde Drive."""
    if _storage_mode == 'drive' and _drive_module:
        try:
            return _drive_module.get_available_config_keys()
        except Exception as e:
            print(f"Error listando configs desde Drive: {e}")
            return []
    return []


# ============================================================================
# GENERACIÓN DE CÓDIGO LUA
# ============================================================================

def generate_crafting_block(data: dict) -> str:
    """Genera un bloque de código Lua para un crafteo en formato VORP Crafting."""

    # Ingredientes
    items_lines = []
    for ing in data['ingredientes']:
        take_value = "true" if data.get('take_items', True) else "false"
        items_lines.append(
            f'{{\n        name = "{ing["name"]}",\n'
            f'        count = {ing["count"]},\n'
            f'        take = {take_value}\n    }}'
        )
    items_block = "{" + ", ".join(items_lines) + "}"

    # Recompensas
    recompensas = data.get('recompensas', [])
    if not recompensas:
        recompensas = [{'name': data.get('recompensa', ''), 'count': data.get('cantidad_recompensa', 1)}]
    reward_lines = []
    for rew in recompensas:
        reward_lines.append(
            f'{{\n        name = "{rew["name"]}",\n        count = {rew["count"]}\n    }}'
        )
    reward_block = "{" + ", ".join(reward_lines) + "}"

    # Job
    job_value = data.get('job', 0)
    job_str = job_value if isinstance(job_value, str) and job_value.startswith('{') else str(job_value)

    # Pack (opcional)
    pack_value = data.get('pack', '')
    pack_line = f'\n    Pack = "{pack_value}",' if pack_value else ''

    lua_code = (
        "{\n"
        f"    TakeItems = {str(data.get('take_items', True)).lower()},\n"
        f"    CurrencyType = {data.get('currency_type', 0)},\n"
        f"    Location = {data.get('location', 0)},\n"
        f'    Animation = "{data.get("animation", "craft")}",\n'
        f'    Category = "{data["categoria"]}",\n'
        f'    Text = "{data["nombre"]}",{pack_line}\n'
        f'    Desc = "{data["descripcion"]}",\n'
        f"    Reward = {reward_block},\n"
        f"    Minlvl = {data.get('nivel_minimo', 0)},\n"
        f"    UseCurrencyMode = {str(data.get('use_currency', False)).lower()},\n"
        f"    Job = {job_str},\n"
        f'    Type = "{data.get("tipo", "item")}",\n'
        f"    Items = {items_block}\n"
        "}"
    )
    return lua_code


# ============================================================================
# CREAR CONFIG NUEVO / VACÍO
# ============================================================================

def create_empty_config(job_key: str, config_name: str = None) -> str:
    """Genera el contenido de un config nuevo vacío para un job."""
    if not config_name:
        config_name = get_config_name(job_key)
    return (
        f"Config.{config_name} = {{\n}}\n\n"
        f"-- Agregamos a la configuración general los items de {job_key}\n"
        f"for _, item in pairs(Config.{config_name}) do\n"
        f"    table.insert(Config.Crafting, item)\n"
        f"end\n"
    )


# ============================================================================
# AÑADIR CRAFTEO A CONFIG (robusto con conteo de llaves)
# ============================================================================

def _find_main_table_close(content: str) -> int:
    """
    Encuentra la posición de la llave '}' que cierra la tabla Config.X = { ... }.
    Ignora strings y comentarios. Retorna el índice o -1.
    """
    header = re.match(r'Config\.\w+\s*=\s*\{', content)
    if not header:
        return -1

    depth = 0
    i = header.end() - 1  # posición del '{'
    in_string = False
    in_comment = False
    length = len(content)

    while i < length:
        c = content[i]
        if not in_string and not in_comment and i + 1 < length and content[i:i+2] == '--':
            in_comment = True
            i += 2
            continue
        if in_comment:
            if c == '\n':
                in_comment = False
            i += 1
            continue
        if c == '"' and not in_comment:
            in_string = not in_string
            i += 1
            continue
        if in_string:
            if c == '\\':
                i += 2
                continue
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


def add_crafting_to_config(job_key: str, new_crafting_block: str) -> str:
    """Añade un nuevo bloque de crafteo al archivo de configuración existente."""
    existing_content = get_config_file_content(job_key)

    if not existing_content:
        config_name = get_config_name(job_key)
        return (
            f"Config.{config_name} = {{{new_crafting_block}\n}}\n\n"
            f"-- Agregamos a la configuración general los items de {job_key}\n"
            f"for _, item in pairs(Config.{config_name}) do\n"
            f"    table.insert(Config.Crafting, item)\n"
            f"end\n"
        )

    close_pos = _find_main_table_close(existing_content)
    if close_pos == -1:
        return existing_content + "\n" + new_crafting_block

    before = existing_content[:close_pos].rstrip()
    after = existing_content[close_pos:]  # empieza con '}'

    header = re.match(r'Config\.\w+\s*=\s*\{', existing_content)
    inner = existing_content[header.end():close_pos].strip()

    if inner:
        if not before.endswith(','):
            before += ','
        return before + "\n" + new_crafting_block + "\n" + after
    else:
        return before + "\n" + new_crafting_block + "\n" + after


# ============================================================================
# PARSER DE LUA
# ============================================================================

def _extract_lua_string(value: str) -> str:
    m = re.match(r'^"(.*)"$', value.strip())
    return m.group(1) if m else value.strip()


def _parse_lua_table_items(block: str) -> list:
    """Parsea una tabla Lua de items/rewards: {{name="x", count=1}, ...}"""
    items = []
    depth = 0
    current = ""
    for char in block:
        if char == '{':
            depth += 1
            if depth == 2:
                current = ""
            continue
        elif char == '}':
            depth -= 1
            if depth == 1 and current.strip():
                item = {}
                for pair in re.finditer(r'(\w+)\s*=\s*("[^"]*"|\w+)', current):
                    key = pair.group(1)
                    val = pair.group(2)
                    if val.startswith('"'):
                        item[key] = val.strip('"')
                    elif val == 'true':
                        item[key] = True
                    elif val == 'false':
                        item[key] = False
                    else:
                        try:
                            item[key] = int(val)
                        except ValueError:
                            item[key] = val
                if item:
                    items.append(item)
                current = ""
                continue
            elif depth == 0:
                break
        if depth >= 2:
            current += char
    return items


def _parse_lua_job(value: str):
    value = value.strip()
    if value.startswith('{'):
        return value
    try:
        return int(value)
    except ValueError:
        return value


def parse_crafting_blocks(lua_content: str) -> list:
    """Parsea un archivo de config Lua y extrae todos los bloques de crafteo."""
    crafteos = []
    if not lua_content:
        return crafteos

    header_match = re.match(r'Config\.\w+\s*=\s*\{', lua_content)
    if not header_match:
        return crafteos

    content_start = header_match.end()
    depth = 0
    block_start = None
    i = content_start

    while i < len(lua_content):
        char = lua_content[i]
        if lua_content[i:i+2] == '--':
            line_end = lua_content.find('\n', i)
            if line_end == -1:
                break
            i = line_end + 1
            continue
        if char == '{':
            if depth == 0:
                block_start = i
            depth += 1
        elif char == '}':
            depth -= 1
            if depth == 0 and block_start is not None:
                block_text = lua_content[block_start:i+1]
                if 'Text' in block_text and 'Items' in block_text:
                    crafteo = _parse_single_block(block_text)
                    if crafteo:
                        crafteo['_raw_block'] = block_text
                        crafteo['_start_pos'] = block_start
                        crafteo['_end_pos'] = i + 1
                        crafteos.append(crafteo)
                block_start = None
        i += 1

    return crafteos


def _parse_single_block(block: str) -> dict:
    """Parsea un bloque individual de crafteo Lua y lo convierte a dict."""
    crafteo = {}

    m = re.search(r'TakeItems\s*=\s*(true|false)', block)
    if m: crafteo['take_items'] = m.group(1) == 'true'

    m = re.search(r'CurrencyType\s*=\s*(\d+)', block)
    if m: crafteo['currency_type'] = int(m.group(1))

    m = re.search(r'Location\s*=\s*(\d+)', block)
    if m: crafteo['location'] = int(m.group(1))

    m = re.search(r'Animation\s*=\s*"([^"]*)"', block)
    if m: crafteo['animation'] = m.group(1)

    m = re.search(r'Category\s*=\s*"([^"]*)"', block)
    if m: crafteo['categoria'] = m.group(1)

    m = re.search(r'Text\s*=\s*"([^"]*)"', block)
    if m: crafteo['nombre'] = m.group(1)

    m = re.search(r'Desc\s*=\s*"([^"]*)"', block)
    if m: crafteo['descripcion'] = m.group(1)

    m = re.search(r'Minlvl\s*=\s*(\d+)', block)
    if m: crafteo['nivel_minimo'] = int(m.group(1))

    m = re.search(r'UseCurrencyMode\s*=\s*(true|false)', block)
    if m: crafteo['use_currency'] = m.group(1) == 'true'

    m = re.search(r'Type\s*=\s*"([^"]*)"', block)
    if m: crafteo['tipo'] = m.group(1)

    m = re.search(r'Ilegal\s*=\s*(true|false)', block)
    if m: crafteo['ilegal'] = m.group(1) == 'true'

    m = re.search(r'Pack\s*=\s*"([^"]*)"', block)
    if m: crafteo['pack'] = m.group(1)

    m = re.search(r'Job\s*=\s*(\{[^}]*\}|\d+)', block)
    if m: crafteo['job'] = _parse_lua_job(m.group(1))

    # Reward
    reward_start_m = re.search(r'Reward\s*=\s*\{', block)
    if reward_start_m:
        brace_start = reward_start_m.end() - 1
        depth = 0
        reward_end = brace_start
        for idx in range(brace_start, len(block)):
            if block[idx] == '{': depth += 1
            elif block[idx] == '}':
                depth -= 1
                if depth == 0:
                    reward_end = idx + 1
                    break
        crafteo['recompensas'] = _parse_lua_table_items(block[brace_start:reward_end])

    # Items
    items_start_m = re.search(r'\bItems\s*=\s*\{', block)
    if items_start_m:
        brace_start = items_start_m.end() - 1
        depth = 0
        items_end = brace_start
        for idx in range(brace_start, len(block)):
            if block[idx] == '{': depth += 1
            elif block[idx] == '}':
                depth -= 1
                if depth == 0:
                    items_end = idx + 1
                    break
        crafteo['ingredientes'] = _parse_lua_table_items(block[brace_start:items_end])

    return crafteo


# ============================================================================
# REEMPLAZAR / ELIMINAR / COMENTAR / DESCOMENTAR CRAFTEOS
# ============================================================================

def replace_crafting_in_config(job_key: str, old_craft_name: str, new_crafting_block: str) -> str:
    """Reemplaza un bloque de crafteo existente por nombre."""
    content = get_config_file_content(job_key)
    if not content:
        return None
    crafteos = parse_crafting_blocks(content)
    target = next((c for c in crafteos if c.get('nombre') == old_craft_name), None)
    if not target:
        return None
    return content[:target['_start_pos']] + new_crafting_block + content[target['_end_pos']:]


def delete_crafting_from_config(job_key: str, craft_name: str) -> str:
    """Elimina un bloque de crafteo del archivo de configuración."""
    content = get_config_file_content(job_key)
    if not content:
        return None
    crafteos = parse_crafting_blocks(content)
    target = next((c for c in crafteos if c.get('nombre') == craft_name), None)
    if not target:
        return None

    before = content[:target['_start_pos']].rstrip()
    after = content[target['_end_pos']:].lstrip()

    if before.endswith(','):
        before = before[:-1]
    if after.startswith(','):
        after = after[1:].lstrip()

    return before + "\n" + after


def comment_crafting_in_config(job_key: str, craft_name: str) -> str:
    """Comenta (desactiva) un bloque de crafteo existente."""
    content = get_config_file_content(job_key)
    if not content:
        return None
    crafteos = parse_crafting_blocks(content)
    target = next((c for c in crafteos if c.get('nombre') == craft_name), None)
    if not target:
        return None

    start = target['_start_pos']
    end = target['_end_pos']
    raw_block = content[start:end]

    commented_block = '\n'.join('-- ' + line for line in raw_block.split('\n'))

    before = content[:start].rstrip()
    after_raw = content[end:]
    after = after_raw.lstrip(' \t')

    if after.startswith(','):
        after_pos = end + (len(after_raw) - len(after)) + 1
        if not before.endswith('\n'):
            before += '\n'
        new_content = before + commented_block + '\n' + content[after_pos:]
    else:
        if before.endswith(','):
            before = before[:-1]
        if not before.endswith('\n'):
            before += '\n'
        new_content = before + commented_block + '\n' + after

    return new_content


def parse_commented_blocks(lua_content: str) -> list:
    """Busca bloques de crafteo comentados (desactivados) en un archivo Lua."""
    bloques = []
    if not lua_content:
        return bloques

    lines = lua_content.split('\n')
    i = 0

    while i < len(lines):
        stripped = lines[i].strip()
        if stripped == '-- {' or stripped == '-- {,':
            block_lines = [lines[i]]
            block_start_line = i
            j = i + 1
            while j < len(lines):
                next_stripped = lines[j].strip()
                if next_stripped.startswith('--'):
                    block_lines.append(lines[j])
                    if next_stripped in ('-- },', '-- }', '-- },'):
                        j += 1
                        break
                elif next_stripped == '':
                    block_lines.append(lines[j])
                else:
                    break
                j += 1

            full_commented = '\n'.join(block_lines)
            if 'Text' in full_commented and 'Items' in full_commented:
                uncommented = '\n'.join(
                    l.strip().removeprefix('-- ').removeprefix('--')
                    for l in block_lines if l.strip().startswith('--')
                )
                nombre = ''
                descripcion = ''
                m_text = re.search(r'Text\s*=\s*"([^"]*)"', uncommented)
                if m_text: nombre = m_text.group(1)
                m_desc = re.search(r'Desc\s*=\s*"([^"]*)"', uncommented)
                if m_desc: descripcion = m_desc.group(1)

                pos_start = sum(len(lines[k]) + 1 for k in range(block_start_line))
                pos_end = sum(len(lines[k]) + 1 for k in range(j))

                bloques.append({
                    'nombre': nombre,
                    'descripcion': descripcion,
                    '_commented_text': full_commented,
                    '_start_pos': pos_start,
                    '_end_pos': pos_end,
                    '_start_line': block_start_line,
                    '_end_line': j
                })
            i = j
        else:
            i += 1

    return bloques


def uncomment_crafting_in_config(job_key: str, craft_name: str) -> str:
    """Descomenta (reactiva) un bloque de crafteo comentado."""
    content = get_config_file_content(job_key)
    if not content:
        return None

    commented_blocks = parse_commented_blocks(content)
    target = next((b for b in commented_blocks if b.get('nombre') == craft_name), None)
    if not target:
        return None

    start = target['_start_pos']
    end = target['_end_pos']
    commented_text = content[start:end]

    uncommented_lines = []
    for line in commented_text.split('\n'):
        stripped = line.strip()
        if stripped.startswith('-- '):
            uncommented_lines.append(line.replace('-- ', '', 1))
        elif stripped.startswith('--'):
            uncommented_lines.append(line.replace('--', '', 1))
        else:
            uncommented_lines.append(line)

    uncommented_block = '\n'.join(uncommented_lines).rstrip()
    if not uncommented_block.endswith('},') and not uncommented_block.endswith('}'):
        uncommented_block = uncommented_block.rstrip(',').rstrip() + '}'

    before = content[:start].rstrip()
    after = content[end:].lstrip()

    if before and before[-1] == '}':
        before += ','
    if after and after[0] == '{':
        if not uncommented_block.endswith(','):
            uncommented_block += ','

    return before + '\n' + uncommented_block + '\n' + after


# ============================================================================
# VALIDACIÓN DE SINTAXIS LUA
# ============================================================================

def validate_lua_syntax(lua_code: str) -> list:
    """
    Valida la sintaxis básica de un bloque o archivo Lua de crafteo.
    Retorna lista de errores (vacía = OK).
    """
    errors = []
    depth = 0
    in_string = False
    in_comment = False

    for i, c in enumerate(lua_code):
        if in_comment:
            if c == '\n':
                in_comment = False
            continue

        if not in_string and i + 1 < len(lua_code) and lua_code[i:i+2] == '--':
            in_comment = True
            continue

        if c == '"' and not in_comment:
            if i > 0 and lua_code[i-1] == '\\':
                continue
            in_string = not in_string
            continue

        if in_string:
            continue

        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth < 0:
                errors.append(f"Llave de cierre '}}' sin apertura (posición {i})")
                break

    if depth > 0:
        errors.append(f"Faltan {depth} llave(s) de cierre '}}'")

    if in_string:
        errors.append("String sin cerrar (falta comilla de cierre)")

    # Campos obligatorios solo en bloques de crafteo individuales
    if 'Config.' not in lua_code:
        required = ['TakeItems', 'Text', 'Reward', 'Items', 'Type']
        for field in required:
            if field not in lua_code:
                errors.append(f"Falta campo obligatorio: {field}")

    return errors


def validate_full_config(lua_code: str) -> list:
    """Valida un archivo config completo. Retorna lista de errores."""
    errors = validate_lua_syntax(lua_code)

    if not re.match(r'Config\.\w+\s*=\s*\{', lua_code):
        errors.append("El archivo debe empezar con Config.NombreJob = {")

    close = _find_main_table_close(lua_code)
    if close == -1 and 'Config.' in lua_code:
        errors.append("No se encontró el cierre de la tabla principal")

    if 'table.insert(Config.Crafting' not in lua_code:
        errors.append("Falta el bucle for...table.insert(Config.Crafting, item)")

    return errors