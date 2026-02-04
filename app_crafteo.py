"""
Generador de Crafteos para RedM - VORP Crafting System
Aplicación Streamlit interactiva con diseño mejorado
"""

import streamlit as st
from config_items import (
    JOBS, TIPOS_CRAFTEO, ITEMS_RECOMPENSA, ITEMS_INGREDIENTES, 
    ANIMACIONES, CONFIG_PATH, ALL_ITEMS
)
from lua_crafteo_generator import (
    generate_crafting_block, 
    add_crafting_to_config,
    get_config_file_content
)

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
# ESTILOS CSS PERSONALIZADOS - DISEÑO MODERNO
# ============================================================================
st.markdown("""
<style>
    /* Reset y variables */
    :root {
        --primary-color: #ff6b35;
        --secondary-color: #2a5298;
        --bg-dark: #0e1117;
        --bg-card: #1a1d24;
        --bg-card-hover: #262b36;
        --text-primary: #fafafa;
        --text-secondary: #b0b0b0;
        --success-color: #00d26a;
        --warning-color: #ffc107;
        --error-color: #ff4757;
        --border-radius: 12px;
    }
    
    /* Header principal */
    .main-header {
        text-align: center;
        padding: 30px 20px;
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 50%, #ff6b35 100%);
        border-radius: var(--border-radius);
        margin-bottom: 25px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .main-header h1 {
        color: white;
        margin: 0;
        font-size: 2.5rem;
        font-weight: 700;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    .main-header p {
        color: rgba(255, 255, 255, 0.85);
        margin: 10px 0 0 0;
        font-size: 1.1rem;
    }
    
    /* Tarjetas de sección */
    .section-card {
        background: var(--bg-card);
        padding: 20px;
        border-radius: var(--border-radius);
        margin-bottom: 20px;
        border: 1px solid rgba(255, 255, 255, 0.05);
        transition: all 0.3s ease;
    }
    
    .section-card:hover {
        border-color: rgba(255, 107, 53, 0.3);
        box-shadow: 0 4px 20px rgba(255, 107, 53, 0.1);
    }
    
    .section-title {
        color: var(--primary-color);
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    /* Ingredientes */
    .ingredient-box {
        background: linear-gradient(135deg, #1a1d24 0%, #262b36 100%);
        padding: 15px;
        border-radius: 10px;
        margin: 8px 0;
        border-left: 4px solid var(--primary-color);
        display: flex;
        align-items: center;
        justify-content: space-between;
        transition: all 0.2s ease;
    }
    
    .ingredient-box:hover {
        transform: translateX(5px);
        background: linear-gradient(135deg, #262b36 0%, #2d323d 100%);
    }
    
    .ingredient-info {
        display: flex;
        align-items: center;
        gap: 12px;
    }
    
    .ingredient-icon {
        font-size: 1.5rem;
    }
    
    .ingredient-name {
        font-weight: 600;
        color: var(--text-primary);
    }
    
    .ingredient-id {
        color: var(--text-secondary);
        font-size: 0.85rem;
        font-family: monospace;
    }
    
    .ingredient-count {
        background: var(--primary-color);
        color: white;
        padding: 5px 12px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 0.9rem;
    }
    
    /* Stats cards */
    .stats-container {
        display: flex;
        gap: 15px;
        margin-bottom: 20px;
    }
    
    .stat-card {
        background: var(--bg-card);
        padding: 15px 20px;
        border-radius: 10px;
        flex: 1;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }
    
    .stat-number {
        font-size: 2rem;
        font-weight: 700;
        color: var(--primary-color);
    }
    
    .stat-label {
        color: var(--text-secondary);
        font-size: 0.85rem;
        margin-top: 5px;
    }
    
    /* Job badges */
    .job-badge {
        display: inline-block;
        padding: 8px 16px;
        border-radius: 25px;
        font-size: 0.9rem;
        font-weight: 600;
        margin: 4px;
        background: linear-gradient(135deg, var(--bg-card) 0%, var(--bg-card-hover) 100%);
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.2s ease;
    }
    
    .job-badge:hover {
        transform: scale(1.05);
        border-color: var(--primary-color);
    }
    
    /* Resumen crafteo */
    .craft-summary {
        background: linear-gradient(135deg, #1a2a1a 0%, #1a1d24 100%);
        border: 1px solid var(--success-color);
        border-radius: var(--border-radius);
        padding: 20px;
        margin: 15px 0;
    }
    
    .craft-summary-title {
        color: var(--success-color);
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 15px;
    }
    
    .summary-row {
        display: flex;
        justify-content: space-between;
        padding: 8px 0;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    }
    
    .summary-label {
        color: var(--text-secondary);
    }
    
    .summary-value {
        color: var(--text-primary);
        font-weight: 500;
    }
    
    /* Código Lua */
    .lua-code-container {
        background: #1e1e1e;
        border-radius: var(--border-radius);
        border: 1px solid #333;
        overflow: hidden;
    }
    
    .lua-code-header {
        background: #2d2d2d;
        padding: 10px 15px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid #333;
    }
    
    .lua-code-title {
        color: var(--primary-color);
        font-weight: 600;
    }
    
    /* Botones personalizados */
    .stButton > button {
        border-radius: 10px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 15px rgba(255, 107, 53, 0.3) !important;
    }
    
    /* Download button */
    .stDownloadButton > button {
        background: linear-gradient(135deg, var(--success-color) 0%, #00b359 100%) !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
    }
    
    .stDownloadButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 15px rgba(0, 210, 106, 0.4) !important;
    }
    
    /* Selectbox mejorado */
    .stSelectbox > div > div {
        border-radius: 10px !important;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background: var(--bg-card) !important;
        border-radius: 10px !important;
    }
    
    /* Sidebar */
    .css-1d391kg, [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0e1117 0%, #1a1d24 100%);
    }
    
    .sidebar-stat {
        background: var(--bg-card);
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        text-align: center;
    }
    
    .sidebar-stat-number {
        font-size: 1.8rem;
        font-weight: 700;
        color: var(--primary-color);
    }
    
    .sidebar-stat-label {
        color: var(--text-secondary);
        font-size: 0.8rem;
    }
    
    /* Info boxes */
    .info-tip {
        background: linear-gradient(135deg, #1a2a3a 0%, #1a1d24 100%);
        border-left: 4px solid var(--secondary-color);
        padding: 15px;
        border-radius: 0 10px 10px 0;
        margin: 10px 0;
    }
    
    /* Empty state */
    .empty-state {
        text-align: center;
        padding: 40px 20px;
        color: var(--text-secondary);
    }
    
    .empty-state-icon {
        font-size: 3rem;
        margin-bottom: 15px;
    }
    
    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .animate-in {
        animation: fadeIn 0.3s ease-out;
    }
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: var(--bg-dark);
    }
    
    ::-webkit-scrollbar-thumb {
        background: var(--primary-color);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #ff8c5a;
    }
    
    /* Code block */
    code {
        white-space: pre-wrap !important;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
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

def filter_items(items_dict: dict, search_term: str) -> dict:
    """Filtra items por término de búsqueda"""
    if not search_term:
        return items_dict
    search_lower = search_term.lower()
    return {k: v for k, v in items_dict.items() 
            if search_lower in k.lower() or search_lower in v.lower()}

# ============================================================================
# INICIALIZACIÓN DE SESSION STATE
# ============================================================================
if 'ingredientes' not in st.session_state:
    st.session_state.ingredientes = []

if 'recompensas' not in st.session_state:
    st.session_state.recompensas = []

if 'job_seleccionado' not in st.session_state:
    st.session_state.job_seleccionado = None

if 'search_recompensa' not in st.session_state:
    st.session_state.search_recompensa = ""

if 'search_ingrediente' not in st.session_state:
    st.session_state.search_ingrediente = ""

# ============================================================================
# HEADER PRINCIPAL
# ============================================================================
st.markdown("""
<div class="main-header animate-in">
    <h1>🔨 Generador de Crafteos RedM</h1>
    <p>VORP Crafting System - Herramienta de Configuración para La Hermandad</p>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# SIDEBAR - INFORMACIÓN Y ESTADÍSTICAS
# ============================================================================
with st.sidebar:
    st.markdown("### 📊 Estadísticas")
    
    # Stats
    st.markdown(f"""
    <div class="sidebar-stat">
        <div class="sidebar-stat-number">{len(ALL_ITEMS):,}</div>
        <div class="sidebar-stat-label">Items Disponibles</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="sidebar-stat">
        <div class="sidebar-stat-number">{len(JOBS)}</div>
        <div class="sidebar-stat-label">Categorías</div>
    </div>
    """, unsafe_allow_html=True)
    
    col_stat1, col_stat2 = st.columns(2)
    with col_stat1:
        st.markdown(f"""
        <div class="sidebar-stat">
            <div class="sidebar-stat-number">{len(st.session_state.recompensas)}</div>
            <div class="sidebar-stat-label">Recompensas</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col_stat2:
        st.markdown(f"""
        <div class="sidebar-stat">
            <div class="sidebar-stat-number">{len(st.session_state.ingredientes)}</div>
            <div class="sidebar-stat-label">Ingredientes</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Jobs disponibles con badges
    st.markdown("### 📋 Categorías")
    
    jobs_html = ""
    for job_key, job_data in JOBS.items():
        jobs_html += f'<span class="job-badge">{job_data["nombre"]}</span>'
    
    st.markdown(f'<div style="line-height: 2.5;">{jobs_html}</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Tips
    st.markdown("### 💡 Tips")
    st.markdown("""
    <div class="info-tip">
        <strong>Búsqueda rápida:</strong> Usa el campo de búsqueda para filtrar entre los +1000 items disponibles.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-tip">
        <strong>Ingredientes:</strong> Puedes añadir el mismo ingrediente varias veces con diferentes cantidades.
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# LAYOUT PRINCIPAL
# ============================================================================
col_form, col_output = st.columns([1, 1], gap="large")

# ============================================================================
# COLUMNA IZQUIERDA - FORMULARIO
# ============================================================================
with col_form:
    st.markdown("## 📝 Configurar Crafteo")
    
    # ----- PASO 1: SELECCIONAR JOB -----
    st.markdown("""
    <div class="section-card">
        <div class="section-title">🏷️ Paso 1: Categoría</div>
    </div>
    """, unsafe_allow_html=True)
    
    job_options = {k: v['nombre'] for k, v in JOBS.items()}
    job_seleccionado = st.selectbox(
        "Selecciona la categoría/job",
        options=list(job_options.keys()),
        format_func=lambda x: job_options[x],
        key="job_select",
        help="Selecciona la facción para la que es este crafteo"
    )
    
    # Detectar cambio de job para limpiar ingredientes y recompensas
    if st.session_state.job_seleccionado != job_seleccionado:
        st.session_state.job_seleccionado = job_seleccionado
        st.session_state.ingredientes = []
        st.session_state.recompensas = []
    
    job_data = JOBS[job_seleccionado]
    
    # ----- PASO 2: INFORMACIÓN BÁSICA -----
    st.markdown("""
    <div class="section-card">
        <div class="section-title">✏️ Paso 2: Información Básica</div>
    </div>
    """, unsafe_allow_html=True)
    
    col_info1, col_info2 = st.columns([2, 1])
    
    with col_info1:
        nombre = st.text_input(
            "Nombre del Crafteo *",
            placeholder="Ej: Munición de pistola",
            help="Nombre que verá el jugador en el menú"
        )
    
    with col_info2:
        nivel_minimo = st.number_input(
            "Nivel Mínimo",
            min_value=0,
            max_value=100,
            value=0,
            help="Nivel requerido para craftear"
        )
    
    # Tipo de crafteo
    if job_seleccionado in ['armero', 'bandas']:
        tipo_options = {'item': '📦 Item Normal', 'weapon': '🔫 Arma'}
    else:
        tipo_options = {'item': '📦 Item Normal'}
    
    tipo = st.selectbox(
        "Tipo de Crafteo",
        options=list(tipo_options.keys()),
        format_func=lambda x: tipo_options[x],
        help="Tipo de item que se craftea"
    )
    
    # ----- PASO 3: RECOMPENSAS -----
    st.markdown("""
    <div class="section-card">
        <div class="section-title">🎁 Paso 3: Recompensas</div>
    </div>
    """, unsafe_allow_html=True)
    
    items_disponibles = get_items_for_job(job_seleccionado)
    
    # Filtrar según tipo
    if tipo == 'weapon':
        items_filtrados = {k: v for k, v in items_disponibles.items() if is_weapon_item(k)}
    else:
        items_filtrados = {k: v for k, v in items_disponibles.items() if not is_weapon_item(k)}
    
    if not items_filtrados:
        items_filtrados = items_disponibles
    
    # Búsqueda de recompensa
    col_search_rew, col_manual_rew = st.columns([3, 1])
    
    with col_search_rew:
        search_recompensa = st.text_input(
            "🔍 Buscar item de recompensa",
            placeholder="Escribe para filtrar...",
            key="search_rew_input"
        )
    
    with col_manual_rew:
        usar_item_manual = st.checkbox("ID manual", key="manual_reward")
    
    # Filtrar items
    items_filtrados_search = filter_items(items_filtrados, search_recompensa)
    
    col_rew1, col_rew2, col_rew3 = st.columns([3, 1, 1])
    
    with col_rew1:
        if usar_item_manual:
            nueva_recompensa = st.text_input(
                "ID del Item",
                placeholder="Ej: weapon_revolver_cattleman",
                key="manual_rew_input"
            )
            nueva_recompensa_label = nueva_recompensa
        else:
            # Mostrar cantidad de items filtrados
            if search_recompensa:
                st.caption(f"📋 {len(items_filtrados_search)} items encontrados")
            
            nueva_recompensa = st.selectbox(
                "Item de Recompensa",
                options=[""] + list(items_filtrados_search.keys()),
                format_func=lambda x: f"{items_filtrados_search[x]} ({x})" if x else "-- Seleccionar item --",
                help="Item que recibirá el jugador",
                key="new_rew_select"
            )
            nueva_recompensa_label = items_filtrados_search.get(nueva_recompensa, nueva_recompensa)
    
    with col_rew2:
        cantidad_recompensa = st.number_input(
            "Cantidad",
            min_value=1,
            max_value=999,
            value=1,
            key="cant_rew"
        )
    
    with col_rew3:
        st.write("")
        st.write("")
        if st.button("➕ Añadir", use_container_width=True, type="primary", key="add_reward"):
            if nueva_recompensa:
                st.session_state.recompensas.append({
                    'name': nueva_recompensa,
                    'label': nueva_recompensa_label,
                    'count': cantidad_recompensa
                })
                st.rerun()
            else:
                st.error("⚠️ Selecciona un item de recompensa")
    
    # Mostrar recompensas añadidas
    if st.session_state.recompensas:
        st.markdown(f"**Recompensas añadidas ({len(st.session_state.recompensas)}):**")
        
        for idx, rew in enumerate(st.session_state.recompensas):
            col_list1, col_list2 = st.columns([5, 1])
            with col_list1:
                st.markdown(f"""
                <div class="ingredient-box" style="border-left-color: #00d26a;">
                    <div class="ingredient-info">
                        <span class="ingredient-icon">🎁</span>
                        <div>
                            <div class="ingredient-name">{rew['label']}</div>
                            <div class="ingredient-id">{rew['name']}</div>
                        </div>
                    </div>
                    <span class="ingredient-count" style="background: #00d26a;">x{rew['count']}</span>
                </div>
                """, unsafe_allow_html=True)
            with col_list2:
                st.write("")
                if st.button("🗑️", key=f"del_rew_{idx}", help="Eliminar recompensa"):
                    st.session_state.recompensas.pop(idx)
                    st.rerun()
        
        col_clear_rew1, col_clear_rew2 = st.columns([1, 1])
        with col_clear_rew2:
            if st.button("🗑️ Limpiar recompensas", type="secondary", use_container_width=True, key="clear_rewards"):
                st.session_state.recompensas = []
                st.rerun()
    else:
        st.markdown("""
        <div class="empty-state" style="padding: 20px;">
            <div class="empty-state-icon">🎁</div>
            <p>No hay recompensas añadidas</p>
            <p style="font-size: 0.85rem;">Añade al menos un item como recompensa</p>
        </div>
        """, unsafe_allow_html=True)
    
    # ----- PASO 4: INGREDIENTES -----
    st.markdown("""
    <div class="section-card">
        <div class="section-title">🧪 Paso 4: Ingredientes</div>
    </div>
    """, unsafe_allow_html=True)
    
    ingredientes_disponibles = get_ingredientes_for_job(job_seleccionado)
    
    # Búsqueda de ingredientes
    col_search_ing, col_manual_ing = st.columns([3, 1])
    
    with col_search_ing:
        search_ingrediente = st.text_input(
            "🔍 Buscar ingrediente",
            placeholder="Escribe para filtrar...",
            key="search_ing_input"
        )
    
    with col_manual_ing:
        usar_ing_manual = st.checkbox("ID manual", key="manual_ing")
    
    # Filtrar ingredientes
    ingredientes_filtrados = filter_items(ingredientes_disponibles, search_ingrediente)
    
    col_ing1, col_ing2, col_ing3 = st.columns([3, 1, 1])
    
    with col_ing1:
        if usar_ing_manual:
            nuevo_ingrediente = st.text_input(
                "ID del Ingrediente",
                placeholder="Ej: gunpowder",
                key="new_ing_manual"
            )
            nuevo_ingrediente_label = nuevo_ingrediente
        else:
            if search_ingrediente:
                st.caption(f"📋 {len(ingredientes_filtrados)} items encontrados")
            
            nuevo_ingrediente = st.selectbox(
                "Ingrediente",
                options=[""] + list(ingredientes_filtrados.keys()),
                format_func=lambda x: f"{ingredientes_filtrados[x]} ({x})" if x else "-- Seleccionar ingrediente --",
                key="new_ing_select"
            )
            nuevo_ingrediente_label = ingredientes_filtrados.get(nuevo_ingrediente, nuevo_ingrediente)
    
    with col_ing2:
        cantidad_ingrediente = st.number_input(
            "Cantidad",
            min_value=1,
            max_value=999,
            value=1,
            key="cant_ing"
        )
    
    with col_ing3:
        st.write("")
        st.write("")
        if st.button("➕ Añadir", use_container_width=True, type="primary"):
            if nuevo_ingrediente:
                st.session_state.ingredientes.append({
                    'name': nuevo_ingrediente,
                    'label': nuevo_ingrediente_label,
                    'count': cantidad_ingrediente
                })
                st.rerun()
            else:
                st.error("⚠️ Selecciona un ingrediente")
    
    # Mostrar ingredientes añadidos
    if st.session_state.ingredientes:
        st.markdown(f"**Ingredientes añadidos ({len(st.session_state.ingredientes)}):**")
        
        for idx, ing in enumerate(st.session_state.ingredientes):
            col_list1, col_list2 = st.columns([5, 1])
            with col_list1:
                st.markdown(f"""
                <div class="ingredient-box">
                    <div class="ingredient-info">
                        <span class="ingredient-icon">📦</span>
                        <div>
                            <div class="ingredient-name">{ing['label']}</div>
                            <div class="ingredient-id">{ing['name']}</div>
                        </div>
                    </div>
                    <span class="ingredient-count">x{ing['count']}</span>
                </div>
                """, unsafe_allow_html=True)
            with col_list2:
                st.write("")
                if st.button("🗑️", key=f"del_{idx}", help="Eliminar ingrediente"):
                    st.session_state.ingredientes.pop(idx)
                    st.rerun()
        
        col_clear1, col_clear2 = st.columns([1, 1])
        with col_clear2:
            if st.button("🗑️ Limpiar todos", type="secondary", use_container_width=True):
                st.session_state.ingredientes = []
                st.rerun()
    else:
        st.markdown("""
        <div class="empty-state">
            <div class="empty-state-icon">📭</div>
            <p>No hay ingredientes añadidos</p>
            <p style="font-size: 0.85rem;">Usa el selector de arriba para añadir ingredientes</p>
        </div>
        """, unsafe_allow_html=True)
    
    # ----- PASO 5: OPCIONES AVANZADAS -----
    with st.expander("⚙️ Opciones Avanzadas", expanded=False):
        col_adv1, col_adv2 = st.columns(2)
        
        with col_adv1:
            take_items = st.checkbox(
                "🔄 Consumir ingredientes",
                value=True,
                help="Los ingredientes se consumen al craftear"
            )
            
            use_currency = st.checkbox(
                "💰 Cobrar dinero",
                value=False,
                help="Cobrar dinero además de ingredientes"
            )
            
            if use_currency:
                currency_type = st.selectbox(
                    "Tipo de moneda",
                    options=[0, 1],
                    format_func=lambda x: "💵 Cash ($)" if x == 0 else "🪙 Gold (oro)"
                )
            else:
                currency_type = 0
        
        with col_adv2:
            location = st.number_input(
                "📍 Location ID",
                min_value=0,
                value=0,
                help="ID de ubicación para el crafteo"
            )
            
            animation = st.selectbox(
                "🎬 Animación",
                options=list(ANIMACIONES.keys()),
                format_func=lambda x: ANIMACIONES[x]
            )

# ============================================================================
# COLUMNA DERECHA - OUTPUT
# ============================================================================
with col_output:
    st.markdown("## 📤 Resultado")
    
    # Validaciones
    errores = []
    if not nombre:
        errores.append("Nombre del crafteo")
    if not st.session_state.recompensas:
        errores.append("Al menos una recompensa")
    if not st.session_state.ingredientes:
        errores.append("Al menos un ingrediente")
    
    if errores:
        st.markdown("""
        <div class="section-card">
            <div class="section-title" style="color: #ffc107;">⚠️ Campos Requeridos</div>
        </div>
        """, unsafe_allow_html=True)
        
        for e in errores:
            st.markdown(f"• {e}")
        
        st.markdown("""
        <div class="empty-state" style="margin-top: 30px;">
            <div class="empty-state-icon">📋</div>
            <p>Completa todos los campos para generar el código</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        # Generar descripción automática
        desc_parts = [f"{ing['count']}x {ing['label']}" for ing in st.session_state.ingredientes]
        descripcion = ", ".join(desc_parts)
        
        category = job_data['category']
        job_value = job_data['job_value']
        
        datos_crafteo = {
            'nombre': nombre,
            'descripcion': descripcion,
            'categoria': category,
            'tipo': tipo,
            'nivel_minimo': nivel_minimo,
            'recompensas': st.session_state.recompensas,
            'ingredientes': st.session_state.ingredientes,
            'take_items': take_items,
            'currency_type': currency_type,
            'location': location,
            'animation': animation,
            'use_currency': use_currency,
            'job': job_value
        }
        
        codigo_lua = generate_crafting_block(datos_crafteo)
        
        # Generar texto de recompensas para el resumen
        recompensas_texto = ", ".join([f"{r['count']}x {r['label']}" for r in st.session_state.recompensas])
        
        # Resumen visual
        st.markdown(f"""
        <div class="craft-summary">
            <div class="craft-summary-title">✅ Crafteo Configurado</div>
            <div class="summary-row">
                <span class="summary-label">Categoría</span>
                <span class="summary-value">{job_data['nombre']}</span>
            </div>
            <div class="summary-row">
                <span class="summary-label">Nombre</span>
                <span class="summary-value">{nombre}</span>
            </div>
            <div class="summary-row">
                <span class="summary-label">Recompensas</span>
                <span class="summary-value">{len(st.session_state.recompensas)} items</span>
            </div>
            <div class="summary-row">
                <span class="summary-label">Nivel mínimo</span>
                <span class="summary-value">{nivel_minimo}</span>
            </div>
            <div class="summary-row">
                <span class="summary-label">Ingredientes</span>
                <span class="summary-value">{len(st.session_state.ingredientes)} items</span>
            </div>
            <div class="summary-row" style="border: none;">
                <span class="summary-label">Archivo destino</span>
                <span class="summary-value" style="font-family: monospace;">config_{job_seleccionado}.lua</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Lista de recompensas
        st.markdown("**🎁 Recompensas del crafteo:**")
        for rew in st.session_state.recompensas:
            st.markdown(f"- `{rew['count']}x` **{rew['label']}** (`{rew['name']}`)")
        
        # Lista de ingredientes
        st.markdown("**🧪 Ingredientes del crafteo:**")
        for ing in st.session_state.ingredientes:
            st.markdown(f"- `{ing['count']}x` **{ing['label']}** (`{ing['name']}`)")
        
        st.markdown("---")
        
        # Código Lua
        st.markdown("**💻 Código Lua generado:**")
        st.code(codigo_lua, language="lua")
        
        # Botones de acción - Solo código
        col_btn1, col_btn2 = st.columns(2)
        
        with col_btn1:
            st.download_button(
                label="💾 Descargar código",
                data=codigo_lua,
                file_name=f"crafteo_{job_seleccionado}_{nombre.lower().replace(' ', '_')}.lua",
                mime="text/plain",
                use_container_width=True,
                key="download_code"
            )
        
        with col_btn2:
            if st.button("📋 Copiar al portapapeles", use_container_width=True):
                st.toast("✅ Código copiado!", icon="📋")
        
        # Sección de Config Completo
        st.markdown("---")
        st.markdown("""
        <div class="section-card">
            <div class="section-title">📁 Descargar Config Completo</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Verificar si existe el archivo de config
        existing_config = get_config_file_content(job_seleccionado)
        
        if existing_config:
            # Generar el config completo con el nuevo crafteo añadido
            config_completo = add_crafting_to_config(job_seleccionado, codigo_lua)
            
            # Contar crafteos existentes
            crafteos_existentes = existing_config.count('Text = ')
            
            st.success(f"✅ Archivo `config_{job_seleccionado}.lua` encontrado con **{crafteos_existentes}** crafteos existentes")
            
            # Botón para descargar el config completo
            st.download_button(
                label=f"📥 Descargar config_{job_seleccionado}.lua completo",
                data=config_completo,
                file_name=f"config_{job_seleccionado}.lua",
                mime="text/plain",
                use_container_width=True,
                type="primary",
                key="download_full_config"
            )
            
            # Mostrar preview del config
            with st.expander("👁️ Ver preview del config completo", expanded=False):
                st.code(config_completo, language="lua")
        else:
            st.warning(f"⚠️ No se encontró `config_{job_seleccionado}.lua`. Se creará uno nuevo.")
            
            # Crear config nuevo
            config_name = job_seleccionado.capitalize()
            if job_seleccionado == 'cocinaDulce':
                config_name = 'CocinaDulce'
            elif job_seleccionado == 'cocinaMixta':
                config_name = 'CocinaMixta'
            elif job_seleccionado == 'cocinaPacks':
                config_name = 'CocinaPacks'
            elif job_seleccionado == 'cocinaTier1':
                config_name = 'CocinaTier1'
            elif job_seleccionado == 'cocinaTier2':
                config_name = 'CocinaTier2'
            elif job_seleccionado == 'cocinaTier3':
                config_name = 'CocinaTier3'
            
            nuevo_config = f"Config.{config_name} = {{{codigo_lua}\n}}"
            
            st.download_button(
                label=f"📥 Crear y descargar config_{job_seleccionado}.lua",
                data=nuevo_config,
                file_name=f"config_{job_seleccionado}.lua",
                mime="text/plain",
                use_container_width=True,
                type="primary",
                key="download_new_config"
            )
        
        # Instrucciones
        st.markdown("---")
        st.markdown(f"""
        **📁 Instrucciones de instalación:**
        
        1. Descarga el archivo `config_{job_seleccionado}.lua` completo
        2. Reemplaza el archivo existente en tu servidor
        3. Recarga el servidor con `/refresh`
        
        **O manualmente:**
        1. Abre el archivo `config_{job_seleccionado}.lua`
        2. Copia el código del crafteo generado
        3. Pégalo antes del último `}}`
        4. Guarda y recarga
        """)

# ============================================================================
# FOOTER
# ============================================================================
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 20px;'>
    <p style='color: #666; font-size: 0.9rem; margin: 0;'>
        🔨 <strong>Generador de Crafteos para RedM</strong> - VORP Crafting System
    </p>
    <p style='color: #555; font-size: 0.8rem; margin: 5px 0 0 0;'>
        Desarrollado con ❤️ para La Hermandad
    </p>
</div>
""", unsafe_allow_html=True)
