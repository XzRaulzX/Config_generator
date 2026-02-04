"""
Generador de bloques de código Lua para VORP Crafting
"""

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
    Reward = {{{{
        name = "{data['recompensa']}",
        count = {data['cantidad_recompensa']}
    }}}},
    Minlvl = {data.get('nivel_minimo', 0)},
    UseCurrencyMode = {str(data.get('use_currency', False)).lower()},
    Job = {job_str},
    Type = "{data.get('tipo', 'item')}",
    Items = {items_block}
}},"""
    
    return lua_code
