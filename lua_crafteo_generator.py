"""
Generador de bloques de código Lua para VORP Crafting
"""
import os
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
        take_str = ",\n        take = true" if data.get('take_items', True) else ""
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
    
    # Generar el bloque de crafteo
    lua_code = f"""{{
    TakeItems = {str(data.get('take_items', True)).lower()},
    CurrencyType = {data.get('currency_type', 0)},
    Location = {data.get('location', 0)},
    Animation = "{data.get('animation', 'craft')}",
    Category = "{data['categoria']}",
    Text = "{data['nombre']}",
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
