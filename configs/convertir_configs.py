import re
import os
import sys
from pathlib import Path

def parse_lua_config(file_path):
    """
    Parsea un archivo de configuración Lua de VORP Crafting y extrae las recetas
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Buscar la configuración principal (Config.NombreCategoria)
    config_match = re.search(r'Config\.(\w+)\s*=\s*{', content)
    if not config_match:
        print(f"No se pudo encontrar la configuración en {file_path}")
        return []
    
    category_name = config_match.group(1)
    
    # Extraer el contenido completo de la configuración
    config_start = content.find('Config.' + category_name + ' = {')
    if config_start == -1:
        print(f"No se pudo encontrar el inicio de la configuración en {file_path}")
        return []
    
    # Buscar el final de la configuración (antes del comentario final)
    config_content = content[config_start:]
    
    # Extraer todas las recetas usando un enfoque simple y directo
    recipes = []
    
    # Buscar todas las ocurrencias de {{ ... }} que contengan Text =
    recipe_blocks = []
    
    # Encontrar todas las posiciones donde empieza una receta
    start_positions = []
    pos = 0
    while True:
        start_pos = config_content.find('{', pos)
        if start_pos == -1:
            break
        # Verificar que es el inicio de una receta (debe contener Text =)
        # Buscar hasta el siguiente } para verificar si contiene Text =
        end_pos = config_content.find('}', start_pos)
        if end_pos != -1:
            potential_recipe = config_content[start_pos:end_pos + 1]
            if 'Text =' in potential_recipe:
                start_positions.append(start_pos)
        pos = start_pos + 1
    
    print(f"Encontrados {len(start_positions)} inicios de recetas")
    
    # Para cada inicio, encontrar el final correspondiente
    for start_pos in start_positions:
        # Contar llaves para encontrar el final
        brace_count = 0
        found_end = False
        
        # Buscar desde la posición actual hasta el final del contenido
        for i, char in enumerate(config_content[start_pos:]):
            if char == '{':
                brace_count += 1
            elif char == '}':
                brace_count -= 1
                if brace_count == 0:
                    # Encontramos el final de la receta
                    recipe_block = config_content[start_pos:start_pos + i + 1]
                    if 'Text =' in recipe_block:  # Verificar que es una receta válida
                        recipe_blocks.append(recipe_block)
                        print(f"Receta válida encontrada en posición {start_pos}")
                    found_end = True
                    break
        
        if not found_end:
            print(f"Advertencia: No se encontró el final para la receta en posición {start_pos}")
    
    print(f"Encontrados {len(recipe_blocks)} bloques de recetas válidas")
    
    for recipe_block in recipe_blocks:
        recipe = parse_recipe(recipe_block, category_name)
        if recipe and recipe['Nombre']:  # Solo incluir recetas con nombre
            recipes.append(recipe)
    
    return recipes

def parse_recipe(recipe_text, category_name):
    """
    Parsea una receta individual y extrae sus propiedades
    """
    recipe = {
        'Categoria': category_name,
        'Nombre': '',
        'Descripcion': '',
        'Tipo': '',
        'Recompensa': '',
        'Cantidad_Recompensa': '',
        'Nivel_Minimo': '',
        'Ingredientes': []
    }
    
    # Extraer Text (nombre de la receta)
    text_match = re.search(r'Text\s*=\s*"([^"]+)"', recipe_text)
    if text_match:
        recipe['Nombre'] = text_match.group(1)
    
    # Extraer Desc (descripción)
    desc_match = re.search(r'Desc\s*=\s*"([^"]+)"', recipe_text)
    if desc_match:
        recipe['Descripcion'] = desc_match.group(1)
    
    # Extraer Type
    type_match = re.search(r'Type\s*=\s*"([^"]+)"', recipe_text)
    if type_match:
        recipe['Tipo'] = type_match.group(1)
    
    # Extraer Minlvl
    minlvl_match = re.search(r'Minlvl\s*=\s*(\d+)', recipe_text)
    if minlvl_match:
        recipe['Nivel_Minimo'] = minlvl_match.group(1)
    
    # Extraer Reward
    reward_match = re.search(r'Reward\s*=\s*{([^}]+)}', recipe_text, re.DOTALL)
    if reward_match:
        reward_text = reward_match.group(1)
        name_match = re.search(r'name\s*=\s*"([^"]+)"', reward_text)
        count_match = re.search(r'count\s*=\s*(\d+)', reward_text)
        
        if name_match:
            recipe['Recompensa'] = name_match.group(1)
        if count_match:
            recipe['Cantidad_Recompensa'] = count_match.group(1)
    
    # Extraer Items (ingredientes)
    items_match = re.search(r'Items\s*=\s*{([^}]+)}', recipe_text, re.DOTALL)
    if items_match:
        items_text = items_match.group(1)
        # Buscar todos los items individuales
        item_pattern = r'{([^}]+)}'
        item_matches = re.findall(item_pattern, items_text, re.DOTALL)
        
        for item_text in item_matches:
            name_match = re.search(r'name\s*=\s*"([^"]+)"', item_text)
            count_match = re.search(r'count\s*=\s*(\d+)', item_text)
            
            if name_match and count_match:
                recipe['Ingredientes'].append({
                    'nombre': name_match.group(1),
                    'cantidad': count_match.group(1)
                })
    
    return recipe

def recipes_to_csv(recipes, output_file):
    """
    Convierte las recetas a formato CSV
    """
    if not recipes:
        print("No hay recetas para convertir")
        return
    
    with open(output_file, 'w', encoding='utf-8', newline='') as file:
        # Escribir encabezados
        headers = ['Categoria', 'Nombre', 'Descripcion', 'Tipo', 'Recompensa', 
                  'Cantidad_Recompensa', 'Nivel_Minimo', 'Ingredientes']
        file.write(';'.join(headers) + '\n')
        
        # Escribir cada receta
        for recipe in recipes:
            # Formatear ingredientes como "item:cantidad,item:cantidad"
            ingredientes_str = ','.join([f"{item['nombre']}:{item['cantidad']}" 
                                       for item in recipe['Ingredientes']])
            
            # Crear línea CSV
            line = [
                recipe['Categoria'],
                recipe['Nombre'],
                recipe['Descripcion'],
                recipe['Tipo'],
                recipe['Recompensa'],
                recipe['Cantidad_Recompensa'],
                recipe['Nivel_Minimo'],
                ingredientes_str
            ]
            
            # Escapar comillas si es necesario
            line = [f'"{field}"' if ';' in str(field) else str(field) for field in line]
            file.write(';'.join(line) + '\n')

def process_config_file(file_path):
    """
    Procesa un archivo de configuración y genera el CSV
    """
    print(f"Procesando: {file_path}")
    
    # Parsear el archivo
    recipes = parse_lua_config(file_path)
    
    if not recipes:
        print(f"No se encontraron recetas en {file_path}")
        return
    
    # Generar nombre del archivo de salida
    file_name = Path(file_path).stem
    output_file = f"{file_name}_recetas.csv"
    
    # Convertir a CSV
    recipes_to_csv(recipes, output_file)
    
    print(f"Se encontraron {len(recipes)} recetas")
    print(f"Archivo CSV generado: {output_file}")
    print("-" * 50)

def main():
    """
    Función principal que procesa todos los archivos de configuración
    """
    # Obtener la ruta del script actual
    script_dir = Path(__file__).parent
    
    # Buscar la carpeta config en diferentes ubicaciones relativas
    possible_config_paths = [
        script_dir / "config",  # Mismo directorio que el script
        script_dir / ".." / "config",  # Un nivel arriba
        script_dir / ".." / ".." / "config",  # Dos niveles arriba
        script_dir / "vorp_crafting" / "config",  # Subdirectorio vorp_crafting
        script_dir / ".." / "vorp_crafting" / "config",  # Un nivel arriba + vorp_crafting
    ]
    
    config_dir = None
    for path in possible_config_paths:
        if path.exists():
            config_dir = path
            break
    
    if not config_dir:
        print("Error: No se encontró el directorio 'config'")
        print("Buscando en las siguientes rutas:")
        for path in possible_config_paths:
            print(f"  - {path.absolute()}")
        print("\nAsegúrate de que el script esté en la ubicación correcta")
        return
    
    print(f"Directorio de configuración encontrado: {config_dir.absolute()}")
    
    # Buscar todos los archivos config_*.lua
    config_files = list(config_dir.glob("config_*.lua"))
    
    if not config_files:
        print("No se encontraron archivos de configuración (config_*.lua)")
        return
    
    print(f"Se encontraron {len(config_files)} archivos de configuración")
    print("=" * 50)
    
    # Procesar cada archivo
    for config_file in config_files:
        try:
            process_config_file(config_file)
        except Exception as e:
            print(f"Error procesando {config_file}: {e}")
            continue
    
    print("Procesamiento completado!")

if __name__ == "__main__":
    main()