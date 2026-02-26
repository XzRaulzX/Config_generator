"""
Generador de bloques de código Lua para VORP Crafting
"""
import os
import re
from pathlib import Path

# Obtener el directorio base
BASE_DIR = Path(__file__).parent
CONFIGS_PATH = BASE_DIR / "configs"


def generate_crafting_block(data: dict) -> str:
    """
    Genera un bloque de código Lua para un crafteo en formato VORP Crafting
    
    Args:
        data: Diccionario con los datos del crafteo
    
    Returns:
        str: Código Lua formateado
    """
    
    # Formatear ingredientes
    items_lines = []
    for ing in data['ingredientes']:
        take_value = "true" if data.get('take_items', True) else "false"
        take_str = f",\n        take = {take_value}"
        items_lines.append(f"""{{
        name = "{ing['name']}",
        count = {ing['count']}{take_str}
    }}""")
    
    if len(items_lines) == 1:
        items_block = "{" + items_lines[0] + "}"
    else:
        items_block = "{" + ", ".join(items_lines) + "}"
    
    # Formatear recompensas (puede ser una lista de items)
    recompensas = data.get('recompensas', [])
    if not recompensas:
        # Compatibilidad con formato antiguo (un solo item)
        recompensas = [{
            'name': data.get('recompensa', ''),
            'count': data.get('cantidad_recompensa', 1)
        }]
    
    reward_lines = []
    for rew in recompensas:
        reward_lines.append(f"""{{
        name = "{rew['name']}",
        count = {rew['count']}
    }}""")
    
    if len(reward_lines) == 1:
        reward_block = "{" + reward_lines[0] + "}"
    else:
        reward_block = "{" + ", ".join(reward_lines) + "}"
    
    # Formatear Job (puede ser 0 o una tabla de strings)
    job_value = data.get('job', 0)
    if isinstance(job_value, str) and job_value.startswith('{'):
        job_str = job_value
    else:
        job_str = str(job_value)
    
    # Línea opcional de Pack
    pack_value = data.get('pack', '')
    pack_line = f'\n    Pack = "{pack_value}",' if pack_value else ''
    
    # Generar el bloque de crafteo
    lua_code = f"""{{
    TakeItems = {str(data.get('take_items', True)).lower()},
    CurrencyType = {data.get('currency_type', 0)},
    Location = {data.get('location', 0)},
    Animation = "{data.get('animation', 'craft')}",
    Category = "{data['categoria']}",
    Text = "{data['nombre']}",{pack_line}
    Desc = "{data['descripcion']}",
    Reward = {reward_block},
    Minlvl = {data.get('nivel_minimo', 0)},
    UseCurrencyMode = {str(data.get('use_currency', False)).lower()},
    Job = {job_str},
    Type = "{data.get('tipo', 'item')}",
    Items = {items_block}
}}"""
    
    return lua_code


def get_config_file_content(job_key: str) -> str:
    """
    Lee el contenido de un archivo de configuración existente
    
    Args:
        job_key: Clave del job (ej: 'armero', 'medicos')
    
    Returns:
        str: Contenido del archivo o None si no existe
    """
    config_file = CONFIGS_PATH / f"config_{job_key}.lua"
    try:
        if config_file.exists():
            with open(config_file, 'r', encoding='utf-8') as f:
                return f.read()
    except Exception as e:
        print(f"Error leyendo config: {e}")
    return None


