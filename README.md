# 🔨 Generador de Crafteos RedM - VORP Crafting

Herramienta web para generar código Lua de crafteos para servidores RedM con el sistema VORP Crafting.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://config-generator.streamlit.app)

## 🎯 Características

- ✅ Interfaz visual intuitiva
- ✅ Selección de Job/Facción con items filtrados
- ✅ Soporte para 18 categorías diferentes
- ✅ Items y armas para cada facción
- ✅ Generación automática de código Lua
- ✅ Validación para reducir errores
- ✅ Descarga directa del código generado

## 🚀 Demo Online

Accede a la herramienta desplegada en Streamlit Cloud:
**[https://config-generator.streamlit.app](https://config-generator.streamlit.app)**

## 📦 Instalación Local

```bash
# Clonar el repositorio
git clone https://github.com/XzRaulzX/Config_generator.git
cd Config_generator

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar
streamlit run app_crafteo.py
```

## 🏷️ Categorías Soportadas

| Categoría | Emoji |
|-----------|-------|
| Agricultor | 🌾 |
| Armero | 🔫 |
| Artesano | 🎨 |
| Bandas | 💀 |
| Cocina Dulce | 🍰 |
| Cocina Mixta | 🍲 |
| Cocina Packs | 📦 |
| Cocina Tier 1 | 🍳 |
| Cocina Tier 2 | 👨‍🍳 |
| Cocina Tier 3 | 👩‍🍳 |
| Destilador | 🥃 |
| Distribuidora | 🚚 |
| Establo | 🐴 |
| Ganadero | 🐄 |
| Médicos | ⚕️ |
| Perista | 💰 |
| Pescadero | 🎣 |
| Tabacalero | 🚬 |

## 📝 Formato de Salida

El código generado sigue el formato estándar de VORP Crafting:

```lua
{
    TakeItems = true,
    CurrencyType = 0,
    Location = 0,
    Animation = "craft",
    Category = "Armero",
    Text = "Munición de pistola",
    Desc = "1x Pólvora, 1x Carcasa de bala",
    Reward = {{
        name = "ammopistolnormal",
        count = 1
    }},
    Minlvl = 3,
    UseCurrencyMode = false,
    Job = 0,
    Type = "item",
    Items = {{
        name = "gunpowder",
        count = 1,
        take = true
    }, {
        name = "carcasa_bala",
        count = 1,
        take = true
    }}
},
```

## 📁 Estructura del Proyecto

```
Config_generator/
├── app_crafteo.py          # Aplicación principal Streamlit
├── config_items.py         # Base de datos de items y jobs
├── lua_crafteo_generator.py # Generador de código Lua
├── requirements.txt        # Dependencias
├── configs/               # Archivos de configuración Lua
│   ├── config_agricultor.lua
│   ├── config_armero.lua
│   └── ...
└── .streamlit/
    └── config.toml        # Configuración de Streamlit
```

## 🛠️ Tecnologías

- **Python 3.8+**
- **Streamlit** - Framework web
- **Lua** - Formato de salida

## 📄 Licencia

Herramienta interna para servidores RedM.

---

Desarrollado con ❤️ para La Hermandad
