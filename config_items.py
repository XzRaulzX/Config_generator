"""
Configuración de datos para el generador de crafteos RedM
Items, jobs, categorías, animaciones y packs para VORP Crafting System
"""
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent
DATA_PATH = BASE_DIR / "data"


def load_all_items():
    """Carga todos los items del archivo items.json"""
    items_file = DATA_PATH / "items.json"
    try:
        with open(items_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return {item['item']: item['label'] for item in data.get('items', [])}
    except Exception as e:
        print(f"Error cargando items.json: {e}")
        return {}


ALL_ITEMS = load_all_items()

# ============================================================================
# JOBS BASE - Metadatos de oficios conocidos
# Se extiende dinámicamente con configs descubiertas en Drive
# ============================================================================
BASE_JOBS = {
    'agricultor': {'nombre': '🌾 Agricultor', 'category': 'agricultor', 'job_value': 0},
    'armero': {'nombre': '🔫 Armero', 'category': 'Armero', 'job_value': 0},
    'artesano': {'nombre': '🎨 Artesano', 'category': 'Artesano', 'job_value': 0},
    'bandas': {'nombre': '💀 Bandas', 'category': 'MesaHerreroBanda', 'job_value': 0},
    'cocinaDulce': {'nombre': '🍰 Cocina Dulce', 'category': 'CocinaDulce', 'job_value': 0},
    'cocinaMixta': {'nombre': '🍲 Cocina Mixta', 'category': 'CocinaMixta', 'job_value': 0},
    'cocinaPacks': {'nombre': '📦 Cocina Packs', 'category': 'CocinaPacks', 'job_value': 0},
    'cocinaTier1': {'nombre': '🍳 Cocina Tier 1', 'category': 'CocinaTier1', 'job_value': 0},
    'cocinaTier2': {'nombre': '👨‍🍳 Cocina Tier 2', 'category': 'CocinaTier2', 'job_value': 0},
    'cocinaTier3': {'nombre': '👩‍🍳 Cocina Tier 3', 'category': 'CocinaTier3', 'job_value': 0},
    'destilador': {'nombre': '🥃 Destilador', 'category': 'Destilador', 'job_value': 0},
    'distribuidora': {'nombre': '🚚 Distribuidora', 'category': 'Distribuidora', 'job_value': 0},
    'establo': {'nombre': '🐴 Establo', 'category': 'Establo', 'job_value': 0},
    'ganadero': {'nombre': '🐄 Ganadero', 'category': 'Ganadero', 'job_value': 0},
    'medicos': {'nombre': '⚕️ Médicos', 'category': 'Medico', 'job_value': '{"medicoAR", "medicoBW", "medicoMF"}'},
    'perista': {'nombre': '💰 Perista', 'category': 'Perista', 'job_value': 0},
    'pescadero': {'nombre': '🎣 Pescadero', 'category': 'Pescadero', 'job_value': 0},
    'tabacalero': {'nombre': '🚬 Tabacalero', 'category': 'Tabacalero', 'job_value': 0},
}


def get_job_metadata(key):
    """Obtiene metadatos de un job. Genera valores por defecto si no es un job conocido."""
    if key in BASE_JOBS:
        return BASE_JOBS[key]
    config_name = key[0].upper() + key[1:] if key else key
    return {
        'nombre': f'📄 {key.replace("_", " ").title()}',
        'category': config_name,
        'job_value': 0,
    }


def get_job_display_name(key):
    """Nombre legible para un job."""
    return get_job_metadata(key)['nombre']


# ============================================================================
# TIPOS DE CRAFTEO
# ============================================================================
TIPOS_CRAFTEO = {
    'item': 'Item Normal',
    'weapon': 'Arma',
}

# ============================================================================
# ANIMACIONES DISPONIBLES (sincronizadas con Config.Animations)
# ============================================================================
ANIMACIONES = {
    'craft': '🛠️ Crafteo genérico',
    'CocinaTier3': '🧂 Cocina avanzada (salero)',
    'spindlecook': '🍖 Asar en pincho',
    'knifecooking': '🔪 Cocinar con cuchillo',
    'campfire': '🔥 Encender fogata',
}

# ============================================================================
# CATEGORÍAS DE CRAFTEO (sincronizadas con Config.Categories del servidor)
# ============================================================================
CATEGORIAS_CRAFTEO = {
    'food': '🍔 Comida',
    'items': '📦 Items',
    'weapons': '🔫 Armas',
    'meleeweapons': '🗡️ Armas cuerpo a cuerpo',
    'cocina': '🍳 Cocina',
    'empty': '📝 Elaboraciones',
    'CocinaTier1': '🍳 Cocina Tier 1',
    'CocinaTier2': '👨‍🍳 Cocina Tier 2',
    'CocinaTier3': '👩‍🍳 Cocina Tier 3',
    'CocinaDulce': '🍰 Cocina Dulce',
    'CocinaMixta': '🍲 Cocina Mixta',
    'CocinaPacks': '🍽️ Cocina Packs',
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
    'MesaHerreroBanda': '🛠️ Mesa Herrero (Banda)',
    'MesaEnfermeriaBanda': '🩺 Mesa Enfermería (Banda)',
}

# ============================================================================
# PACKS PREDEFINIDOS
# ============================================================================
PACKS_PREDEFINIDOS = [
    "", "comun", "mejicana", "afroamericana", "oriental",
    "inglesa", "nativo", "campero",
]