def add_crafting_to_config(job_key: str, new_crafting_block: str) -> str:
    """
    Añade un nuevo bloque de crafteo al archivo de configuración existente
    
    Args:
        job_key: Clave del job
        new_crafting_block: Bloque de código Lua del nuevo crafteo
    
    Returns:
        str: Contenido completo del archivo con el nuevo crafteo añadido
    """
    import re
    
    existing_content = get_config_file_content(job_key)
    
    if existing_content:
        # El formato del archivo es:
        # Config.NombreJob = {{...crafteos...}}
        # 
        # -- Agregamos a la configuración general los items de artesano
        # for _, item in pairs(Config.NombreJob) do
        #     table.insert(Config.Crafting, item)
        # end
        
        # Buscar el patrón: }}\n\n-- Agregamos... (el cierre del array y el bucle for)
        pattern = r'(\}\})\s*(-- Agregamos.*?for _, item in pairs\(Config\.\w+\) do\s+table\.insert\(Config\.Crafting, item\)\s+end)'
        match = re.search(pattern, existing_content, re.DOTALL)
        
        if match:
            # Encontramos el patrón con bucle for
            # Insertar el nuevo crafteo antes del cierre }}
            before_close = existing_content[:match.start()]
            closing_and_for = match.group(1) + "\n\n" + match.group(2)
            
            # Asegurar que hay una coma antes del nuevo crafteo
            before_close = before_close.rstrip()
            if not before_close.endswith(','):
                before_close += ","
            
            new_content = before_close + " " + new_crafting_block + "\n" + closing_and_for
            return new_content
        else:
            # Intentar otro patrón: solo cierre de array sin bucle for
            # Config.Job = {...}
            pattern2 = r'(\})\s*$'
            match2 = re.search(pattern2, existing_content)
            
            if match2:
                before_close = existing_content[:match2.start()].rstrip()
                if not before_close.endswith(','):
                    before_close += ","
                
                # Añadir el nuevo crafteo y crear el bucle for
                config_name = get_config_name(job_key)
                for_loop = f"\n\n-- Agregamos a la configuración general los items de {job_key}\nfor _, item in pairs(Config.{config_name}) do\n    table.insert(Config.Crafting, item)\nend"
                
                new_content = before_close + " " + new_crafting_block + "\n}" + for_loop
                return new_content
        
        # Si no encontramos ningún patrón esperado, añadir al final
        return existing_content + "\n" + new_crafting_block
    else:
        # No existe el archivo, crear uno nuevo con el bucle for
        config_name = get_config_name(job_key)
        for_loop = f"\n\n-- Agregamos a la configuración general los items de {job_key}\nfor _, item in pairs(Config.{config_name}) do\n    table.insert(Config.Crafting, item)\nend"
        return f"Config.{config_name} = {{{new_crafting_block}\n}}" + for_loop


def get_config_name(job_key: str) -> str:
    """
    Obtiene el nombre del config para Lua basado en la clave del job
    
    Args:
        job_key: Clave del job (ej: 'cocinaTier1', 'medicos')
    
    Returns:
        str: Nombre formateado para Config.X
    """
    # Mapeo de nombres especiales
    name_map = {
        'agricultor': 'Agricultor',
        'armero': 'Armero',
        'artesano': 'Artesano',
        'bandas': 'Bandas',
        'cocinaDulce': 'CocinaDulce',
        'cocinaMixta': 'CocinaMixta',
        'cocinaPacks': 'CocinaPacks',
        'cocinaTier1': 'CocinaTier1',
        'cocinaTier2': 'CocinaTier2',
        'cocinaTier3': 'CocinaTier3',
        'destilador': 'Destilador',
        'distribuidora': 'Distribuidora',
        'establo': 'Establo',
        'ganadero': 'Ganadero',
        'medicos': 'Medicos',
        'perista': 'Perista',
        'pescadero': 'Pescadero',
        'tabacalero': 'Tabacalero'
    }
    return name_map.get(job_key, job_key.capitalize())


def get_available_configs() -> list:
    """
    Obtiene la lista de archivos de configuración disponibles
    
    Returns:
        list: Lista de nombres de archivos de config
    """
    configs = []
    if CONFIGS_PATH.exists():
        for f in CONFIGS_PATH.glob("config_*.lua"):
            configs.append(f.stem.replace("config_", ""))
    return sorted(configs)


# ============================================================================
# PARSER DE LUA - Para leer crafteos existentes
# ============================================================================

def _extract_lua_string(value: str) -> str:
    """Extrae un string Lua quitando comillas"""
    m = re.match(r'^"(.*)"$', value.strip())
    if m:
        return m.group(1)
    return value.strip()


