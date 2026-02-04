"""
Generador de Crafteos para RedM - VORP Crafting System
Aplicación Streamlit interactiva
"""

import streamlit as st
from config_items import (
    JOBS, TIPOS_CRAFTEO, ITEMS_RECOMPENSA, ITEMS_INGREDIENTES, 
    ANIMACIONES, CONFIG_PATH
)
from lua_crafteo_generator import generate_crafting_block

# ============================================================================
# CONFIGURACIÓN DE LA PÁGINA
# ============================================================================
st.set_page_config(
    page_title="Generador de Crafteos RedM",
    page_icon="🔨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# ESTILOS CSS PERSONALIZADOS
# ============================================================================
st.markdown("""
<style>
    .stAlert {
        padding: 10px;
        border-radius: 5px;
    }
    .main-header {
        text-align: center;
        padding: 20px;
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .main-header h1 {
        color: white;
        margin: 0;
    }
    .ingredient-box {
        background-color: #262730;
        padding: 10px;
        border-radius: 5px;
        margin: 5px 0;
    }
    code {
        white-space: pre-wrap !important;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# FUNCIONES AUXILIARES
# ============================================================================

def get_items_for_job(job_key: str) -> dict:
    """Obtiene los items de recompensa para un job específico"""
    return ITEMS_RECOMPENSA.get(job_key, {})

def get_ingredientes_for_job(job_key: str) -> dict:
    """Obtiene los ingredientes disponibles para un job (comunes + específicos)"""
    ingredientes = ITEMS_INGREDIENTES.get('comunes', {}).copy()
    ingredientes.update(ITEMS_INGREDIENTES.get(job_key, {}))
    return ingredientes

def is_weapon_item(item_id: str) -> bool:
    """Verifica si un item es un arma"""
    return item_id.startswith('weapon_')

# ============================================================================
# INICIALIZACIÓN DE SESSION STATE
# ============================================================================
if 'ingredientes' not in st.session_state:
    st.session_state.ingredientes = []

if 'job_seleccionado' not in st.session_state:
    st.session_state.job_seleccionado = None

# ============================================================================
# HEADER PRINCIPAL
# ============================================================================
st.markdown("""
<div class="main-header">
    <h1>🔨 Generador de Crafteos RedM</h1>
    <p style="color: #ccc; margin: 5px 0 0 0;">VORP Crafting System - Herramienta de Configuración</p>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# SIDEBAR - INFORMACIÓN Y CONFIG
# ============================================================================
with st.sidebar:
    st.header("ℹ️ Información")
    st.info("**Configs incluidos en el repositorio**")
    
    st.markdown("---")
    st.subheader("📋 Jobs Disponibles")
    for job_key, job_data in JOBS.items():
        st.text(f"• {job_data['nombre']}")
    
    st.markdown("---")
    st.caption("Herramienta desarrollada para reducir errores en la configuración de crafteos")

# ============================================================================
# LAYOUT PRINCIPAL
# ============================================================================
col_form, col_output = st.columns([1, 1])

# ============================================================================
# COLUMNA IZQUIERDA - FORMULARIO
# ============================================================================
with col_form:
    st.header("📝 Configurar Crafteo")
    
    # ----- PASO 1: SELECCIONAR JOB -----
    st.subheader("1️⃣ Seleccionar Categoría/Job")
    
    job_options = {k: v['nombre'] for k, v in JOBS.items()}
    job_seleccionado = st.selectbox(
        "Job/Facción",
        options=list(job_options.keys()),
        format_func=lambda x: job_options[x],
        key="job_select",
        help="Selecciona la facción para la que es este crafteo"
    )
    
    # Detectar cambio de job para limpiar ingredientes
    if st.session_state.job_seleccionado != job_seleccionado:
        st.session_state.job_seleccionado = job_seleccionado
        st.session_state.ingredientes = []
    
    # Obtener datos del job seleccionado
    job_data = JOBS[job_seleccionado]
    
    st.markdown("---")
    
    # ----- PASO 2: INFORMACIÓN BÁSICA -----
    st.subheader("2️⃣ Información del Crafteo")
    
    nombre = st.text_input(
        "Nombre del Crafteo *",
        placeholder="Ej: Munición de pistola",
        help="Nombre que verá el jugador en el menú"
    )
    
    # Tipo de crafteo - dinámico según el job
    if job_seleccionado in ['armero', 'bandas']:
        tipo_options = {'item': 'Item Normal', 'weapon': 'Arma'}
    else:
        tipo_options = {'item': 'Item Normal'}
    
    tipo = st.selectbox(
        "Tipo de Crafteo",
        options=list(tipo_options.keys()),
        format_func=lambda x: tipo_options[x],
        help="Tipo de item que se craftea"
    )
    
    nivel_minimo = st.number_input(
        "Nivel Mínimo Requerido",
        min_value=0,
        max_value=100,
        value=0,
        help="Nivel que necesita el jugador para craftear"
    )
    
    st.markdown("---")
    
    # ----- PASO 3: RECOMPENSA -----
    st.subheader("3️⃣ Recompensa")
    
    # Obtener items disponibles para este job
    items_disponibles = get_items_for_job(job_seleccionado)
    
    # Filtrar según tipo seleccionado
    if tipo == 'weapon':
        items_filtrados = {k: v for k, v in items_disponibles.items() if is_weapon_item(k)}
    else:
        items_filtrados = {k: v for k, v in items_disponibles.items() if not is_weapon_item(k)}
    
    if not items_filtrados:
        st.warning("No hay items disponibles para este tipo. Puedes escribir el ID manualmente.")
        items_filtrados = items_disponibles
    
    col_rew1, col_rew2 = st.columns([3, 1])
    
    with col_rew1:
        # Opción para escribir manualmente o seleccionar
        usar_item_manual = st.checkbox("Escribir ID manualmente", key="manual_reward")
        
        if usar_item_manual:
            recompensa = st.text_input(
                "ID del Item de Recompensa *",
                placeholder="Ej: weapon_revolver_cattleman"
            )
            recompensa_label = recompensa
        else:
            recompensa = st.selectbox(
                "Item de Recompensa *",
                options=[""] + list(items_filtrados.keys()),
                format_func=lambda x: f"{items_filtrados[x]} ({x})" if x else "-- Seleccionar --",
                help="Item que recibirá el jugador"
            )
            recompensa_label = items_filtrados.get(recompensa, recompensa)
    
    with col_rew2:
        cantidad_recompensa = st.number_input(
            "Cantidad",
            min_value=1,
            max_value=999,
            value=1,
            key="cant_rew"
        )
    
    st.markdown("---")
    
    # ----- PASO 4: INGREDIENTES -----
    st.subheader("4️⃣ Ingredientes")
    
    # Obtener ingredientes disponibles para este job
    ingredientes_disponibles = get_ingredientes_for_job(job_seleccionado)
    
    st.markdown("**Añadir Ingrediente:**")
    col_ing1, col_ing2, col_ing3 = st.columns([3, 1, 1])
    
    with col_ing1:
        usar_ing_manual = st.checkbox("ID manual", key="manual_ing")
        
        if usar_ing_manual:
            nuevo_ingrediente = st.text_input(
                "ID del Ingrediente",
                placeholder="Ej: gunpowder",
                key="new_ing_manual"
            )
            nuevo_ingrediente_label = nuevo_ingrediente
        else:
            nuevo_ingrediente = st.selectbox(
                "Ingrediente",
                options=[""] + list(ingredientes_disponibles.keys()),
                format_func=lambda x: f"{ingredientes_disponibles[x]} ({x})" if x else "-- Seleccionar --",
                key="new_ing_select"
            )
            nuevo_ingrediente_label = ingredientes_disponibles.get(nuevo_ingrediente, nuevo_ingrediente)
    
    with col_ing2:
        cantidad_ingrediente = st.number_input(
            "Cantidad",
            min_value=1,
            max_value=999,
            value=1,
            key="cant_ing"
        )
    
    with col_ing3:
        st.write("")  # Espaciador
        if st.button("➕ Añadir", use_container_width=True, type="primary"):
            if nuevo_ingrediente:
                st.session_state.ingredientes.append({
                    'name': nuevo_ingrediente,
                    'label': nuevo_ingrediente_label,
                    'count': cantidad_ingrediente
                })
                st.rerun()
            else:
                st.error("Selecciona un ingrediente")
    
    # Mostrar ingredientes añadidos
    if st.session_state.ingredientes:
        st.markdown("**Ingredientes actuales:**")
        for idx, ing in enumerate(st.session_state.ingredientes):
            col_list1, col_list2 = st.columns([4, 1])
            with col_list1:
                st.markdown(f"""
                <div class="ingredient-box">
                    📦 <strong>{ing['label']}</strong> ({ing['name']}) - Cantidad: <strong>{ing['count']}</strong>
                </div>
                """, unsafe_allow_html=True)
            with col_list2:
                if st.button("🗑️", key=f"del_{idx}"):
                    st.session_state.ingredientes.pop(idx)
                    st.rerun()
        
        if st.button("🗑️ Limpiar todos", type="secondary"):
            st.session_state.ingredientes = []
            st.rerun()
    else:
        st.info("Añade al menos un ingrediente para generar el crafteo")
    
    st.markdown("---")
    
    # ----- PASO 5: OPCIONES AVANZADAS -----
    with st.expander("⚙️ Opciones Avanzadas"):
        col_adv1, col_adv2 = st.columns(2)
        
        with col_adv1:
            take_items = st.checkbox(
                "Consumir ingredientes (TakeItems)",
                value=True,
                help="Si los ingredientes se consumen al craftear"
            )
            
            use_currency = st.checkbox(
                "Usar dinero (UseCurrencyMode)",
                value=False,
                help="Si se cobra dinero además de ingredientes"
            )
            
            if use_currency:
                currency_type = st.selectbox(
                    "Tipo de moneda",
                    options=[0, 1],
                    format_func=lambda x: "Cash ($)" if x == 0 else "Gold (oro)"
                )
            else:
                currency_type = 0
        
        with col_adv2:
            location = st.number_input(
                "Location ID",
                min_value=0,
                value=0,
                help="ID de ubicación para el crafteo"
            )
            
            animation = st.selectbox(
                "Animación",
                options=list(ANIMACIONES.keys()),
                format_func=lambda x: ANIMACIONES[x]
            )

# ============================================================================
# COLUMNA DERECHA - OUTPUT
# ============================================================================
with col_output:
    st.header("📤 Código Lua Generado")
    
    # Validaciones
    errores = []
    if not nombre:
        errores.append("Falta el nombre del crafteo")
    if not recompensa:
        errores.append("Falta seleccionar la recompensa")
    if not st.session_state.ingredientes:
        errores.append("Añade al menos un ingrediente")
    
    if errores:
        st.warning("**⚠️ Completa los campos requeridos:**")
        for e in errores:
            st.write(f"• {e}")
    else:
        # Generar descripción automática
        desc_parts = []
        for ing in st.session_state.ingredientes:
            desc_parts.append(f"{ing['count']}x {ing['label']}")
        descripcion = ", ".join(desc_parts)
        
        # Obtener Category del job
        category = job_data['category']
        job_value = job_data['job_value']
        
        # Preparar datos
        datos_crafteo = {
            'nombre': nombre,
            'descripcion': descripcion,
            'categoria': category,
            'tipo': tipo,
            'nivel_minimo': nivel_minimo,
            'recompensa': recompensa,
            'cantidad_recompensa': cantidad_recompensa,
            'ingredientes': st.session_state.ingredientes,
            'take_items': take_items,
            'currency_type': currency_type,
            'location': location,
            'animation': animation,
            'use_currency': use_currency,
            'job': job_value
        }
        
        # Generar código
        codigo_lua = generate_crafting_block(datos_crafteo)
        
        # Mostrar resumen
        st.success("✅ Crafteo configurado correctamente")
        
        st.info(f"""
**📋 Resumen:**
- **Job:** {job_data['nombre']}
- **Nombre:** {nombre}
- **Tipo:** {tipo_options.get(tipo, tipo)}
- **Recompensa:** {cantidad_recompensa}x {recompensa_label}
- **Ingredientes:** {len(st.session_state.ingredientes)}
- **Nivel mínimo:** {nivel_minimo}
- **Archivo destino:** `config_{job_seleccionado}.lua`
        """)
        
        # Mostrar código
        st.markdown("**Código Lua:**")
        st.code(codigo_lua, language="lua")
        
        # Botón de descarga
        st.download_button(
            label="💾 Descargar código",
            data=codigo_lua,
            file_name=f"crafteo_{job_seleccionado}_{nombre.lower().replace(' ', '_')}.lua",
            mime="text/plain",
            use_container_width=True
        )
        
        # Info sobre dónde pegar
        st.markdown("---")
        st.markdown(f"""
        **📁 Instrucciones:**
        1. Abre el archivo `config_{job_seleccionado}.lua`
        2. Busca la sección del nivel {nivel_minimo} (o créala)
        3. Pega el código antes del cierre `}}`
        4. Guarda el archivo y recarga el servidor
        """)

# ============================================================================
# FOOTER
# ============================================================================
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; font-size: 12px;'>
    <p>Generador de Crafteos para RedM - VORP Crafting System</p>
    <p>Desarrollado para La Hermandad</p>
</div>
""", unsafe_allow_html=True)
