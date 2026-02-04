"""
Configuración de datos para el generador de crafteos RedM
Contiene todos los jobs, items de recompensa e ingredientes organizados por categoría
"""
import os
import json
from pathlib import Path

# ============================================================================
# PATH DE CONFIGURACIONES (relativo para Streamlit Cloud)
# ============================================================================
# Obtener el directorio del script actual
BASE_DIR = Path(__file__).parent
CONFIG_PATH = BASE_DIR / "configs"
DATA_PATH = BASE_DIR / "data"

# ============================================================================
# CARGAR TODOS LOS ITEMS DESDE items.json
# ============================================================================
def load_all_items():
    """Carga todos los items del archivo items.json y los convierte en diccionario"""
    items_file = DATA_PATH / "items.json"
    try:
        with open(items_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Crear diccionario {item_id: label}
            return {item['item']: item['label'] for item in data.get('items', [])}
    except Exception as e:
        print(f"Error cargando items.json: {e}")
        return {}

# Cargar todos los items al iniciar
ALL_ITEMS = load_all_items()

# ============================================================================
# JOBS/CATEGORÍAS DISPONIBLES
# ============================================================================
# Los 'category' deben coincidir con los ident de Config.Categories en config.lua
JOBS = {
    'agricultor': {
        'nombre': '🌾 Agricultor',
        'category': 'agricultor',  # Coincide con config.lua
        'job_value': 0,  # 0 = cualquiera puede craftear
    },
    'armero': {
        'nombre': '🔫 Armero',
        'category': 'Armero',  # Coincide con config.lua (mayúscula)
        'job_value': 0,
    },
    'artesano': {
        'nombre': '🎨 Artesano',
        'category': 'Artesano',  # Corregido: mayúscula en config.lua
        'job_value': 0,
    },
    'bandas': {
        'nombre': '💀 Bandas',
        'category': 'MesaHerreroBanda',  # Usa Mesa Herrero de banda
        'job_value': 0,
    },
    'cocinaDulce': {
        'nombre': '🍰 Cocina Dulce',
        'category': 'CocinaDulce',  # Corregido: CamelCase en config.lua
        'job_value': 0,
    },
    'cocinaMixta': {
        'nombre': '🍲 Cocina Mixta',
        'category': 'CocinaMixta',  # Corregido: CamelCase en config.lua
        'job_value': 0,
    },
    'cocinaPacks': {
        'nombre': '📦 Cocina Packs',
        'category': 'CocinaPacks',  # Corregido: CamelCase en config.lua
        'job_value': 0,
    },
    'cocinaTier1': {
        'nombre': '🍳 Cocina Tier 1',
        'category': 'CocinaTier1',  # Corregido: CamelCase en config.lua
        'job_value': 0,
    },
    'cocinaTier2': {
        'nombre': '👨‍🍳 Cocina Tier 2',
        'category': 'CocinaTier2',  # Corregido: CamelCase en config.lua
        'job_value': 0,
    },
    'cocinaTier3': {
        'nombre': '👩‍🍳 Cocina Tier 3',
        'category': 'CocinaTier3',  # Corregido: CamelCase en config.lua
        'job_value': 0,
    },
    'destilador': {
        'nombre': '🥃 Destilador',
        'category': 'Destilador',  # Coincide con config.lua
        'job_value': 0,
    },
    'distribuidora': {
        'nombre': '🚚 Distribuidora',
        'category': 'Distribuidora',  # Corregido: mayúscula en config.lua
        'job_value': 0,
    },
    'establo': {
        'nombre': '🐴 Establo',
        'category': 'Establo',  # Coincide con config.lua
        'job_value': 0,
    },
    'ganadero': {
        'nombre': '🐄 Ganadero',
        'category': 'Ganadero',  # Corregido: mayúscula en config.lua
        'job_value': 0,
    },
    'medicos': {
        'nombre': '⚕️ Médicos',
        'category': 'Medico',  # Coincide con config.lua
        'job_value': '{"medicoAR", "medicoBW", "medicoMF"}',
    },
    'perista': {
        'nombre': '💰 Perista',
        'category': 'Perista',  # Corregido: mayúscula en config.lua
        'job_value': 0,
    },
    'pescadero': {
        'nombre': '🎣 Pescadero',
        'category': 'Pescadero',  # Corregido: mayúscula en config.lua
        'job_value': 0,
    },
    'tabacalero': {
        'nombre': '🚬 Tabacalero',
        'category': 'Tabacalero',  # Corregido: mayúscula en config.lua
        'job_value': 0,
    },
}

# ============================================================================
# TIPOS DE CRAFTEO
# ============================================================================
TIPOS_CRAFTEO = {
    'item': 'Item Normal',
    'weapon': 'Arma',
}

# ============================================================================
# ITEMS DE RECOMPENSA - TODOS LOS ITEMS PARA TODAS LAS CATEGORÍAS
# ============================================================================
# Ahora todos los jobs tienen acceso a todos los items del JSON
def get_items_recompensa():
    """Genera el diccionario de items de recompensa con todos los items para cada job"""
    jobs_list = [
        'agricultor', 'armero', 'artesano', 'bandas', 
        'cocinaDulce', 'cocinaMixta', 'cocinaPacks', 
        'cocinaTier1', 'cocinaTier2', 'cocinaTier3',
        'destilador', 'distribuidora', 'establo', 
        'ganadero', 'medicos', 'perista', 'pescadero', 'tabacalero'
    ]
    return {job: ALL_ITEMS.copy() for job in jobs_list}

ITEMS_RECOMPENSA = get_items_recompensa()

# ============================================================================
# ITEMS INGREDIENTES - TODOS LOS ITEMS PARA TODAS LAS CATEGORÍAS
# ============================================================================
def get_items_ingredientes():
    """Genera el diccionario de ingredientes con todos los items para cada job"""
    jobs_list = [
        'comunes', 'agricultor', 'armero', 'artesano', 'bandas', 
        'cocinaDulce', 'cocinaMixta', 'cocinaPacks', 
        'cocinaTier1', 'cocinaTier2', 'cocinaTier3',
        'destilador', 'distribuidora', 'establo', 
        'ganadero', 'medicos', 'perista', 'pescadero', 'tabacalero'
    ]
    return {job: ALL_ITEMS.copy() for job in jobs_list}

ITEMS_INGREDIENTES = get_items_ingredientes()

# ============================================================================
# ANIMACIONES DISPONIBLES (sincronizadas con Config.Animations del servidor)
# ============================================================================
ANIMACIONES = {
    'craft': '🛠️ Crafteo genérico (por defecto)',
    'CocinaTier3': '🧂 Cocina avanzada (con salero)',
    'spindlecook': '🍖 Asar en pincho (carne en palo)',
    'knifecooking': '🔪 Cocinar con cuchillo',
    'campfire': '🔥 Encender fogata',
}

# ============================================================================
# CATEGORÍAS DE CRAFTEO DISPONIBLES (sincronizadas con Config.Categories)
# ============================================================================
# Los ident deben coincidir EXACTAMENTE con los del config.lua del servidor
CATEGORIAS_CRAFTEO = {
    # Categorías generales
    'food': '🍔 Comida (general)',
    'items': '📦 Items (general)',
    'weapons': '🔫 Armas',
    'meleeweapons': '🗡️ Armas cuerpo a cuerpo',
    'cocina': '🍳 Cocina (general)',
    'empty': '📝 Elaboraciones (vacío)',
    # Cocina por tiers
    'CocinaTier1': '🍳 Cocina Tier 1 (básica)',
    'CocinaTier2': '👨‍🍳 Cocina Tier 2 (media)',
    'CocinaTier3': '👩‍🍳 Cocina Tier 3 (avanzada)',
    'CocinaDulce': '🍰 Cocina Dulce',
    'CocinaMixta': '🍲 Cocina Mixta',
    'CocinaPacks': '🍽️ Cocina Packs (especialidades)',
    # Oficios
    'agricultor': '🌾 Agricultor',
    'Ganadero': '🐄 Ganadero',
    'Pescadero': '🎣 Pescadero',
    'Tabacalero': '🚬 Tabacalero',
    'Destilador': '🥃 Destilador',
    'Distribuidora': '🚚 Distribuidora',
    'Artesano': '🎨 Artesano',
    'Armero': '🔫 Armero',
    'Establo': '🐴 Establo',
    'Perista': '💎 Perista',
    'Medico': '⚕️ Médico',
    # Bandas
    'MesaHerreroBanda': '🛠️ Mesa Herrero (Banda)',
    'MesaEnfermeriaBanda': '🩺 Mesa Enfermería (Banda)',
}