def _parse_lua_table_items(block: str) -> list:
    """
    Parsea una tabla Lua de items/rewards como:
    {{name="x", count=1, take=true}, {name="y", count=2}}
    
    Returns:
        list de dicts con 'name', 'count' y opcionalmente 'take'
    """
    items = []
    depth = 0
    current = ""
    for char in block:
        if char == '{':
            depth += 1
            if depth <= 2:
                # Inicio de tabla externa (depth 1) o interna (depth 2)
                if depth == 2:
                    current = ""
                continue
        elif char == '}':
            depth -= 1
            if depth == 1 and current.strip():
                # Fin de una sub-tabla interna → parsear item
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
    """
    Parsea el valor de Job, que puede ser:
    - 0 (número)
    - {"medicoAR", "medicoBW"} (tabla de strings)
    """
    value = value.strip()
    if value.startswith('{'):
        # Tabla de strings
        return value
    try:
        return int(value)
    except ValueError:
        return value


def parse_crafting_blocks(lua_content: str) -> list:
    """
    Parsea un archivo de config Lua y extrae todos los bloques de crafteo
    como diccionarios Python.
    
    Args:
        lua_content: Contenido del archivo .lua
    
    Returns:
        list de dicts, cada uno representando un crafteo con sus campos
    """
    crafteos = []
    
    if not lua_content:
        return crafteos
    
    # Encontrar el inicio del array principal: Config.Xxx = {
    # y extraer todo hasta el cierre correspondiente
    header_match = re.match(r'Config\.\w+\s*=\s*\{', lua_content)
    if not header_match:
        return crafteos
    
    # Extraer bloques de crafteo individuales
    # Cada bloque empieza con { y contiene TakeItems, Text, etc.
    # Usamos posición-based parsing para manejar tablas anidadas
    content_start = header_match.end()
    
    # Buscar todos los bloques de nivel 1 (crafteos individuales)
    depth = 0
    block_start = None
    i = content_start
    
    while i < len(lua_content):
        char = lua_content[i]
        
        # Saltar comentarios de línea
        if lua_content[i:i+2] == '--':
            # Verificar si es un bloque comentado (contiene TakeItems)
            line_end = lua_content.find('\n', i)
            if line_end == -1:
                break
            # Si estamos fuera de un bloque de crafteo, saltar la línea
            if depth == 0:
                i = line_end + 1
                continue
            else:
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
                # Solo parsear si parece un bloque de crafteo (tiene Text =)
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
    """
    Parsea un bloque individual de crafteo Lua y lo convierte a dict.
    
    Args:
        block: Texto del bloque Lua (incluyendo llaves externas)
    
    Returns:
        dict con los campos del crafteo
    """
    crafteo = {}
    
    # Extraer campos simples: Key = value
    # TakeItems (bool)
    m = re.search(r'TakeItems\s*=\s*(true|false)', block)
    if m:
        crafteo['take_items'] = m.group(1) == 'true'
    
    # CurrencyType (int)
    m = re.search(r'CurrencyType\s*=\s*(\d+)', block)
    if m:
        crafteo['currency_type'] = int(m.group(1))
    
    # Location (int)
    m = re.search(r'Location\s*=\s*(\d+)', block)
    if m:
        crafteo['location'] = int(m.group(1))
    
    # Animation (string)
    m = re.search(r'Animation\s*=\s*"([^"]*)"', block)
    if m:
        crafteo['animation'] = m.group(1)
    
    # Category (string)
    m = re.search(r'Category\s*=\s*"([^"]*)"', block)
    if m:
        crafteo['categoria'] = m.group(1)
    
    # Text (string) - nombre del crafteo
    m = re.search(r'Text\s*=\s*"([^"]*)"', block)
    if m:
        crafteo['nombre'] = m.group(1)
    
    # Desc (string)
    m = re.search(r'Desc\s*=\s*"([^"]*)"', block)
    if m:
        crafteo['descripcion'] = m.group(1)
    
    # Minlvl (int)
    m = re.search(r'Minlvl\s*=\s*(\d+)', block)
    if m:
        crafteo['nivel_minimo'] = int(m.group(1))
    
    # UseCurrencyMode (bool)
    m = re.search(r'UseCurrencyMode\s*=\s*(true|false)', block)
    if m:
        crafteo['use_currency'] = m.group(1) == 'true'
    
    # Type (string)
    m = re.search(r'Type\s*=\s*"([^"]*)"', block)
    if m:
        crafteo['tipo'] = m.group(1)
    
    # Ilegal (bool, opcional)
    m = re.search(r'Ilegal\s*=\s*(true|false)', block)
    if m:
        crafteo['ilegal'] = m.group(1) == 'true'
    
    # Pack (string, opcional)
    m = re.search(r'Pack\s*=\s*"([^"]*)"', block)
    if m:
        crafteo['pack'] = m.group(1)
    
    # Job - puede ser número o tabla
    m = re.search(r'Job\s*=\s*(\{[^}]*\}|\d+)', block)
    if m:
        crafteo['job'] = _parse_lua_job(m.group(1))
    
    # Reward - extraer la tabla completa
    reward_match = re.search(r'Reward\s*=\s*(\{.+?\}(?:\s*\})?)', block, re.DOTALL)
    if reward_match:
        # Necesitamos encontrar el bloque completo de Reward
        reward_start = block.index('Reward')
        # Encontrar el inicio de la tabla
        eq_pos = block.index('=', reward_start)
        brace_start = block.index('{', eq_pos)
        
        # Contar llaves para encontrar el cierre
        depth = 0
        reward_end = brace_start
        for idx in range(brace_start, len(block)):
            if block[idx] == '{':
                depth += 1
            elif block[idx] == '}':
                depth -= 1
                if depth == 0:
                    reward_end = idx + 1
                    break
        
        reward_block = block[brace_start:reward_end]
        crafteo['recompensas'] = _parse_lua_table_items(reward_block)
    
    # Items - extraer la tabla completa
    items_start_search = re.search(r'\bItems\s*=\s*\{', block)
    if items_start_search:
        brace_start = items_start_search.end() - 1
        depth = 0
        items_end = brace_start
        for idx in range(brace_start, len(block)):
            if block[idx] == '{':
                depth += 1
            elif block[idx] == '}':
                depth -= 1
                if depth == 0:
                    items_end = idx + 1
                    break
        
        items_block = block[brace_start:items_end]
        crafteo['ingredientes'] = _parse_lua_table_items(items_block)
    
    return crafteo


