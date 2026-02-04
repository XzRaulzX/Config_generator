"""
Configuración de datos para el generador de crafteos RedM
Contiene todos los jobs, items de recompensa e ingredientes organizados por categoría
"""
import os
from pathlib import Path

# ============================================================================
# PATH DE CONFIGURACIONES (relativo para Streamlit Cloud)
# ============================================================================
# Obtener el directorio del script actual
BASE_DIR = Path(__file__).parent
CONFIG_PATH = BASE_DIR / "configs"

# ============================================================================
# JOBS/CATEGORÍAS DISPONIBLES
# ============================================================================
JOBS = {
    'agricultor': {
        'nombre': '🌾 Agricultor',
        'category': 'agricultor',
        'job_value': 0,  # 0 = cualquiera puede craftear
    },
    'armero': {
        'nombre': '🔫 Armero',
        'category': 'Armero',
        'job_value': 0,
    },
    'artesano': {
        'nombre': '🎨 Artesano',
        'category': 'artesano',
        'job_value': 0,
    },
    'bandas': {
        'nombre': '💀 Bandas',
        'category': 'bandas',
        'job_value': 0,
    },
    'cocinaDulce': {
        'nombre': '🍰 Cocina Dulce',
        'category': 'cocinaDulce',
        'job_value': 0,
    },
    'cocinaMixta': {
        'nombre': '🍲 Cocina Mixta',
        'category': 'cocinaMixta',
        'job_value': 0,
    },
    'cocinaPacks': {
        'nombre': '📦 Cocina Packs',
        'category': 'cocinaPacks',
        'job_value': 0,
    },
    'cocinaTier1': {
        'nombre': '🍳 Cocina Tier 1',
        'category': 'cocinaTier1',
        'job_value': 0,
    },
    'cocinaTier2': {
        'nombre': '👨‍🍳 Cocina Tier 2',
        'category': 'cocinaTier2',
        'job_value': 0,
    },
    'cocinaTier3': {
        'nombre': '👩‍🍳 Cocina Tier 3',
        'category': 'cocinaTier3',
        'job_value': 0,
    },
    'destilador': {
        'nombre': '🥃 Destilador',
        'category': 'Destilador',
        'job_value': 0,
    },
    'distribuidora': {
        'nombre': '🚚 Distribuidora',
        'category': 'distribuidora',
        'job_value': 0,
    },
    'establo': {
        'nombre': '🐴 Establo',
        'category': 'Establo',
        'job_value': 0,
    },
    'ganadero': {
        'nombre': '🐄 Ganadero',
        'category': 'ganadero',
        'job_value': 0,
    },
    'medicos': {
        'nombre': '⚕️ Médicos',
        'category': 'Medico',
        'job_value': '{"medicoAR", "medicoBW", "medicoMF"}',
    },
    'perista': {
        'nombre': '💰 Perista',
        'category': 'perista',
        'job_value': 0,
    },
    'pescadero': {
        'nombre': '🎣 Pescadero',
        'category': 'pescadero',
        'job_value': 0,
    },
    'tabacalero': {
        'nombre': '🚬 Tabacalero',
        'category': 'tabacalero',
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
# ITEMS DE RECOMPENSA POR CATEGORÍA
# ============================================================================
ITEMS_RECOMPENSA = {
    'agricultor': {
        'consumable_haycube': 'Cubito de heno',
        'harina_maiz': 'Harina de maíz',
        'cafe_molido': 'Café molido',
        'harina': 'Harina',
        'trigo': 'Trigo',
        'corn': 'Maíz',
        'cotton': 'Algodón',
        'fibers': 'Fibra',
    },
    'armero': {
        # Municiones
        'cleanshort': 'Aceite para armas',
        'ammoshotgunnormal': 'Munición de escopeta',
        'ammopistolnormal': 'Munición de pistola',
        'ammorevolvernormal': 'Munición de revolver',
        'ammorepeaternormal': 'Munición de fusil de repetición',
        'ammoriflenormal': 'Munición de rifle',
        'ammovarmint': 'Munición del 22',
        # Armas
        'weapon_revolver_cattleman': 'Revólver Cattleman',
        'weapon_revolver_doubleaction': 'Revólver Doble Acción',
        'weapon_revolver_schofield': 'Revólver Schofield',
        'weapon_revolver_navy': 'Revólver Navy',
        'weapon_pistol_volcanic': 'Pistola Volcanic',
        'weapon_pistol_mauser': 'Pistola Mauser',
        'weapon_pistol_semiauto': 'Pistola Semiautomática',
        'weapon_shotgun_doublebarrel': 'Escopeta Doble Cañón',
        'weapon_shotgun_pump': 'Escopeta de Bombeo',
        'weapon_shotgun_repeating': 'Escopeta Repetidora',
        'weapon_shotgun_sawedoff': 'Escopeta Recortada',
        'weapon_rifle_varmint': 'Rifle del 22',
        'weapon_rifle_springfield': 'Rifle Springfield',
        'weapon_rifle_boltaction': 'Rifle de Cerrojo',
        'weapon_rifle_carcano': 'Rifle Carcano',
        'weapon_repeater_carbine': 'Carabina Repetidora',
        'weapon_repeater_winchester': 'Winchester',
        'weapon_repeater_henry': 'Rifle Henry',
        'weapon_repeater_evans': 'Rifle Evans',
        'weapon_bow': 'Arco',
        'weapon_lasso': 'Lazo',
        'weapon_melee_knife': 'Cuchillo',
        'weapon_melee_machete': 'Machete',
        'weapon_melee_cleaver': 'Cuchilla de Carnicero',
        'weapon_melee_hatchet': 'Hacha',
        'weapon_thrown_dynamite': 'Dinamita',
        'weapon_thrown_molotov': 'Molotov',
    },
    'artesano': {
        'cuerda': 'Cuerda',
        'silla_caballo': 'Silla de caballo',
        'herradura': 'Herradura',
        'bolsa_cuero': 'Bolsa de cuero',
        'montura': 'Montura',
        'riendas': 'Riendas',
    },
    'bandas': {
        # Items
        'dinamita': 'Dinamita',
        'molotov': 'Molotov',
        'lockpick': 'Ganzúa',
        'mascara': 'Máscara',
        # Armas
        'weapon_revolver_cattleman': 'Revólver Cattleman',
        'weapon_revolver_doubleaction': 'Revólver Doble Acción',
        'weapon_revolver_schofield': 'Revólver Schofield',
        'weapon_revolver_navy': 'Revólver Navy',
        'weapon_pistol_volcanic': 'Pistola Volcanic',
        'weapon_pistol_mauser': 'Pistola Mauser',
        'weapon_pistol_semiauto': 'Pistola Semiautomática',
        'weapon_shotgun_doublebarrel': 'Escopeta Doble Cañón',
        'weapon_shotgun_sawedoff': 'Escopeta Recortada',
        'weapon_rifle_varmint': 'Rifle del 22',
        'weapon_repeater_carbine': 'Carabina Repetidora',
        'weapon_bow': 'Arco',
        'weapon_melee_knife': 'Cuchillo',
        'weapon_melee_machete': 'Machete',
        'weapon_melee_hatchet': 'Hacha',
        'weapon_thrown_dynamite': 'Dinamita (arrojadiza)',
        'weapon_thrown_molotov': 'Molotov (arrojadiza)',
    },
    'cocinaDulce': {
        'pastel': 'Pastel',
        'galletas': 'Galletas',
        'tarta': 'Tarta',
        'dulce': 'Dulce',
        'caramelo': 'Caramelo',
    },
    'cocinaMixta': {
        'estofado': 'Estofado',
        'guiso': 'Guiso',
        'sopa': 'Sopa',
        'caldo': 'Caldo',
    },
    'cocinaPacks': {
        'pack_comida': 'Pack de comida',
        'racion': 'Ración',
        'provisiones': 'Provisiones',
    },
    'cocinaTier1': {
        'pan': 'Pan',
        'tortilla': 'Tortilla',
        'huevos_fritos': 'Huevos fritos',
        'carne_asada': 'Carne asada',
    },
    'cocinaTier2': {
        'estofado': 'Estofado',
        'asado': 'Asado',
        'pastel_carne': 'Pastel de carne',
    },
    'cocinaTier3': {
        'banquete': 'Banquete',
        'plato_gourmet': 'Plato gourmet',
        'festin': 'Festín',
    },
    'destilador': {
        'moonshine': 'Aguardiente',
        'beer': 'Cerveza',
        'zarzaparrilla': 'Zarzaparrilla',
        'consumable_whiskey': 'Whiskey',
        'consumable_brandy': 'Brandy',
        'consumable_rum': 'Ron',
        'consumable_gin': 'Ginebra',
        'consumable_tequila': 'Tequila',
        'consumable_absinthe': 'Absenta',
        'vino_tinto': 'Vino tinto',
        'vino_blanco': 'Vino blanco',
    },
    'distribuidora': {
        'caja_madera': 'Caja de madera',
        'saco': 'Saco',
        'barril': 'Barril',
        'paquete': 'Paquete',
    },
    'establo': {
        'HorseTag': 'Documentación de caballo',
        'Horse_Shoe': 'Herraduras',
        'silla_montar_1': 'Caballete básico',
        'silla_montar_2': 'Caballete normal',
        'silla_montar_3': 'Caballete avanzado',
        'consumable_haycube': 'Cubito de heno',
        'horse_brush': 'Cepillo de caballo',
        'horse_food': 'Comida de caballo',
    },
    'ganadero': {
        'carne_cruda': 'Carne cruda',
        'cuero': 'Cuero',
        'leche': 'Leche',
        'lana': 'Lana',
        'huevos': 'Huevos',
        'grasa_animal': 'Grasa animal',
        'cuero_curtido': 'Cuero curtido',
    },
    'medicos': {
        'aguja_hilo': 'Aguja e hilo',
        'cataplasma_simple': 'Cataplasma simple',
        'extracto_menta': 'Extracto de menta',
        'venda_medica': 'Venda médica',
        'medicina': 'Medicina',
        'tonico_salud': 'Tónico de salud',
        'antidoto': 'Antídoto',
        'estimulante': 'Estimulante',
        'cura_heridas': 'Cura heridas',
        'analgesico': 'Analgésico',
    },
    'perista': {
        'joya_fundida': 'Joya fundida',
        'oro_lingote': 'Lingote de oro',
        'plata_lingote': 'Lingote de plata',
        'piedra_preciosa': 'Piedra preciosa',
    },
    'pescadero': {
        'pescado_cocinado': 'Pescado cocinado',
        'salmon_ahumado': 'Salmón ahumado',
        'caviar': 'Caviar',
        'aceite_pescado': 'Aceite de pescado',
        'filete_pescado': 'Filete de pescado',
    },
    'tabacalero': {
        'cigarro': 'Cigarro',
        'puro': 'Puro',
        'tabaco_premium': 'Tabaco premium',
        'cigarrillo': 'Cigarrillo',
        'tabaco_mascar': 'Tabaco de mascar',
    },
}

# ============================================================================
# ITEMS INGREDIENTES POR CATEGORÍA (filtrados por job relevante)
# ============================================================================
ITEMS_INGREDIENTES = {
    'comunes': {
        # Materiales básicos - disponibles para todos
        'iron': 'Lingote de hierro',
        'wood': 'Madera blanda',
        'hwood': 'Madera dura',
        'stick': 'Palo',
        'cobre': 'Cobre',
        'coal': 'Carbón',
        'fibers': 'Fibra',
        'trozotela': 'Trozo de tela',
        'leather': 'Cuero',
        'nota': 'Nota de papel',
        'pluma': 'Pluma',
        'botella': 'Botella vacía',
        'water': 'Agua',
    },
    'agricultor': {
        'trigo': 'Trigo',
        'corn': 'Maíz',
        'grano_cafe': 'Granos de Café',
        'semillas': 'Semillas',
        'sugar': 'Azúcar',
        'cotton': 'Algodón',
        'vegetales': 'Vegetales',
        'zanahoria': 'Zanahoria',
        'patata': 'Patata',
        'tomate': 'Tomate',
        'cebolla': 'Cebolla',
    },
    'armero': {
        'gunpowder': 'Pólvora',
        'carcasa_bala': 'Carcasa de bala',
        'plomo': 'Plomo',
        'acero': 'Acero',
        'fishoil': 'Aceite de pescado',
        'mecanismo_arma': 'Mecanismo de arma',
        'mango_madera': 'Mango de madera',
        'cañon_metal': 'Cañón de metal',
    },
    'artesano': {
        'cuero_curtido': 'Cuero curtido',
        'tela': 'Tela',
        'cuerda': 'Cuerda',
        'hilo': 'Hilo',
        'aguja': 'Aguja',
        'metal': 'Metal',
    },
    'bandas': {
        'gunpowder': 'Pólvora',
        'mecha': 'Mecha',
        'botella': 'Botella vacía',
        'alcohol': 'Alcohol',
        'tela': 'Tela',
        'alambre': 'Alambre',
    },
    'cocinaDulce': {
        'harina': 'Harina',
        'sugar': 'Azúcar',
        'huevos': 'Huevos',
        'leche': 'Leche',
        'mantequilla': 'Mantequilla',
        'chocolate': 'Chocolate',
        'frutas': 'Frutas',
    },
    'cocinaMixta': {
        'carne_cruda': 'Carne cruda',
        'vegetales': 'Vegetales',
        'patata': 'Patata',
        'zanahoria': 'Zanahoria',
        'cebolla': 'Cebolla',
        'sal': 'Sal',
        'pimienta': 'Pimienta',
        'water': 'Agua',
    },
    'cocinaPacks': {
        'pan': 'Pan',
        'carne_cocinada': 'Carne cocinada',
        'vegetales': 'Vegetales',
        'queso': 'Queso',
    },
    'cocinaTier1': {
        'harina': 'Harina',
        'huevos': 'Huevos',
        'carne_cruda': 'Carne cruda',
        'sal': 'Sal',
        'water': 'Agua',
    },
    'cocinaTier2': {
        'carne_cruda': 'Carne cruda',
        'vegetales': 'Vegetales',
        'especias': 'Especias',
        'vino': 'Vino',
        'caldo': 'Caldo',
    },
    'cocinaTier3': {
        'carne_premium': 'Carne premium',
        'especias_raras': 'Especias raras',
        'trufa': 'Trufa',
        'caviar': 'Caviar',
    },
    'destilador': {
        'trigo': 'Trigo',
        'sugar': 'Azúcar',
        'botella': 'Botella vacía',
        'water': 'Agua',
        'herb_black_current': 'Planta de casis',
        'levadura': 'Levadura',
        'uvas': 'Uvas',
        'manzana': 'Manzana',
        'agave': 'Agave',
    },
    'distribuidora': {
        'wood': 'Madera',
        'cuerda': 'Cuerda',
        'clavos': 'Clavos',
        'tela': 'Tela',
    },
    'establo': {
        'iron': 'Lingote de hierro',
        'wood': 'Madera blanda',
        'hwood': 'Madera dura',
        'stick': 'Palo',
        'cobre': 'Cobre',
        'cuero': 'Cuero',
        'nota': 'Nota de papel',
        'pluma': 'Pluma',
        'heno': 'Heno',
        'trigo': 'Trigo',
    },
    'ganadero': {
        'cuchillo': 'Cuchillo',
        'sal': 'Sal',
        'water': 'Agua',
        'heno': 'Heno',
    },
    'medicos': {
        'iron': 'Hierro',
        'fibers': 'Fibra',
        'trozotela': 'Tela',
        'herb_red_sage': 'Salvia',
        'herb_wild_mint': 'Menta',
        'botella': 'Botella',
        'cotton': 'Algodón',
        'alcohol_medicinal': 'Alcohol medicinal',
        'hierba_medicinal': 'Hierba medicinal',
        'vendas_limpias': 'Vendas limpias',
        'frasco_vacio': 'Frasco vacío',
    },
    'perista': {
        'joya_robada': 'Joya robada',
        'oro_sucio': 'Oro sucio',
        'plata_sucia': 'Plata sucia',
        'carbon': 'Carbón',
    },
    'pescadero': {
        'pescado': 'Pescado',
        'salmon': 'Salmón',
        'trucha': 'Trucha',
        'sal': 'Sal',
        'limon': 'Limón',
        'wood': 'Madera (ahumar)',
    },
    'tabacalero': {
        'hoja_tabaco': 'Hoja de tabaco',
        'papel_fumar': 'Papel para fumar',
        'filtro': 'Filtro',
    },
}

# ============================================================================
# ANIMACIONES DISPONIBLES
# ============================================================================
ANIMACIONES = {
    'craft': 'Crafteo genérico',
    'cooking': 'Cocinando',
    'medical': 'Médico',
    'brewing': 'Destilando',
    'smithing': 'Herrería',
}