def replace_crafting_in_config(job_key: str, old_craft_name: str, new_crafting_block: str) -> str:
    """
    Reemplaza un bloque de crafteo existente en el archivo de configuración.
    
    Args:
        job_key: Clave del job (ej: 'armero')
        old_craft_name: Nombre (Text) del crafteo a reemplazar
        new_crafting_block: Nuevo bloque de código Lua
    
    Returns:
        str: Contenido completo del archivo con el crafteo reemplazado,
             o None si no se encontró el crafteo
    """
    content = get_config_file_content(job_key)
    if not content:
        return None
    
    crafteos = parse_crafting_blocks(content)
    
    # Buscar el crafteo por nombre
    target = None
    for c in crafteos:
        if c.get('nombre') == old_craft_name:
            target = c
            break
    
    if not target:
        return None
    
    # Reemplazar el bloque viejo por el nuevo
    start = target['_start_pos']
    end = target['_end_pos']
    
    new_content = content[:start] + new_crafting_block + content[end:]
    return new_content


def delete_crafting_from_config(job_key: str, craft_name: str) -> str:
    """
    Elimina un bloque de crafteo del archivo de configuración.
    
    Args:
        job_key: Clave del job
        craft_name: Nombre (Text) del crafteo a eliminar
    
    Returns:
        str: Contenido completo del archivo sin el crafteo,
             o None si no se encontró
    """
    content = get_config_file_content(job_key)
    if not content:
        return None
    
    crafteos = parse_crafting_blocks(content)
    
    target = None
    for c in crafteos:
        if c.get('nombre') == craft_name:
            target = c
            break
    
    if not target:
        return None
    
    start = target['_start_pos']
    end = target['_end_pos']
    
    # Eliminar el bloque y la coma/espacios sobrantes
    before = content[:start].rstrip()
    after = content[end:].lstrip()
    
    # Limpiar coma sobrante
    if before.endswith(','):
        before = before[:-1]
    if after.startswith(','):
        after = after[1:].lstrip()
    
    new_content = before + "\n" + after
    return new_content
