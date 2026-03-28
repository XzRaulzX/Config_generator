"""
Gestor de Configs de Crafteo para RedM — VORP Crafting System
Herramienta Streamlit con integración Google Drive
"""

import streamlit as st
import traceback
import re
from config_items import (
    ALL_ITEMS, BASE_JOBS, ANIMACIONES, CATEGORIAS_CRAFTEO, TIPOS_CRAFTEO,
    PACKS_PREDEFINIDOS, get_job_metadata, get_job_display_name,
    DATA_PATH, load_all_items,
)

# Claves especiales para archivos de metadatos en Drive
_CATEGORIAS_KEY = 'categorias'
_PACKS_KEY = 'packs'
import lua_crafteo_generator as _lcg
import lua_metabolism_generator as _lmg
from lua_crafteo_generator import (
    generate_crafting_block, add_crafting_to_config,
    parse_crafting_blocks, replace_crafting_in_config, delete_crafting_from_config,
    comment_crafting_in_config, uncomment_crafting_in_config, parse_commented_blocks,
    save_config_file, set_storage_mode, get_storage_mode, get_available_configs,
    get_config_name, register_config_name, create_empty_config,
    validate_lua_syntax, validate_full_config, sort_config_alphabetically,
)

# ============================================================================
# GOOGLE DRIVE — INICIALIZACIÓN
# ============================================================================
_drive_available = False
try:
    import drive_manager
    _drive_available = True
except ImportError:
    _drive_available = False


def init_drive_connection():
    if not _drive_available:
        st.session_state.drive_error = "Módulo drive_manager no disponible"
        return False
    try:
        if "gcp_service_account" not in st.secrets:
            st.session_state.drive_error = "No se encontró [gcp_service_account] en st.secrets."
            return False
        raw = st.secrets["gcp_service_account"]
        if 'private_key' not in raw or 'client_email' not in raw:
            st.session_state.drive_error = "Faltan campos en secrets (private_key/client_email)."
            return False
        success, debug_info = drive_manager.init_from_secrets(raw)
        st.session_state.drive_debug = debug_info
        if success:
            st.session_state.drive_error = None
            set_storage_mode('drive', drive_manager)
            _lmg.set_storage_mode('drive', drive_manager)
            return True
        else:
            st.session_state.drive_error = f"Conexión fallida.\n{debug_info}"
            return False
    except Exception as e:
        st.session_state.drive_error = f"{type(e).__name__}: {e}\n{traceback.format_exc()}"
        return False


if 'drive_error' not in st.session_state:
    st.session_state.drive_error = None

if 'drive_connected' not in st.session_state or st.session_state.get('_retry_drive'):
    st.session_state._retry_drive = False
    st.session_state.drive_connected = init_drive_connection()
elif st.session_state.drive_connected and _drive_available:
    set_storage_mode('drive', drive_manager)
    _lmg.set_storage_mode('drive', drive_manager)

# ============================================================================
# CONFIGURACIÓN DE PÁGINA
# ============================================================================
st.set_page_config(
    page_title="Craftsman's Forge — RedM",
    page_icon="⚒️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================================
# CSS — Tema Western compacto
# ============================================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Rye&family=Cinzel:wght@400;600;700&family=IM+Fell+English:ital@0;1&display=swap');
    :root {
        --gold: #c9a227; --gold-light: #dbb84d; --gold-dark: #8b6914;
        --red: #8b0000; --red-dark: #5c0000;
        --brown: #3d2914; --brown-light: #5c3d1e; --brown-dark: #1a1108;
        --leather: #8b4513; --leather-dark: #654321;
        --parchment: #d4c5a9; --cream: #f5e6c8; --sepia: #704214;
    }
    .stApp {
        background: linear-gradient(rgba(18,12,8,.94), rgba(26,17,8,.96));
        background-size: cover; background-attachment: fixed;
    }
    /* Header */
    .main-header {
        text-align:center; padding:30px 20px 25px; margin-bottom:20px;
        background: linear-gradient(var(--parchment), #c4b089);
        border-radius:3px;
        box-shadow: 0 0 0 3px var(--brown-dark), 0 0 0 5px var(--leather), 0 8px 25px rgba(0,0,0,.6);
    }
    .main-header h1 {
        font-family:'Rye',cursive; color:var(--brown-dark); font-size:2.4rem;
        margin:8px 0; letter-spacing:3px; text-transform:uppercase;
    }
    .main-header p {
        font-family:'IM Fell English',serif; color:var(--sepia);
        font-style:italic; margin:5px 0 0; font-size:1rem;
    }
    /* Cards */
    .card {
        background: linear-gradient(145deg, rgba(74,55,40,.95), rgba(42,28,15,.98));
        padding:18px; border-radius:3px; margin-bottom:15px;
        border:2px solid var(--leather-dark);
        box-shadow: inset 0 0 30px rgba(0,0,0,.4), 0 4px 15px rgba(0,0,0,.4);
    }
    .card-title {
        font-family:'Cinzel',serif; color:var(--gold); font-weight:600;
        margin-bottom:12px; text-transform:uppercase; letter-spacing:2px;
        border-bottom:1px solid var(--leather); padding-bottom:8px; font-size:.9rem;
    }
    /* Ingredient/Reward rows */
    .item-row {
        background: linear-gradient(90deg, rgba(139,69,19,.25), rgba(61,41,20,.45));
        padding:10px 14px; border-radius:3px; margin:6px 0;
        border-left:3px solid var(--gold); display:flex;
        align-items:center; justify-content:space-between;
    }
    .item-row .name { font-family:'Cinzel',serif; color:var(--cream); font-weight:600; font-size:.85rem; }
    .item-row .id { font-family:'IM Fell English',serif; color:var(--parchment); font-size:.8rem; opacity:.8; }
    .item-row .count {
        background:var(--gold); color:var(--brown-dark); padding:4px 10px;
        border-radius:2px; font-family:'Cinzel',serif; font-weight:700; font-size:.8rem;
    }
    /* Stat boxes */
    .stat-box {
        background: linear-gradient(var(--parchment), #bca981);
        padding:14px 10px; border-radius:3px; text-align:center; margin:6px 0;
        border:2px solid var(--brown);
        box-shadow: inset 0 0 15px rgba(139,69,19,.15), 0 3px 10px rgba(0,0,0,.3);
    }
    .stat-box .num { font-family:'Rye',cursive; font-size:1.8rem; color:var(--red-dark); }
    .stat-box .lbl { font-family:'Cinzel',serif; color:var(--brown); font-size:.7rem; text-transform:uppercase; letter-spacing:1px; margin-top:3px; }
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(rgba(26,17,8,.96), rgba(42,28,15,.97));
        border-right:3px solid var(--leather-dark);
    }
    /* Buttons */
    .stButton > button {
        font-family:'Cinzel',serif !important; border-radius:2px !important;
        font-weight:600 !important; text-transform:uppercase !important; letter-spacing:1px !important;
        border:2px solid var(--gold) !important;
        background: linear-gradient(145deg, rgba(74,55,40,.95), rgba(42,28,15,.98)) !important;
        color:var(--gold) !important;
    }
    .stButton > button:hover {
        background: linear-gradient(145deg, var(--gold), var(--gold-dark)) !important;
        color:var(--brown-dark) !important;
    }
    .stDownloadButton > button {
        background: linear-gradient(145deg, var(--red), var(--red-dark)) !important;
        border:2px solid var(--gold) !important; color:var(--gold) !important;
        font-family:'Rye',cursive !important; letter-spacing:2px !important;
    }
    /* Inputs */
    .stSelectbox label, .stNumberInput label, .stTextInput label, .stTextArea label {
        font-family:'Cinzel',serif !important; color:var(--gold) !important; text-transform:uppercase !important;
    }
    .stSelectbox > div > div, .stNumberInput > div > div > input, .stTextInput > div > div > input {
        border:2px solid var(--leather) !important; border-radius:2px !important;
        background:var(--brown-dark) !important; color:var(--cream) !important;
    }
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap:4px; background:var(--brown-dark); padding:5px; border-radius:2px; border:2px solid var(--leather);
    }
    .stTabs [data-baseweb="tab"] {
        font-family:'Cinzel',serif !important; text-transform:uppercase; letter-spacing:1px; color:var(--parchment);
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(145deg, var(--gold), var(--gold-light)) !important;
        color:var(--brown-dark) !important;
    }
    /* Checkbox */
    .stCheckbox label { font-family:'IM Fell English',serif !important; color:var(--parchment) !important; }
    /* Expander */
    .streamlit-expanderHeader {
        font-family:'Cinzel',serif !important; color:var(--gold) !important;
    }
    /* Code */
    code { background:var(--brown-dark) !important; color:var(--gold) !important; }
    /* Hide branding + sidebar */
    #MainMenu {visibility:hidden;} footer {visibility:hidden;}
    [data-testid="stSidebar"] {display:none !important;}
    [data-testid="collapsedControl"] {display:none !important;}
    /* Divider */
    .divider { text-align:center; margin:12px 0; color:var(--gold); letter-spacing:8px; font-size:.9rem; }
    /* Compact item rows */
    .item-compact {
        background: linear-gradient(90deg, rgba(139,69,19,.2), rgba(61,41,20,.35));
        padding:6px 10px; border-radius:2px; margin:3px 0;
        border-left:3px solid var(--gold); display:flex;
        align-items:center; justify-content:space-between;
    }
    .item-compact .name { font-family:'Cinzel',serif; color:var(--cream); font-weight:600; font-size:.8rem; }
    .item-compact .id { color:var(--parchment); font-size:.7rem; opacity:.7; }
    .item-compact .count {
        background:var(--gold); color:var(--brown-dark); padding:2px 8px;
        border-radius:2px; font-family:'Cinzel',serif; font-weight:700; font-size:.75rem;
    }
    .item-compact.reward { border-left-color:#00d26a; }
    .item-compact.reward .count { background:#00d26a; }
    /* Section label */
    .section-label {
        font-family:'Cinzel',serif; color:var(--gold); font-weight:600;
        text-transform:uppercase; letter-spacing:2px; font-size:.8rem;
        border-bottom:1px solid var(--leather); padding-bottom:4px; margin:8px 0 6px;
    }
    /* Western quote */
    .western-quote {
        font-family:'IM Fell English',serif; color:var(--parchment); font-style:italic;
        text-align:center; padding:8px; font-size:.85rem; opacity:.8;
    }
    /* Compact summary */
    .summary-compact {
        background: linear-gradient(145deg, rgba(74,55,40,.9), rgba(42,28,15,.95));
        padding:12px; border-radius:3px; border:1px solid var(--leather-dark);
        margin:6px 0;
    }
    .summary-compact td {
        color:var(--parchment); font-family:'IM Fell English',serif;
        padding:2px 6px; font-size:.85rem;
    }
    .summary-compact b { color:var(--gold); }
</style>
""", unsafe_allow_html=True)


# ============================================================================
# HELPERS — PENDING CHANGES SYSTEM
# ============================================================================

# Guardar la función original UNA sola vez en el módulo para evitar recursión
# en reruns de Streamlit (donde el módulo ya está parcheado).
if not hasattr(_lcg, '_original_get_config_file_content'):
    _lcg._original_get_config_file_content = _lcg.get_config_file_content


def _read_from_drive(job_key):
    """Lee directamente desde Drive, sin pasar por monkey-patch."""
    filename = f"config_{job_key}.lua"
    if _drive_available and st.session_state.get('drive_connected'):
        try:
            return drive_manager.read_file(filename)
        except Exception as e:
            print(f"Error leyendo {filename} desde Drive: {e}")
            return None
    return None


def invalidate_drive_cache():
    """Invalida la caché local para forzar recarga desde Drive."""
    st.session_state.pop('_drive_cache', None)
    st.session_state.pop('_cached_config_keys', None)
    st.session_state.pop('_cached_categorias', None)
    st.session_state.pop('_cached_packs', None)
    if _drive_available:
        drive_manager.clear_cache()


def get_config_file_content(job_key):
    """Lee contenido: primero pending, luego caché local, luego Drive."""
    pending = st.session_state.get('pending_changes', {})
    if job_key in pending:
        return pending[job_key]
    # Caché local en session_state
    if '_drive_cache' not in st.session_state:
        st.session_state._drive_cache = {}
    cache = st.session_state._drive_cache
    if job_key not in cache:
        cache[job_key] = _read_from_drive(job_key)
    return cache[job_key]


# Monkey-patch para que funciones internas (comment, delete, etc.) usen pending
_lcg.get_config_file_content = get_config_file_content


def stage_change(key, content):
    """Almacena un cambio pendiente en session state."""
    if 'pending_changes' not in st.session_state:
        st.session_state.pending_changes = {}
    st.session_state.pending_changes[key] = content


def stage_config_change(key, content):
    """Almacena un cambio de config con ordenación alfabética automática."""
    try:
        sorted_content = sort_config_alphabetically(content)
        stage_change(key, sorted_content if sorted_content else content)
    except Exception:
        stage_change(key, content)


def apply_all_changes():
    """Escribe todos los cambios pendientes a Drive. Retorna (ok, errores)."""
    pending = st.session_state.get('pending_changes', {})
    if not pending:
        return True, []
    errors = []
    for key, content in list(pending.items()):
        try:
            if not save_config_file(key, content):
                errors.append(f"{key} (save retornó False)")
        except Exception as e:
            errors.append(f"{key} ({type(e).__name__}: {e})")
    if not errors:
        st.session_state.pending_changes = {}
        invalidate_drive_cache()
        return True, []
    # Eliminar los que sí se guardaron
    for key in list(pending.keys()):
        if not any(key in err for err in errors):
            del st.session_state.pending_changes[key]
    invalidate_drive_cache()
    return False, errors


def discard_all_changes():
    """Descarta todos los cambios pendientes."""
    st.session_state.pending_changes = {}


def filter_items(items_dict, search_term):
    if not search_term:
        return items_dict
    s = search_term.lower()
    return {k: v for k, v in items_dict.items() if s in k.lower() or s in v.lower()}


def _parse_lua_table(content):
    """Parsea una tabla Lua con formato ['key'] = 'value' → dict."""
    result = {}
    if not content:
        return result
    for m in re.finditer(r"\['([^']+)'\]\s*=\s*'([^']*)'", content):
        result[m.group(1)] = m.group(2)
    return result


def serialize_categorias(cats_dict):
    """Serializa dict de categorías → Lua."""
    max_key_len = max((len(k) for k in cats_dict), default=0)
    lines = ['Config.CATEGORIAS_CRAFTEO = {']
    for key, display in cats_dict.items():
        pad = ' ' * (max_key_len - len(key) + 4)
        lines.append(f"    ['{key}']{pad}= '{display}',")
    lines.append('}')
    return '\n'.join(lines) + '\n'


def serialize_packs(packs_dict):
    """Serializa dict de packs → Lua."""
    max_key_len = max((len(k) for k in packs_dict), default=0)
    lines = ['Config.PACKS = {']
    for key, display in packs_dict.items():
        pad = ' ' * (max_key_len - len(key) + 4)
        lines.append(f"    ['{key}']{pad}= '{display}',")
    lines.append('}')
    return '\n'.join(lines) + '\n'


def load_categorias():
    """Carga categorías desde Drive. Fallback a hardcoded."""
    content = get_config_file_content(_CATEGORIAS_KEY)
    if content:
        cats = _parse_lua_table(content)
        if cats:
            return cats
    return dict(CATEGORIAS_CRAFTEO)


def load_packs():
    """Carga packs desde Drive. Fallback a PACKS_PREDEFINIDOS."""
    content = get_config_file_content(_PACKS_KEY)
    if content:
        packs = _parse_lua_table(content)
        if packs:
            return packs
    # Convertir lista legacy a dict (clave = valor)
    return {p: p.capitalize() for p in PACKS_PREDEFINIDOS if p}


def render_apply_button(tab_key):
    """Renderiza el botón de aplicar cambios a Drive dentro de una pestaña."""
    pending = st.session_state.get('pending_changes', {})
    n = len(pending)
    if n > 0:
        st.markdown("---")
        st.warning(f"⚠️ Tienes **{n}** cambio(s) pendiente(s): {', '.join(f'config_{k}.lua' for k in pending.keys())}")
        col_apply, col_disc, _ = st.columns([2, 1, 2])
        with col_apply:
            if st.button(f"☁️ Aplicar {n} cambio(s) a Drive", key=f"apply_{tab_key}", use_container_width=True, type="primary"):
                ok, errs = apply_all_changes()
                if ok:
                    st.toast("✅ Cambios aplicados a Drive")
                    st.rerun()
                else:
                    for err in errs:
                        st.error(f"Error: {err}")
        with col_disc:
            if st.button("🗑️ Descartar", key=f"discard_{tab_key}", use_container_width=True):
                discard_all_changes()
                st.rerun()


# ============================================================================
# SESSION STATE
# ============================================================================
defaults = {
    'ingredientes': [], 'recompensas': [], 'selected_config': None,
    'modo_edicion': False, 'nombre_original': None, 'crafteo_editando': None,
    'pending_changes': {}, '_inline_edit': None,
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ============================================================================
# HEADER
# ============================================================================
import random as _rnd
_WESTERN_QUOTES = [
    "Cada receta que creas fortalece a La Hermandad.",
    "En el Viejo Oeste, el que sabe craftear sobrevive.",
    "Gracias por aportar tu granito de arena a La Hermandad.",
    "Un buen artesano deja huella en cada pieza.",
    "El trabajo honrado es la ley de esta tierra.",
    "Forjando el futuro del Oeste, una receta a la vez.",
    "Detrás de cada config hay un hermano que se curra las cosas.",
    "La Hermandad se construye con el esfuerzo de todos.",
]
_quote = _rnd.choice(_WESTERN_QUOTES)
st.markdown(f"""
<div class="main-header">
    <h1>⚒️ CRAFTSMAN'S FORGE</h1>
    <p>~ Gestor de Configs VORP Crafting — La Hermandad ~</p>
    <p style="margin-top:8px;font-size:.85rem;opacity:.7">« {_quote} »</p>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# BLOQUEO SI NO HAY CONEXIÓN A DRIVE
# ============================================================================
if not st.session_state.drive_connected:
    st.error("⚠️ **No se pudo conectar con Google Drive.** La aplicación requiere conexión a Drive para funcionar.")
    if st.session_state.get('drive_error'):
        with st.expander("🔍 Ver diagnóstico"):
            st.code(st.session_state.drive_error, language="text")
    if st.button("🔄 Reintentar conexión", use_container_width=True, key="retry_drive"):
        if _drive_available:
            drive_manager.reset_service()
        st.session_state._retry_drive = True
        st.rerun()
    st.stop()

# ============================================================================
# DATOS (cacheados en session_state, solo recargan con Refrescar/Aplicar)
# ============================================================================
_SPECIAL_KEYS = {_CATEGORIAS_KEY, _PACKS_KEY}

if '_cached_config_keys' not in st.session_state:
    _raw_keys = get_available_configs()
    st.session_state._cached_config_keys = [k for k in _raw_keys if k not in _SPECIAL_KEYS]

config_keys = sorted(
    set(st.session_state._cached_config_keys)
    | {k for k in st.session_state.get('pending_changes', {}) if k not in _SPECIAL_KEYS}
)

if '_cached_categorias' not in st.session_state:
    st.session_state._cached_categorias = load_categorias()
categorias_dict = st.session_state._cached_categorias

if '_cached_packs' not in st.session_state:
    st.session_state._cached_packs = load_packs()
packs_dict = st.session_state._cached_packs

pending = st.session_state.get('pending_changes', {})
n_pending = len(pending)

# Info bar
if n_pending > 0:
    col_info1, col_info2, col_info3, col_info4 = st.columns([2, 2, 1, 1])
else:
    col_info1, col_info2, col_info3 = st.columns([2, 2, 1])
with col_info1:
    st.success(f"☁️ Drive conectado — {len(config_keys)} configs")
with col_info2:
    st.info(f"📦 {len(ALL_ITEMS):,} items disponibles")
with col_info3:
    if st.button("🔄 Refrescar Drive", key="refresh_configs", use_container_width=True):
        invalidate_drive_cache()
        st.rerun()
if n_pending > 0:
    with col_info4:
        if st.button(f"☁️ Aplicar {n_pending} cambio(s)", key="apply_changes", use_container_width=True, type="primary"):
            ok, errs = apply_all_changes()
            if ok:
                st.toast("✅ Cambios aplicados a Drive")
                st.rerun()
            else:
                for err in errs:
                    st.error(f"Error: {err}")
    st.warning(f"⚠️ Tienes **{n_pending}** cambio(s) pendiente(s) sin subir a Drive: {', '.join(f'config_{k}.lua' for k in pending.keys())}")
    col_discard, _ = st.columns([1, 3])
    with col_discard:
        if st.button("🗑️ Descartar cambios", key="discard_changes"):
            discard_all_changes()
            st.rerun()

# ============================================================================
# TABS PRINCIPALES
# ============================================================================
tab_recetas, tab_nueva, tab_items, tab_categorias, tab_packs, tab_metabolismo, tab_editor, tab_config = st.tabs([
    "📋 Gestionar Recetas", "➕ Nueva Receta", "🧱 Items",
    "📂 Categorías", "📦 Packs", "🍖 Metabolismos", "✏️ Editor Lua", "🏭 Nuevo Config"
])


# ============================================================================
# TAB 1: GESTIONAR RECETAS
# ============================================================================
with tab_recetas:
    if not config_keys:
        st.warning("No se encontraron archivos en Drive. Crea uno en la pestaña **Nuevo Config**.")
    else:
        sel_config = st.selectbox(
            "☁️ Seleccionar Config de Drive",
            options=config_keys,
            format_func=lambda x: f"📄 config_{x}.lua — {get_job_display_name(x)}",
            key="tab1_config_select",
        )

        content = get_config_file_content(sel_config)
        if not content:
            st.error(f"No se pudo leer config_{sel_config}.lua desde Drive")
        else:
            crafteos = parse_crafting_blocks(content)
            crafteos.sort(key=lambda c: c.get('nombre', '').lower())
            comentados = parse_commented_blocks(content)

            st.markdown('<div class="card"><div class="card-title">📋 Recetas del Config</div></div>', unsafe_allow_html=True)

            # Resumen rápido
            c1, c2, c3 = st.columns(3)
            c1.metric("Recetas activas", len(crafteos))
            c2.metric("Desactivadas", len(comentados))
            c3.metric("Líneas", content.count('\n') + 1)

            # --- Crafteos activos ---
            if crafteos:
                st.markdown(f"**Recetas activas ({len(crafteos)}) — ordenadas A→Z**")
                for idx, craft in enumerate(crafteos):
                    nombre_c = craft.get('nombre', 'Sin nombre')
                    desc_c = craft.get('descripcion', '')
                    cat_c = craft.get('categoria', '')
                    pack_c = craft.get('pack', '')
                    n_ing = len(craft.get('ingredientes', []))
                    n_rew = len(craft.get('recompensas', []))
                    nivel_c = craft.get('nivel_minimo', 0)

                    label = f"⚒️ {nombre_c}"
                    if pack_c:
                        label += f"  [Pack: {pack_c}]"

                    # Expandir automáticamente si se está editando esta receta
                    _ie = st.session_state.get('_inline_edit')
                    _is_editing_this = bool(_ie and _ie.get('config') == sel_config
                                             and _ie.get('nombre_original') == nombre_c)

                    with st.expander(label, expanded=_is_editing_this):
                        col_info, col_act = st.columns([3, 1])
                        with col_info:
                            st.markdown(f"""
                            <div class="card" style="padding:12px">
                                <b>Descripción:</b> {desc_c or '—'}<br>
                                <b>Categoría:</b> {cat_c} &nbsp;|&nbsp; <b>Nivel:</b> {nivel_c}<br>
                                <b>Ingredientes:</b> {n_ing} &nbsp;|&nbsp; <b>Recompensas:</b> {n_rew}
                            </div>
                            """, unsafe_allow_html=True)

                            if craft.get('ingredientes'):
                                for ing in craft['ingredientes']:
                                    lbl = ALL_ITEMS.get(ing.get('name', ''), ing.get('name', ''))
                                    st.markdown(f'<div class="item-row"><div><span class="name">{lbl}</span> <span class="id">({ing.get("name", "")})</span></div><span class="count">x{ing.get("count", 1)}</span></div>', unsafe_allow_html=True)

                            if craft.get('recompensas'):
                                for rew in craft['recompensas']:
                                    lbl = ALL_ITEMS.get(rew.get('name', ''), rew.get('name', ''))
                                    st.markdown(f'<div class="item-row" style="border-left-color:#00d26a"><div><span class="name">🎁 {lbl}</span> <span class="id">({rew.get("name", "")})</span></div><span class="count" style="background:#00d26a">x{rew.get("count", 1)}</span></div>', unsafe_allow_html=True)

                        with col_act:
                            # Editar
                            if st.button("✏️ Editar", key=f"edit_{sel_config}_{idx}", use_container_width=True):
                                st.session_state['_inline_edit'] = {
                                    'config': sel_config,
                                    'nombre_original': nombre_c,
                                    'categoria': cat_c,
                                    'nivel_minimo': nivel_c,
                                    'pack': pack_c,
                                    'tipo': craft.get('tipo', 'item'),
                                    'animation': craft.get('animation', 'craft'),
                                    'currency_type': craft.get('currency_type', 0),
                                    'use_currency': craft.get('use_currency', False),
                                    'location': craft.get('location', 0),
                                    'job': craft.get('job', 0),
                                    'ingredientes': [dict(i) for i in craft.get('ingredientes', [])],
                                    'recompensas': [dict(r) for r in craft.get('recompensas', [])],
                                }
                                st.rerun()

                            # Desactivar
                            if st.button("🚫 Desactivar", key=f"dis_{sel_config}_{idx}", use_container_width=True):
                                new_content = comment_crafting_in_config(sel_config, nombre_c)
                                if new_content:
                                    stage_config_change(sel_config, new_content)
                                    st.success(f"'{nombre_c}' desactivado (pendiente de aplicar)")
                                    st.rerun()
                                else:
                                    st.error("Error al desactivar")

                            # Eliminar con confirmación
                            if st.button("🗑️ Eliminar", key=f"del_{sel_config}_{idx}", use_container_width=True):
                                st.session_state[f"_confirm_del_{sel_config}_{idx}"] = True

                            if st.session_state.get(f"_confirm_del_{sel_config}_{idx}"):
                                st.warning("¿Seguro?")
                                ca, cb = st.columns(2)
                                with ca:
                                    if st.button("Sí", key=f"yes_{sel_config}_{idx}", use_container_width=True):
                                        new_content = delete_crafting_from_config(sel_config, nombre_c)
                                        if new_content:
                                            stage_config_change(sel_config, new_content)
                                            st.success(f"'{nombre_c}' eliminado (pendiente de aplicar)")
                                            del st.session_state[f"_confirm_del_{sel_config}_{idx}"]
                                            st.rerun()
                                with cb:
                                    if st.button("No", key=f"no_{sel_config}_{idx}", use_container_width=True):
                                        del st.session_state[f"_confirm_del_{sel_config}_{idx}"]
                                        st.rerun()

                        # --- Formulario de edición inline ---
                        if _is_editing_this:
                            st.markdown("---")
                            st.markdown('<div class="section-label">✏️ Editar Receta</div>', unsafe_allow_html=True)

                            _ie_data = st.session_state['_inline_edit']
                            _ie_ings = _ie_data['ingredientes']
                            _ie_rews = _ie_data['recompensas']

                            # Nombre + Categoría + Nivel
                            _e1, _e2, _e3 = st.columns([3, 2, 1])
                            _ed_name = _e1.text_input("Nombre", value=_ie_data.get('nombre_original', nombre_c),
                                                       key=f"ie_nm_{sel_config}_{idx}")
                            _cat_keys = list(categorias_dict.keys())
                            _ie_cat = _ie_data.get('categoria', cat_c)
                            _ie_cat_idx = _cat_keys.index(_ie_cat) if _ie_cat in _cat_keys else 0
                            _ed_cat = _e2.selectbox("Categoría", _cat_keys, index=_ie_cat_idx,
                                                     format_func=lambda x: categorias_dict.get(x, x),
                                                     key=f"ie_ct_{sel_config}_{idx}")
                            _ed_lvl = _e3.number_input("Nivel", 0, 100,
                                                        _ie_data.get('nivel_minimo', nivel_c),
                                                        key=f"ie_lv_{sel_config}_{idx}")

                            # Ingredientes y Recompensas lado a lado
                            _ecol_ing, _ecol_rew = st.columns(2)

                            with _ecol_ing:
                                st.markdown('<div class="section-label">🧪 Ingredientes</div>', unsafe_allow_html=True)
                                for _ii, _ing in enumerate(_ie_ings):
                                    _lbl = ALL_ITEMS.get(_ing.get('name', ''), _ing.get('name', ''))
                                    _ic1, _ic2, _ic3 = st.columns([4, 2, 1])
                                    _ic1.markdown(f'<div class="item-compact"><span class="name">{_lbl}</span> <span class="id">({_ing.get("name", "")})</span></div>', unsafe_allow_html=True)
                                    _new_cnt = _ic2.number_input("x", 1, 999, _ing.get('count', 1),
                                                                  key=f"ie_ic_{sel_config}_{idx}_{_ii}",
                                                                  label_visibility="collapsed")
                                    if _ic3.button("✕", key=f"ie_di_{sel_config}_{idx}_{_ii}"):
                                        _ie_ings.pop(_ii)
                                        st.rerun()

                                # Añadir ingrediente
                                _search_ie_ing = st.text_input("🔍", placeholder="Buscar ingrediente...",
                                                                key=f"ie_si_{sel_config}_{idx}",
                                                                label_visibility="collapsed")
                                _ings_f = filter_items(ALL_ITEMS, _search_ie_ing)
                                _ai1, _ai2 = st.columns([4, 1])
                                _new_ie_ing = _ai1.selectbox("Ingrediente", [""] + list(_ings_f.keys()),
                                    format_func=lambda x: f"{_ings_f[x]} ({x})" if x else "-- Añadir --",
                                    key=f"ie_ni_{sel_config}_{idx}", label_visibility="collapsed")
                                _cnt_ie_ing = _ai2.number_input("x", 1, 999, 1,
                                                                 key=f"ie_nic_{sel_config}_{idx}",
                                                                 label_visibility="collapsed")
                                if st.button("➕ Ingrediente", key=f"ie_ai_{sel_config}_{idx}", use_container_width=True):
                                    if _new_ie_ing:
                                        _ie_ings.append({'name': _new_ie_ing, 'count': _cnt_ie_ing, 'take': True})
                                        st.rerun()

                            with _ecol_rew:
                                st.markdown('<div class="section-label">🎁 Recompensas</div>', unsafe_allow_html=True)
                                for _ri, _rew in enumerate(_ie_rews):
                                    _lbl = ALL_ITEMS.get(_rew.get('name', ''), _rew.get('name', ''))
                                    _rc1, _rc2, _rc3 = st.columns([4, 2, 1])
                                    _rc1.markdown(f'<div class="item-compact reward"><span class="name">🎁 {_lbl}</span> <span class="id">({_rew.get("name", "")})</span></div>', unsafe_allow_html=True)
                                    _new_rcnt = _rc2.number_input("x", 1, 999, _rew.get('count', 1),
                                                                   key=f"ie_rc_{sel_config}_{idx}_{_ri}",
                                                                   label_visibility="collapsed")
                                    if _rc3.button("✕", key=f"ie_dr_{sel_config}_{idx}_{_ri}"):
                                        _ie_rews.pop(_ri)
                                        st.rerun()

                                # Añadir recompensa
                                _search_ie_rew = st.text_input("🔍", placeholder="Buscar recompensa...",
                                                                key=f"ie_sr_{sel_config}_{idx}",
                                                                label_visibility="collapsed")
                                _rews_f = filter_items(ALL_ITEMS, _search_ie_rew)
                                _ar1, _ar2 = st.columns([4, 1])
                                _new_ie_rew = _ar1.selectbox("Recompensa", [""] + list(_rews_f.keys()),
                                    format_func=lambda x: f"{_rews_f[x]} ({x})" if x else "-- Añadir --",
                                    key=f"ie_nr_{sel_config}_{idx}", label_visibility="collapsed")
                                _cnt_ie_rew = _ar2.number_input("x", 1, 999, 1,
                                                                 key=f"ie_nrc_{sel_config}_{idx}",
                                                                 label_visibility="collapsed")
                                if st.button("➕ Recompensa", key=f"ie_ar_{sel_config}_{idx}", use_container_width=True):
                                    if _new_ie_rew:
                                        _ie_rews.append({'name': _new_ie_rew, 'count': _cnt_ie_rew})
                                        st.rerun()

                            # Botones Guardar / Cancelar
                            _bs, _bc = st.columns(2)
                            _can_save = bool(_ed_name and _ie_ings and _ie_rews)
                            with _bs:
                                if st.button("💾 Guardar cambios", key=f"ie_save_{sel_config}_{idx}",
                                             use_container_width=True, type="primary", disabled=not _can_save):
                                    # Leer cantidades actualizadas de los widgets
                                    _final_ings = []
                                    for _ii, _ing in enumerate(_ie_ings):
                                        _cnt = st.session_state.get(f"ie_ic_{sel_config}_{idx}_{_ii}", _ing.get('count', 1))
                                        _final_ings.append({**_ing, 'count': _cnt})
                                    _final_rews = []
                                    for _ri, _rew in enumerate(_ie_rews):
                                        _cnt = st.session_state.get(f"ie_rc_{sel_config}_{idx}_{_ri}", _rew.get('count', 1))
                                        _final_rews.append({**_rew, 'count': _cnt})

                                    _desc = ", ".join(
                                        f"{i['count']}x {ALL_ITEMS.get(i['name'], i['name'])}"
                                        + ('' if i.get('take', True) else ' (↺)')
                                        for i in _final_ings
                                    )
                                    _datos = {
                                        'nombre': _ed_name, 'descripcion': _desc,
                                        'categoria': _ed_cat, 'tipo': _ie_data.get('tipo', 'item'),
                                        'nivel_minimo': _ed_lvl,
                                        'recompensas': [{'name': r['name'], 'count': r['count']} for r in _final_rews],
                                        'ingredientes': _final_ings,
                                        'currency_type': _ie_data.get('currency_type', 0),
                                        'location': _ie_data.get('location', 0),
                                        'animation': _ie_data.get('animation', 'craft'),
                                        'use_currency': _ie_data.get('use_currency', False),
                                        'job': _ie_data.get('job', 0),
                                        'pack': _ie_data.get('pack', ''),
                                    }
                                    _code = generate_crafting_block(_datos)
                                    _new_content = replace_crafting_in_config(
                                        sel_config, _ie_data['nombre_original'], _code)
                                    if _new_content:
                                        stage_config_change(sel_config, _new_content)
                                        del st.session_state['_inline_edit']
                                        st.toast(f"✏️ '{_ed_name}' editado (pendiente de aplicar)")
                                        st.rerun()
                                    else:
                                        st.error("Error al guardar los cambios")
                            with _bc:
                                if st.button("❌ Cancelar", key=f"ie_cancel_{sel_config}_{idx}",
                                             use_container_width=True):
                                    del st.session_state['_inline_edit']
                                    st.rerun()

                        # Código raw
                        with st.expander("🔍 Ver código Lua"):
                            st.code(craft.get('_raw_block', ''), language="lua")
            else:
                st.info("No hay recetas activas en este config.")

            # --- Crafteos desactivados ---
            if comentados:
                st.markdown("---")
                st.markdown(f"**Recetas desactivadas ({len(comentados)})**")
                for idx_d, bloque_d in enumerate(comentados):
                    col_d1, col_d2 = st.columns([4, 1])
                    with col_d1:
                        st.markdown(f'<div class="item-row" style="border-left-color:#ff4444;opacity:.7"><div><span class="name">🚫 {bloque_d.get("nombre", "?")}</span> <span class="id">{bloque_d.get("descripcion", "")}</span></div></div>', unsafe_allow_html=True)
                    with col_d2:
                        if st.button("✅ Reactivar", key=f"react_{sel_config}_{idx_d}", use_container_width=True):
                            new_content = uncomment_crafting_in_config(sel_config, bloque_d.get('nombre', ''))
                            if new_content:
                                stage_config_change(sel_config, new_content)
                                st.success(f"'{bloque_d.get('nombre', '')}' reactivado (pendiente de aplicar)")
                                st.rerun()
                            else:
                                st.error("Error al reactivar la receta")

    render_apply_button("tab_recetas")


# ============================================================================
# TAB 2: NUEVA RECETA / EDITAR
# ============================================================================
_SAVE_QUOTES = [
    "¡Bien hecho, vaquero! Receta guardada.",
    "Otro día, otra receta pa' La Hermandad.",
    "El Oeste te lo agradecerá, compañero.",
    "Receta lista. El campamento estará orgulloso.",
    "¡Yeehaw! Guardado con éxito.",
]

with tab_nueva:
    if not config_keys:
        st.warning("Crea un config primero en la pestaña **Nuevo Config**.")
    else:
        # --- Fila 1: Config destino + Modo ---
        _c_dest, _c_modo = st.columns([3, 2])
        with _c_dest:
            config_destino = st.selectbox(
                "Config destino",
                options=config_keys,
                format_func=lambda x: f"config_{x}.lua — {get_job_display_name(x)}",
                key="tab2_config_dest",
            )
            job_data = get_job_metadata(config_destino)
        with _c_modo:
            modo = st.radio(
                "Modo",
                ["crear", "editar"],
                format_func=lambda x: "✨ Crear nueva" if x == "crear" else "✏️ Editar existente",
                horizontal=True, key="tab2_modo"
            )

        # Defaults
        d_nombre, d_nivel, d_tipo, d_cat_idx = "", 0, "item", None
        d_use_curr, d_curr_type, d_location = False, 0, 0
        d_animation, d_pack = "craft", ""

        if modo == "editar":
            existing = get_config_file_content(config_destino)
            if existing:
                crafteos_edit = parse_crafting_blocks(existing)
                crafteos_edit.sort(key=lambda c: c.get('nombre', '').lower())
                if crafteos_edit:
                    nombres = [c.get('nombre', '???') for c in crafteos_edit]
                    sel_idx = st.selectbox("Receta a editar", range(len(nombres)),
                                           format_func=lambda i: nombres[i], key="edit_sel")
                    cd = crafteos_edit[sel_idx]

                    nom_sel = cd.get('nombre', '')
                    if st.session_state.nombre_original != nom_sel:
                        st.session_state.nombre_original = nom_sel
                        st.session_state.crafteo_editando = cd
                        st.session_state.ingredientes = [
                            {'name': i.get('name', ''), 'label': ALL_ITEMS.get(i.get('name', ''), i.get('name', '')), 'count': i.get('count', 1), 'take': i.get('take', True)}
                            for i in cd.get('ingredientes', [])
                        ]
                        st.session_state.recompensas = [
                            {'name': r.get('name', ''), 'label': ALL_ITEMS.get(r.get('name', ''), r.get('name', '')), 'count': r.get('count', 1)}
                            for r in cd.get('recompensas', [])
                        ]
                        st.rerun()

                    d_nombre = cd.get('nombre', '')
                    d_nivel = cd.get('nivel_minimo', 0)
                    d_tipo = cd.get('tipo', 'item')
                    d_use_curr = cd.get('use_currency', False)
                    d_curr_type = cd.get('currency_type', 0)
                    d_location = cd.get('location', 0)
                    d_animation = cd.get('animation', 'craft')
                    d_pack = cd.get('pack', '')
                    loaded_cat = cd.get('categoria', '')
                    cat_keys = list(categorias_dict.keys())
                    d_cat_idx = cat_keys.index(loaded_cat) if loaded_cat in cat_keys else None
                else:
                    st.warning("No hay recetas en este config para editar.")
                    modo = "crear"
            else:
                st.warning("No se pudo leer el config desde Drive.")
                modo = "crear"

        if modo == "crear":
            st.session_state.modo_edicion = False
            st.session_state.nombre_original = None
            st.session_state.crafteo_editando = None

        # --- Fila 2: Nombre + Categoría + Tipo + Nivel (todo compacto) ---
        cat_keys = list(categorias_dict.keys())
        if d_cat_idx is not None:
            cat_idx = d_cat_idx
        else:
            default_cat = job_data['category']
            cat_idx = cat_keys.index(default_cat) if default_cat in cat_keys else 0

        tipo_keys = list(TIPOS_CRAFTEO.keys())
        tipo_idx = tipo_keys.index(d_tipo) if d_tipo in tipo_keys else 0

        _c1, _c2, _c3, _c4 = st.columns([3, 2, 2, 1])
        nombre = _c1.text_input("Nombre *", value=d_nombre, placeholder="Ej: Munición de pistola")
        categoria = _c2.selectbox("Categoría", cat_keys, index=cat_idx,
                                   format_func=lambda x: categorias_dict.get(x, x), key="cat_sel")
        tipo = _c3.selectbox("Tipo", tipo_keys, tipo_idx, format_func=lambda x: TIPOS_CRAFTEO[x])
        nivel = _c4.number_input("Nivel", 0, 100, d_nivel)

        # --- Dos columnas: Recompensas | Ingredientes ---
        col_rew, col_ing = st.columns(2)

        with col_rew:
            st.markdown('<div class="section-label">🎁 Recompensas</div>', unsafe_allow_html=True)
            search_rew = st.text_input("🔍 Buscar", placeholder="Filtrar recompensa...", key="s_rew", label_visibility="collapsed")
            items_f = filter_items(ALL_ITEMS, search_rew)

            cr1, cr2 = st.columns([4, 1])
            with cr1:
                use_manual_rew = st.checkbox("ID manual", key="m_rew")
                if use_manual_rew:
                    new_rew = st.text_input("ID", key="mr_id", placeholder="weapon_revolver", label_visibility="collapsed")
                    new_rew_label = new_rew
                else:
                    new_rew = st.selectbox("Item", [""] + list(items_f.keys()),
                        format_func=lambda x: f"{items_f[x]} ({x})" if x else "-- Seleccionar --", key="sr_sel", label_visibility="collapsed")
                    new_rew_label = items_f.get(new_rew, new_rew)
            cnt_rew = cr2.number_input("Cant", 1, 999, 1, key="cr_cnt", label_visibility="collapsed")

            if st.button("➕ Añadir recompensa", key="add_rew", use_container_width=True):
                if new_rew:
                    st.session_state.recompensas.append({'name': new_rew, 'label': new_rew_label, 'count': cnt_rew})
                    st.rerun()

            for i, r in enumerate(st.session_state.recompensas):
                c_a, c_b = st.columns([6, 1])
                c_a.markdown(f'<div class="item-compact reward"><div><span class="name">🎁 {r["label"]}</span> <span class="id">({r["name"]})</span></div><span class="count">x{r["count"]}</span></div>', unsafe_allow_html=True)
                if c_b.button("✕", key=f"dr_{i}"):
                    st.session_state.recompensas.pop(i); st.rerun()

        with col_ing:
            st.markdown('<div class="section-label">🧪 Ingredientes</div>', unsafe_allow_html=True)
            search_ing = st.text_input("🔍 Buscar", placeholder="Filtrar ingrediente...", key="s_ing", label_visibility="collapsed")
            ings_f = filter_items(ALL_ITEMS, search_ing)

            ci1, ci2 = st.columns([4, 1])
            with ci1:
                use_manual_ing = st.checkbox("ID manual", key="m_ing")
                if use_manual_ing:
                    new_ing = st.text_input("ID", key="mi_id", placeholder="gunpowder", label_visibility="collapsed")
                    new_ing_label = new_ing
                else:
                    new_ing = st.selectbox("Ingrediente", [""] + list(ings_f.keys()),
                        format_func=lambda x: f"{ings_f[x]} ({x})" if x else "-- Seleccionar --", key="si_sel", label_visibility="collapsed")
                    new_ing_label = ings_f.get(new_ing, new_ing)
            cnt_ing = ci2.number_input("Cant", 1, 999, 1, key="ci_cnt", label_visibility="collapsed")

            _ci_add, _ci_take = st.columns([3, 2])
            with _ci_add:
                if st.button("➕ Añadir ingrediente", key="add_ing", use_container_width=True):
                    if new_ing:
                        take_new_ing = st.session_state.get('take_new_ing', True)
                        st.session_state.ingredientes.append({'name': new_ing, 'label': new_ing_label, 'count': cnt_ing, 'take': take_new_ing})
                        st.rerun()
            with _ci_take:
                st.checkbox("♻️ Se consume", value=True, key="take_new_ing")

            for i, ing in enumerate(st.session_state.ingredientes):
                c_a, c_b, c_c = st.columns([5, 1, 1])
                take_val = ing.get('take', True)
                suffix = '' if take_val else ' ↺'
                c_a.markdown(f'<div class="item-compact"><div><span class="name">📦 {ing["label"]}{suffix}</span> <span class="id">({ing["name"]})</span></div><span class="count">x{ing["count"]}</span></div>', unsafe_allow_html=True)
                with c_b:
                    new_take = st.checkbox("♻️", value=take_val, key=f"take_{i}", label_visibility="collapsed")
                    if new_take != take_val:
                        st.session_state.ingredientes[i]['take'] = new_take
                        st.rerun()
                if c_c.button("✕", key=f"di_{i}"):
                    st.session_state.ingredientes.pop(i); st.rerun()

        # --- OPCIONES AVANZADAS ---
        with st.expander("⚙️ Opciones avanzadas"):
            ca1, ca2, ca3 = st.columns(3)
            with ca1:
                use_currency = st.checkbox("Cobrar dinero", d_use_curr, key="ucurr")
                if use_currency:
                    currency_type = st.selectbox("Moneda", [0, 1], d_curr_type,
                        format_func=lambda x: "💵 Cash" if x == 0 else "🪙 Gold", key="ctype")
                else:
                    currency_type = 0
            with ca2:
                location = st.number_input("Location ID", 0, value=d_location, key="loc")
                anim_keys = list(ANIMACIONES.keys())
                anim_idx = anim_keys.index(d_animation) if d_animation in anim_keys else 0
                animation = st.selectbox("Animación", anim_keys, anim_idx,
                    format_func=lambda x: ANIMACIONES[x], key="anim")
            with ca3:
                is_pack = st.checkbox("📦 Es un Pack", value=bool(d_pack), key="is_pack")
                if is_pack:
                    pack_keys = list(packs_dict.keys())
                    pack_mode = st.radio("Pack", ["Existente", "Nuevo"], horizontal=True, key="pack_mode", label_visibility="collapsed")
                    if pack_mode == "Existente" and pack_keys:
                        pack_idx = pack_keys.index(d_pack) if d_pack in pack_keys else 0
                        pack = st.selectbox("Pack", pack_keys, pack_idx,
                            format_func=lambda x: f"{packs_dict.get(x, x)} ({x})", key="pack_sel")
                    elif pack_mode == "Existente" and not pack_keys:
                        pack = st.text_input("Nuevo pack", value=d_pack, placeholder="mejicana", key="pack_new")
                    else:
                        pack = st.text_input("Nuevo pack", value="" if not d_pack else d_pack, placeholder="mejicana", key="pack_custom")
                else:
                    pack = ""

            job_override = st.text_input("Job value", value=str(job_data['job_value']),
                help='0 = cualquiera. Ej: {"medicoAR", "medicoBW"}', key="job_ov")
            if job_override.strip().startswith('{'):
                job_final = job_override.strip()
            else:
                try:
                    job_final = int(job_override)
                except ValueError:
                    job_final = 0

        # --- RESUMEN + GUARDADO (compacto, debajo del formulario) ---
        errores = []
        if not nombre: errores.append("Nombre")
        if not st.session_state.recompensas: errores.append("Recompensa")
        if not st.session_state.ingredientes: errores.append("Ingrediente")

        if errores:
            st.warning(f"⚠️ Faltan campos: **{', '.join(errores)}**")
        else:
            desc = ", ".join(
                f"{i['count']}x {i['label']}" + ('' if i.get('take', True) else ' (↺)')
                for i in st.session_state.ingredientes
            )

            datos = {
                'nombre': nombre, 'descripcion': desc, 'categoria': categoria,
                'tipo': tipo, 'nivel_minimo': nivel, 'recompensas': st.session_state.recompensas,
                'ingredientes': st.session_state.ingredientes,
                'currency_type': currency_type, 'location': location, 'animation': animation,
                'use_currency': use_currency, 'job': job_final, 'pack': pack,
            }
            codigo_lua = generate_crafting_block(datos)

            syntax_errors = validate_lua_syntax(codigo_lua)
            if syntax_errors:
                for se in syntax_errors:
                    st.error(f"⚠️ Lua: {se}")

            # Resumen compacto inline
            _rew_txt = ", ".join(f"{r['count']}x {r['label']}" for r in st.session_state.recompensas)
            _ing_txt = ", ".join(f"{i['count']}x {i['label']}" for i in st.session_state.ingredientes)
            st.markdown(f"""
            <div class="summary-compact">
                <table style="width:100%">
                    <tr><td>📄 <b>{nombre}</b></td><td>📂 {categoria}</td><td>📦 config_{config_destino}.lua</td><td>⭐ Nv.{nivel}</td></tr>
                    <tr><td colspan="2">🎁 {_rew_txt}</td><td colspan="2">🧪 {_ing_txt}</td></tr>
                </table>
            </div>
            """, unsafe_allow_html=True)

            # Botones de acción
            if modo == "editar" and st.session_state.nombre_original:
                config_editado = replace_crafting_in_config(config_destino, st.session_state.nombre_original, codigo_lua)
                if config_editado:
                    full_errors = validate_full_config(config_editado)
                    if full_errors:
                        for fe in full_errors:
                            st.caption(f"⚠️ {fe}")

                    _bc1, _bc2, _bc3 = st.columns([3, 2, 2])
                    with _bc1:
                        if st.button("💾 Guardar cambios", use_container_width=True, type="primary", key="save_edit"):
                            stage_config_change(config_destino, config_editado)
                            st.toast(f"🤠 {_rnd.choice(_SAVE_QUOTES)}")
                            st.session_state.ingredientes = []
                            st.session_state.recompensas = []
                            st.session_state.nombre_original = None
                            st.rerun()
                    with _bc2:
                        if st.button("🚫 Desactivar receta", key="disable_edit", use_container_width=True):
                            config_dis = comment_crafting_in_config(config_destino, st.session_state.nombre_original)
                            if config_dis:
                                stage_config_change(config_destino, config_dis)
                                st.toast(f"'{st.session_state.nombre_original}' desactivado")
                                st.session_state.ingredientes = []
                                st.session_state.recompensas = []
                                st.session_state.nombre_original = None
                                st.rerun()
                    with _bc3:
                        st.download_button("📥 Descargar", codigo_lua,
                            f"crafteo_{config_destino}_{nombre.lower().replace(' ', '_')}.lua", "text/plain",
                            use_container_width=True, key="dl_block")

                    with st.expander("💻 Código Lua generado"):
                        st.code(codigo_lua, language="lua")
                else:
                    st.error("No se encontró el crafteo original para reemplazar")

            else:
                existing = get_config_file_content(config_destino)
                if existing:
                    config_completo = add_crafting_to_config(config_destino, codigo_lua)
                    n_existentes = len(parse_crafting_blocks(existing))

                    full_errors = validate_full_config(config_completo)
                    if full_errors:
                        for fe in full_errors:
                            st.caption(f"⚠️ {fe}")

                    _bc1, _bc2 = st.columns([3, 2])
                    with _bc1:
                        if st.button(
                            f"💾 Guardar receta (#{n_existentes + 1} en {config_destino})",
                            use_container_width=True, type="primary", key="save_new"
                        ):  
                            stage_config_change(config_destino, config_completo)
                            st.toast(f"🤠 {_rnd.choice(_SAVE_QUOTES)}")
                            st.session_state.ingredientes = []
                            st.session_state.recompensas = []
                            st.rerun()
                    with _bc2:
                        st.download_button("📥 Descargar", codigo_lua,
                            f"crafteo_{config_destino}_{nombre.lower().replace(' ', '_')}.lua", "text/plain",
                            use_container_width=True, key="dl_block")

                    with st.expander("💻 Código Lua generado"):
                        st.code(codigo_lua, language="lua")
                else:
                    config_name = get_config_name(config_destino)
                    nuevo_config = (
                        f"Config.{config_name} = {{{codigo_lua}\n}}\n\n"
                        f"-- Agregamos a la configuración general los items de {config_destino}\n"
                        f"for _, item in pairs(Config.{config_name}) do\n"
                        f"    table.insert(Config.Crafting, item)\n"
                        f"end\n"
                    )
                    if st.button("💾 Crear config",
                                 use_container_width=True, type="primary", key="create_new"):
                        stage_change(config_destino, nuevo_config)
                        st.toast(f"🤠 {_rnd.choice(_SAVE_QUOTES)}")
                        st.rerun()

    render_apply_button("tab_nueva")


# ============================================================================
# TAB 3: ITEMS (editar lista txt y rebuild json)
# ============================================================================
with tab_items:
    st.subheader("🧱 Gestionar Items")
    st.caption("Edita la lista de IDs de items (uno por línea). Al aplicar se regenera el JSON preservando datos existentes.")

    items_txt_path = DATA_PATH / "items.txt"
    items_json_path = DATA_PATH / "items.json"

    # Cargar contenido actual del txt
    if '_items_txt_content' not in st.session_state:
        try:
            st.session_state._items_txt_content = items_txt_path.read_text(encoding='utf-8')
        except Exception:
            st.session_state._items_txt_content = ""

    edited_txt = st.text_area(
        "items.txt", value=st.session_state._items_txt_content,
        height=400, key="items_txt_editor",
        help="Un ID de item por línea. Ej: gunpowder, sarten, harina_maiz"
    )

    # Estadísticas
    current_ids = [l.strip() for l in edited_txt.splitlines() if l.strip()]
    original_ids = [l.strip() for l in st.session_state._items_txt_content.splitlines() if l.strip()]
    new_ids = set(current_ids) - set(original_ids)
    removed_ids = set(original_ids) - set(current_ids)

    ci1, ci2, ci3 = st.columns(3)
    ci1.metric("Total items", len(current_ids))
    ci2.metric("Nuevos", len(new_ids), delta=len(new_ids) if new_ids else None)
    ci3.metric("Eliminados", len(removed_ids), delta=-len(removed_ids) if removed_ids else None)

    if new_ids:
        with st.expander(f"➕ {len(new_ids)} items nuevos"):
            st.code("\n".join(sorted(new_ids)))
    if removed_ids:
        with st.expander(f"🗑️ {len(removed_ids)} items eliminados"):
            st.code("\n".join(sorted(removed_ids)))

    col_apply, col_reset = st.columns(2)
    with col_apply:
        if st.button("🔄 Aplicar y regenerar JSON", key="rebuild_items", use_container_width=True, type="primary"):
            import json as _json
            # Guardar txt
            items_txt_path.write_text(edited_txt, encoding='utf-8')
            # Rebuild: leer json existente, merge, guardar
            existing = {}
            if items_json_path.exists():
                with open(items_json_path, 'r', encoding='utf-8') as f:
                    for entry in _json.load(f).get('items', []):
                        existing[entry['item']] = entry
            items_out = []
            added = 0
            for item_id in current_ids:
                if item_id in existing:
                    items_out.append(existing[item_id])
                else:
                    items_out.append({
                        'item': item_id, 'label': item_id.replace('_', ' ').title(),
                        'limit': 250, 'can_remove': 1, 'type': 'item_standard',
                        'usable': 1, 'metadata': '{}', 'desc': '',
                        'weight': 0.5, 'degradation': 0, 'groupId': 9
                    })
                    added += 1
            with open(items_json_path, 'w', encoding='utf-8') as f:
                _json.dump({'items': items_out}, f, ensure_ascii=False, indent=2)
            # Actualizar ALL_ITEMS en memoria
            import config_items
            config_items.ALL_ITEMS = load_all_items()
            # Actualizar session state
            st.session_state._items_txt_content = edited_txt
            st.toast(f"✅ {len(items_out)} items ({added} nuevos) — JSON regenerado")
            st.rerun()
    with col_reset:
        if st.button("↩️ Descartar cambios", key="reset_items_txt", use_container_width=True):
            del st.session_state._items_txt_content
            st.rerun()


# ============================================================================
# TAB 7: CREAR NUEVO CONFIG (JOB)
# ============================================================================
with tab_config:
    st.markdown('<div class="card"><div class="card-title">🏭 Crear Nuevo Config / Job</div></div>', unsafe_allow_html=True)
    st.markdown("Crea un nuevo archivo `config_xxx.lua` en Drive para un nuevo oficio o categoría.")

    c1, c2 = st.columns(2)
    with c1:
        new_key = st.text_input("Clave del config *",
            placeholder="tienda, herrero, panaderia...",
            help="Se usará como config_<clave>.lua. Solo letras, sin espacios ni caracteres especiales.",
            key="new_cfg_key")
    with c2:
        new_display = st.text_input("Nombre para mostrar",
            placeholder="🏪 Tienda",
            help="Nombre con emoji que se mostrará en la interfaz",
            key="new_cfg_display")

    _default_lua_name = new_key.replace('_', ' ').title().replace(' ', '') if new_key else ""
    new_config_name = st.text_input("Nombre Config.X en Lua",
        value=_default_lua_name,
        placeholder="Tienda",
        help="Nombre de la variable Lua: Config.Tienda = {}",
        key="new_cfg_lua")

    new_category = st.text_input("Categoría por defecto",
        value=new_config_name if new_config_name else "",
        placeholder="Tienda",
        help="Valor de Category en cada receta de este config",
        key="new_cfg_cat")

    new_job_value = st.text_input("Job value",
        value="0",
        help='0 = cualquiera. Para jobs específicos: {"tiendero", "vendedor"}',
        key="new_cfg_job")

    # Validaciones
    key_valid = bool(new_key and re.fullmatch(r'[a-zA-Z0-9_]+', new_key))
    key_exists = new_key in (config_keys if config_keys else [])

    if new_key and not key_valid:
        st.error("La clave solo puede contener letras, números y guiones bajos, sin espacios.")
    if key_exists:
        st.error(f"Ya existe config_{new_key}.lua")

    if new_key and new_config_name:
        # Preview
        preview_content = create_empty_config(new_key, new_config_name)
        st.markdown("**Preview del archivo:**")
        st.code(preview_content, language="lua")

        can_create = key_valid and not key_exists and new_config_name
        if st.button("💾 Crear config",
                     disabled=not can_create, use_container_width=True, type="primary", key="btn_create_cfg"):
            register_config_name(new_key, new_config_name)
            stage_change(new_key, preview_content)

            if new_category and new_category not in categorias_dict:
                categorias_dict[new_category] = f"📄 {new_display or new_category}"
                st.session_state._cached_categorias = categorias_dict
                stage_change(_CATEGORIAS_KEY, serialize_categorias(categorias_dict))

            if new_key not in BASE_JOBS:
                jv = new_job_value.strip()
                if jv.startswith('{'):
                    jv_parsed = jv
                else:
                    try:
                        jv_parsed = int(jv)
                    except ValueError:
                        jv_parsed = 0
                BASE_JOBS[new_key] = {
                    'nombre': new_display or f"📄 {new_config_name}",
                    'category': new_category or new_config_name,
                    'job_value': jv_parsed,
                }

            st.success(f"✅ config_{new_key}.lua creado (pendiente de aplicar)")
            st.rerun()

    render_apply_button("tab_config")


# ============================================================================
# TAB 4: CATEGORÍAS
# ============================================================================
with tab_categorias:
    st.markdown('<div class="card"><div class="card-title">📂 Gestión de Categorías</div></div>', unsafe_allow_html=True)
    st.markdown("Administra las categorías disponibles para las recetas de crafteo. Se guardan en `config_categorias.lua` en Drive.")

    # Estado local para edición de categorías
    if 'cats_edit' not in st.session_state:
        st.session_state.cats_edit = dict(categorias_dict)

    cats_edit = st.session_state.cats_edit

    # --- Añadir nueva categoría ---
    st.markdown("### ➕ Añadir categoría")
    col_nk, col_nd, col_nb = st.columns([2, 3, 1])
    with col_nk:
        new_cat_key = st.text_input("Clave *", placeholder="CocinaPremium", key="new_cat_key",
                                     help="Identificador interno (sin espacios). Ej: CocinaPremium")
    with col_nd:
        new_cat_display = st.text_input("Nombre para mostrar *", placeholder="👨‍🍳 Cocina Premium", key="new_cat_display",
                                         help="Nombre con emoji que se mostrará en la interfaz")
    with col_nb:
        st.write(""); st.write("")
        add_disabled = not (new_cat_key and new_cat_display and new_cat_key.strip())
        if st.button("➕ Añadir", key="add_cat", use_container_width=True, disabled=add_disabled):
            k = new_cat_key.strip()
            if k in cats_edit:
                st.error(f"La clave '{k}' ya existe.")
            else:
                cats_edit[k] = new_cat_display.strip()
                st.session_state.cats_edit = cats_edit
                st.rerun()

    # --- Lista de categorías existentes ---
    st.markdown("### 📋 Categorías actuales")
    if not cats_edit:
        st.info("No hay categorías definidas.")
    else:
        for idx, (cat_key, cat_display) in enumerate(list(cats_edit.items())):
            col_k, col_d, col_del = st.columns([2, 4, 1])
            with col_k:
                new_display = st.text_input("Nombre", value=cat_display, key=f"cat_d_{idx}", label_visibility="collapsed")
                if new_display != cat_display:
                    cats_edit[cat_key] = new_display
                    st.session_state.cats_edit = cats_edit
            with col_d:
                st.markdown(f"`{cat_key}`")
            with col_del:
                if st.button("🗑️", key=f"del_cat_{idx}"):
                    del cats_edit[cat_key]
                    st.session_state.cats_edit = cats_edit
                    st.rerun()

    # --- Botón guardar categorías ---
    st.markdown("---")
    cats_changed = cats_edit != categorias_dict
    col_save, col_reset, _ = st.columns([2, 1, 2])
    with col_save:
        if st.button(
            "💾 Guardar categorías" if cats_changed else "Sin cambios",
            disabled=not cats_changed, use_container_width=True, type="primary", key="save_cats"
        ):
            stage_change(_CATEGORIAS_KEY, serialize_categorias(cats_edit))
            st.session_state._cached_categorias = dict(cats_edit)
            st.success("Categorías guardadas (pendiente de aplicar a Drive)")
            st.rerun()
    with col_reset:
        if st.button("↩️ Revertir", disabled=not cats_changed, use_container_width=True, key="reset_cats"):
            st.session_state.cats_edit = dict(categorias_dict)
            st.rerun()

    render_apply_button("tab_categorias")


# ============================================================================
# TAB 5: PACKS
# ============================================================================
with tab_packs:
    st.markdown('<div class="card"><div class="card-title">📦 Gestión de Packs</div></div>', unsafe_allow_html=True)
    st.markdown("Administra los packs disponibles para agrupar recetas. Se guardan en `config_packs.lua` en Drive.")

    # Estado local para edición de packs
    if 'packs_edit' not in st.session_state:
        st.session_state.packs_edit = dict(packs_dict)

    packs_edit = st.session_state.packs_edit

    # --- Añadir nuevo pack ---
    st.markdown("### ➕ Añadir pack")
    col_pk, col_pd, col_pb = st.columns([2, 3, 1])
    with col_pk:
        new_pack_key = st.text_input("Clave *", placeholder="mejicana", key="new_pack_key",
                                      help="Identificador interno del pack. Ej: mejicana")
    with col_pd:
        new_pack_display = st.text_input("Nombre para mostrar *", placeholder="Mejicana", key="new_pack_display",
                                          help="Nombre legible que se mostrará en la interfaz")
    with col_pb:
        st.write(""); st.write("")
        add_pack_disabled = not (new_pack_key and new_pack_display and new_pack_key.strip())
        if st.button("➕ Añadir", key="add_pack", use_container_width=True, disabled=add_pack_disabled):
            pk = new_pack_key.strip()
            if pk in packs_edit:
                st.error(f"El pack '{pk}' ya existe.")
            else:
                packs_edit[pk] = new_pack_display.strip()
                st.session_state.packs_edit = packs_edit
                st.rerun()

    # --- Lista de packs existentes ---
    st.markdown("### 📋 Packs actuales")
    if not packs_edit:
        st.info("No hay packs definidos.")
    else:
        for idx, (pack_key, pack_display) in enumerate(list(packs_edit.items())):
            col_k, col_d, col_del = st.columns([2, 4, 1])
            with col_k:
                new_pd = st.text_input("Nombre", value=pack_display, key=f"pack_d_{idx}", label_visibility="collapsed")
                if new_pd != pack_display:
                    packs_edit[pack_key] = new_pd
                    st.session_state.packs_edit = packs_edit
            with col_d:
                st.markdown(f"`{pack_key}`")
            with col_del:
                if st.button("🗑️", key=f"del_pack_{idx}"):
                    del packs_edit[pack_key]
                    st.session_state.packs_edit = packs_edit
                    st.rerun()

    # --- Botón guardar packs ---
    st.markdown("---")
    packs_changed = packs_edit != packs_dict
    col_save_p, col_reset_p, _ = st.columns([2, 1, 2])
    with col_save_p:
        if st.button(
            "💾 Guardar packs" if packs_changed else "Sin cambios",
            disabled=not packs_changed, use_container_width=True, type="primary", key="save_packs"
        ):
            stage_change(_PACKS_KEY, serialize_packs(packs_edit))
            st.session_state._cached_packs = dict(packs_edit)
            st.success("Packs guardados (pendiente de aplicar a Drive)")
            st.rerun()
    with col_reset_p:
        if st.button("↩️ Revertir", disabled=not packs_changed, use_container_width=True, key="reset_packs"):
            st.session_state.packs_edit = dict(packs_dict)
            st.rerun()

    render_apply_button("tab_packs")


# ============================================================================
# FUNCIÓN AUXILIAR: Formulario de metabolismo (definida antes de usarse)
# ============================================================================
def _render_metabolism_form(item_data: dict, form_key: str, metab_content: str, is_new: bool = False,
                           known_anims: list[str] | None = None, known_props: list[str] | None = None):
    """Renderiza el formulario de edición/creación de metabolismo."""
    prefix = f"mf_{form_key}"
    if known_anims is None:
        known_anims = ['eat', 'drink', 'coffee', 'smoke', 'medicine', 'stew', 'eatCan']
    if known_props is None:
        known_props = []

    # --- Item ID y Nombre ---
    _fc1, _fc2 = st.columns(2)
    with _fc1:
        if is_new:
            _use_manual = st.checkbox("ID manual", key=f"{prefix}_manual")
            if _use_manual:
                item_id = st.text_input("ID del item *", value=item_data.get('item_id', ''),
                                         placeholder="mi_nuevo_item", key=f"{prefix}_id")
            else:
                _m_search = st.text_input("🔍 Buscar item", placeholder="Buscar item...",
                                           key=f"{prefix}_search")
                _m_items = filter_items(ALL_ITEMS, _m_search)
                item_id = st.selectbox("Item *", [""] + list(_m_items.keys()),
                    format_func=lambda x: f"{_m_items[x]} ({x})" if x else "-- Seleccionar item --",
                    key=f"{prefix}_item_sel")
        else:
            item_id = item_data.get('item_id', '')
            st.text_input("ID del item", value=item_id, disabled=True, key=f"{prefix}_id")

    with _fc2:
        default_name = item_data.get('name', '') or ALL_ITEMS.get(item_id, item_id.replace('_', ' ').title() if item_id else '')
        item_name = st.text_input("Nombre para mostrar *", value=default_name,
                                   placeholder="Nombre del item", key=f"{prefix}_name")

    # --- Stats principales ---
    st.markdown('<div class="section-label">📊 Stats Base</div>', unsafe_allow_html=True)
    _sc1, _sc2, _sc3, _sc4 = st.columns(4)
    hunger = _sc1.number_input("🍗 Hambre", min_value=0.0, max_value=100.0,
                                value=float(item_data.get('hunger', 0.0)), step=0.5, key=f"{prefix}_hunger")
    thirst = _sc2.number_input("💧 Sed", min_value=0.0, max_value=100.0,
                                value=float(item_data.get('thirst', 0.0)), step=0.5, key=f"{prefix}_thirst")
    stress = _sc3.number_input("😰 Estrés", min_value=-100.0, max_value=100.0,
                                value=float(item_data.get('stress', 0.0)), step=1.0, key=f"{prefix}_stress",
                                help="Negativo = reduce estrés")
    urine = _sc4.number_input("🚽 Orina", min_value=0.0, max_value=100.0,
                               value=float(item_data.get('urine', 0.0)), step=1.0, key=f"{prefix}_urine")

    # --- Opciones especiales ---
    _so1, _so2 = st.columns(2)
    keep_when_use = _so1.checkbox("🔒 Mantener al usar (keepWhenUse)", value=item_data.get('keepWhenUse', False),
                                   key=f"{prefix}_keep")
    snake_antidote = _so2.checkbox("🐍 Antídoto de serpiente", value=item_data.get('snakePoisonAntidote', False),
                                    key=f"{prefix}_antidote")

    # --- Temperatura ---
    has_temp = st.checkbox("🌡️ Modificador de temperatura", value=item_data.get('has_tempModifier', False),
                            key=f"{prefix}_has_temp")
    temp_value = 0.0
    temp_duration = 25000
    if has_temp:
        _tc1, _tc2 = st.columns(2)
        temp_value = _tc1.number_input("Valor (- frío, + calor)", min_value=-20.0, max_value=20.0,
                                        value=float(item_data.get('tempModifier_value', 0.0)), step=1.0,
                                        key=f"{prefix}_temp_val")
        temp_duration = _tc2.number_input("Duración (ms)", min_value=1000, max_value=300000,
                                           value=int(item_data.get('tempModifier_duration', 25000)), step=5000,
                                           key=f"{prefix}_temp_dur")

    # --- Efectos en Jugador ---
    has_player = st.checkbox("👤 Efectos en jugador", value=item_data.get('has_player', False),
                              key=f"{prefix}_has_player")
    p_health = 0.0
    p_stamina = 0.0
    p_health_outer = 0.0
    p_boost_health = [0, 0]
    p_boost_stamina = [0, 0]
    if has_player:
        _pc1, _pc2, _pc3 = st.columns(3)
        p_health = _pc1.number_input("❤️ Health Core", min_value=0.0, max_value=100.0,
                                      value=float(item_data.get('player_healthCore', 0.0)), step=1.0,
                                      key=f"{prefix}_p_hc")
        p_stamina = _pc2.number_input("⚡ Stamina Core", min_value=0.0, max_value=100.0,
                                       value=float(item_data.get('player_staminaCore', 0.0)), step=0.5,
                                       key=f"{prefix}_p_sc")
        p_health_outer = _pc3.number_input("❤️ Health Outer", min_value=0.0, max_value=100.0,
                                            value=float(item_data.get('player_healthOuter', 0.0)), step=1.0,
                                            key=f"{prefix}_p_ho")
        with st.expander("⏱️ Boosts de jugador (duración en segundos)"):
            _pb1, _pb2, _pb3, _pb4 = st.columns(4)
            bh = item_data.get('player_boostHealth', [0, 0])
            bs = item_data.get('player_boostStamina', [0, 0])
            p_boost_health = [
                _pb1.number_input("Boost Health inner", 0, 600, int(bh[0]), key=f"{prefix}_pbhi"),
                _pb2.number_input("Boost Health outer", 0, 600, int(bh[1]), key=f"{prefix}_pbho"),
            ]
            p_boost_stamina = [
                _pb3.number_input("Boost Stamina inner", 0, 600, int(bs[0]), key=f"{prefix}_pbsi"),
                _pb4.number_input("Boost Stamina outer", 0, 600, int(bs[1]), key=f"{prefix}_pbso"),
            ]

    # --- Efectos en Caballo ---
    has_horse = st.checkbox("🐴 Efectos en caballo", value=item_data.get('has_horse', False),
                             key=f"{prefix}_has_horse")
    h_health = 0.0
    h_stamina = 0.0
    h_health_outer = 0.0
    h_boost_health = [0, 0]
    h_boost_stamina = [0, 0]
    if has_horse:
        _hc1, _hc2, _hc3 = st.columns(3)
        h_health = _hc1.number_input("❤️ Horse Health Core", min_value=0.0, max_value=100.0,
                                      value=float(item_data.get('horse_healthCore', 0.0)), step=1.0,
                                      key=f"{prefix}_h_hc")
        h_stamina = _hc2.number_input("⚡ Horse Stamina Core", min_value=0.0, max_value=100.0,
                                       value=float(item_data.get('horse_staminaCore', 0.0)), step=0.5,
                                       key=f"{prefix}_h_sc")
        h_health_outer = _hc3.number_input("❤️ Horse Health Outer", min_value=0.0, max_value=100.0,
                                            value=float(item_data.get('horse_healthOuter', 0.0)), step=1.0,
                                            key=f"{prefix}_h_ho")
        with st.expander("⏱️ Boosts de caballo (duración en segundos)"):
            _hb1, _hb2, _hb3, _hb4 = st.columns(4)
            hbh = item_data.get('horse_boostHealth', [0, 0])
            hbs = item_data.get('horse_boostStamina', [0, 0])
            h_boost_health = [
                _hb1.number_input("Boost Health inner", 0, 600, int(hbh[0]), key=f"{prefix}_hbhi"),
                _hb2.number_input("Boost Health outer", 0, 600, int(hbh[1]), key=f"{prefix}_hbho"),
            ]
            h_boost_stamina = [
                _hb3.number_input("Boost Stamina inner", 0, 600, int(hbs[0]), key=f"{prefix}_hbsi"),
                _hb4.number_input("Boost Stamina outer", 0, 600, int(hbs[1]), key=f"{prefix}_hbso"),
            ]

    # --- Animación / Efectos visuales ---
    st.markdown('<div class="section-label">🎬 Animación y Efectos</div>', unsafe_allow_html=True)
    has_effects = st.checkbox("Activar efectos/animación", value=item_data.get('has_effects', True),
                               key=f"{prefix}_has_fx")
    anim_name = 'eat'
    fx_prop = ''
    fx_screen = ''
    fx_buff_name = ''
    fx_buff_dur = 0
    if has_effects:
        _ac1, _ac2 = st.columns(2)
        cur_anim = item_data.get('effects_animationName', 'eat')
        anim_options = list(known_anims) if known_anims else []
        if cur_anim and cur_anim not in anim_options:
            anim_options.append(cur_anim)
        anim_options_display = anim_options + ['✏️ Personalizado...']
        anim_sel_idx = anim_options.index(cur_anim) if cur_anim in anim_options else 0
        anim_sel = _ac1.selectbox("Animación", anim_options_display, index=anim_sel_idx,
                                   key=f"{prefix}_anim")
        if anim_sel == '✏️ Personalizado...':
            anim_name = _ac1.text_input("Nombre de animación", value=cur_anim,
                                         placeholder="nombre_animacion", key=f"{prefix}_anim_custom")
        else:
            anim_name = anim_sel

        cur_prop = item_data.get('effects_prop', '')
        prop_options = [''] + (list(known_props) if known_props else [])
        if cur_prop and cur_prop not in prop_options:
            prop_options.append(cur_prop)
        prop_options_display = prop_options + ['✏️ Personalizado...']
        prop_sel_idx = prop_options.index(cur_prop) if cur_prop in prop_options else 0
        prop_sel = _ac2.selectbox("Prop (modelo)", prop_options_display, index=prop_sel_idx,
                                   format_func=lambda x: '— Ninguno —' if x == '' else x,
                                   key=f"{prefix}_prop")
        if prop_sel == '✏️ Personalizado...':
            fx_prop = _ac2.text_input("ID del prop", value=cur_prop, placeholder="P_MODEL_X",
                                       key=f"{prefix}_prop_custom")
        else:
            fx_prop = prop_sel

        with st.expander("🎭 Efectos avanzados"):
            fx_screen = st.text_input("Screen FX", value=item_data.get('effects_screenFx', ''),
                                       placeholder="Nombre del efecto de pantalla", key=f"{prefix}_sfx")
            _bf1, _bf2 = st.columns(2)
            fx_buff_name = _bf1.text_input("Buff Effect nombre", value=item_data.get('effects_buffEffect_name', ''),
                                            placeholder="PlayerBoostBuff", key=f"{prefix}_buff_n")
            fx_buff_dur = _bf2.number_input("Buff duración (s)", 0, 600,
                                             int(item_data.get('effects_buffEffect_duration', 0)),
                                             key=f"{prefix}_buff_d")

    # --- Borrachera ---
    has_drunk = st.checkbox("🍺 Borrachera", value=item_data.get('has_drunk', False), key=f"{prefix}_has_drunk")
    drunk_min = 0
    drunk_max = 0
    drunk_intensity = 0
    if has_drunk:
        _dc1, _dc2, _dc3 = st.columns(3)
        drunk_min = _dc1.number_input("Mín. bebidas", 0, 20, int(item_data.get('drunk_min', 1)),
                                       key=f"{prefix}_d_min")
        drunk_max = _dc2.number_input("Máx. bebidas", 0, 20, int(item_data.get('drunk_max', 4)),
                                       key=f"{prefix}_d_max")
        drunk_intensity = _dc3.number_input("Intensidad", 0, 10, int(item_data.get('drunk_intensity', 1)),
                                             key=f"{prefix}_d_int")

    # --- Return Items ---
    has_ri = st.checkbox("♻️ Items devueltos al consumir", value=item_data.get('has_returnItems', False),
                          key=f"{prefix}_has_ri")
    return_items = list(item_data.get('returnItems', []))
    if has_ri:
        for ri_idx, ri in enumerate(return_items):
            _ri1, _ri2, _ri3 = st.columns([4, 2, 1])
            _ri1.text_input("Item", value=ri['name'], key=f"{prefix}_ri_n_{ri_idx}", disabled=True,
                            label_visibility="collapsed")
            _ri2.number_input("x", 1, 99, ri['amount'], key=f"{prefix}_ri_a_{ri_idx}",
                              label_visibility="collapsed")
            if _ri3.button("✕", key=f"{prefix}_ri_d_{ri_idx}"):
                return_items.pop(ri_idx)
                st.rerun()
        _ri_s1, _ri_s2 = st.columns([4, 1])
        _ri_search = st.text_input("🔍", placeholder="Buscar item a devolver...",
                                    key=f"{prefix}_ri_search", label_visibility="collapsed")
        _ri_items = filter_items(ALL_ITEMS, _ri_search)
        _new_ri = _ri_s1.selectbox("Devolver", [""] + list(_ri_items.keys()),
            format_func=lambda x: f"{_ri_items[x]} ({x})" if x else "-- Seleccionar --",
            key=f"{prefix}_ri_new", label_visibility="collapsed")
        _new_ri_amt = _ri_s2.number_input("x", 1, 99, 1, key=f"{prefix}_ri_amt", label_visibility="collapsed")
        if st.button("➕ Añadir item devuelto", key=f"{prefix}_ri_add", use_container_width=True):
            if _new_ri:
                return_items.append({'name': _new_ri, 'amount': _new_ri_amt})
                st.rerun()

    # --- Required Items ---
    has_rq = st.checkbox("🔑 Items requeridos para usar", value=item_data.get('has_requiredItems', False),
                          key=f"{prefix}_has_rq")
    required_items = list(item_data.get('requiredItems', []))
    if has_rq:
        for rq_idx, rq in enumerate(required_items):
            _rq1, _rq2, _rq3 = st.columns([4, 2, 1])
            _rq1.text_input("Item", value=rq['name'], key=f"{prefix}_rq_n_{rq_idx}", disabled=True,
                            label_visibility="collapsed")
            _rq2.number_input("x", 1, 99, rq['amount'], key=f"{prefix}_rq_a_{rq_idx}",
                              label_visibility="collapsed")
            if _rq3.button("✕", key=f"{prefix}_rq_d_{rq_idx}"):
                required_items.pop(rq_idx)
                st.rerun()
        _rq_search = st.text_input("🔍", placeholder="Buscar item requerido...",
                                    key=f"{prefix}_rq_search", label_visibility="collapsed")
        _rq_items = filter_items(ALL_ITEMS, _rq_search)
        _rq_s1, _rq_s2 = st.columns([4, 1])
        _new_rq = _rq_s1.selectbox("Requerir", [""] + list(_rq_items.keys()),
            format_func=lambda x: f"{_rq_items[x]} ({x})" if x else "-- Seleccionar --",
            key=f"{prefix}_rq_new", label_visibility="collapsed")
        _new_rq_amt = _rq_s2.number_input("x", 1, 99, 1, key=f"{prefix}_rq_amt", label_visibility="collapsed")
        if st.button("➕ Añadir item requerido", key=f"{prefix}_rq_add", use_container_width=True):
            if _new_rq:
                required_items.append({'name': _new_rq, 'amount': _new_rq_amt})
                st.rerun()

    # --- Opciones extra ---
    with st.expander("⚙️ Opciones extra"):
        _oe1, _oe2 = st.columns(2)
        cooldown = _oe1.number_input("Cooldown (ms, 0 = sin cooldown)", 0, 600000,
                                      int(item_data.get('cooldown', 0)), step=1000, key=f"{prefix}_cd")
        use_on_mount = _oe2.checkbox("🐴 Usar montado", value=item_data.get('useOnMount', True),
                                      key=f"{prefix}_mount")
        has_ca = st.checkbox("⚙️ ClientAction personalizado", value=item_data.get('has_clientAction', False),
                              key=f"{prefix}_has_ca")
        ca_code = ''
        if has_ca:
            ca_code = st.text_area("Código ClientAction", value=item_data.get('clientAction_code', ''),
                                    height=100, key=f"{prefix}_ca_code",
                                    placeholder="TriggerEvent('mi_evento')")

    # --- Recopilar datos y generar ---
    final_ri = []
    for ri_idx, ri in enumerate(return_items):
        amt = st.session_state.get(f"{prefix}_ri_a_{ri_idx}", ri['amount'])
        final_ri.append({'name': ri['name'], 'amount': amt})
    final_rq = []
    for rq_idx, rq in enumerate(required_items):
        amt = st.session_state.get(f"{prefix}_rq_a_{rq_idx}", rq['amount'])
        final_rq.append({'name': rq['name'], 'amount': amt})

    datos = {
        'item_id': item_id,
        'name': item_name,
        'hunger': hunger,
        'thirst': thirst,
        'stress': stress,
        'urine': urine,
        'keepWhenUse': keep_when_use,
        'snakePoisonAntidote': snake_antidote,
        'has_tempModifier': has_temp,
        'tempModifier_value': temp_value,
        'tempModifier_duration': temp_duration,
        'has_player': has_player,
        'player_healthCore': p_health,
        'player_staminaCore': p_stamina,
        'player_healthOuter': p_health_outer,
        'player_boostHealth': p_boost_health,
        'player_boostStamina': p_boost_stamina,
        'has_horse': has_horse,
        'horse_healthCore': h_health,
        'horse_staminaCore': h_stamina,
        'horse_healthOuter': h_health_outer,
        'horse_boostHealth': h_boost_health,
        'horse_boostStamina': h_boost_stamina,
        'has_effects': has_effects,
        'effects_enabled': True,
        'effects_animationName': anim_name,
        'effects_prop': fx_prop,
        'effects_screenFx': fx_screen,
        'effects_buffEffect_name': fx_buff_name,
        'effects_buffEffect_duration': fx_buff_dur,
        'has_drunk': has_drunk,
        'drunk_min': drunk_min,
        'drunk_max': drunk_max,
        'drunk_intensity': drunk_intensity,
        'has_returnItems': has_ri,
        'returnItems': final_ri,
        'has_requiredItems': has_rq,
        'requiredItems': final_rq,
        'cooldown': cooldown,
        'useOnMount': use_on_mount,
        'has_clientAction': has_ca,
        'clientAction_code': ca_code,
    }

    can_save = bool(item_id and item_name)
    if not can_save:
        st.warning("⚠️ Falta el ID del item y/o nombre.")

    if item_id:
        code_preview = _lmg.generate_metabolism_block(datos)
        with st.expander("💻 Preview código Lua"):
            st.code(code_preview, language="lua")

    _bsave, _bcancel = st.columns(2)
    with _bsave:
        if st.button("💾 Guardar", key=f"{prefix}_save", use_container_width=True, type="primary",
                      disabled=not can_save):
            code = _lmg.generate_metabolism_block(datos)
            if is_new:
                new_content = _lmg.add_item_to_config(metab_content, code)
            else:
                new_content = _lmg.replace_item_in_config(metab_content, item_data.get('item_id', ''), code)
            if new_content:
                st.session_state._metab_pending = new_content
                st.session_state.pop('_metab_editing', None)
                st.toast(f"✅ '{item_name}' {'creado' if is_new else 'editado'} (pendiente)")
                st.rerun()
            else:
                st.error("Error al procesar el cambio")
    with _bcancel:
        if st.button("❌ Cancelar", key=f"{prefix}_cancel", use_container_width=True):
            st.session_state.pop('_metab_editing', None)
            st.rerun()


# ============================================================================
# TAB 6: METABOLISMOS (configurar qué hace cada item al consumirlo)
# ============================================================================
with tab_metabolismo:
    st.markdown('<div class="card"><div class="card-title">🍖 Metabolismos — Configurar Items Consumibles</div></div>', unsafe_allow_html=True)
    st.markdown("Configura lo que hacen los items al consumirlos: hambre, sed, estrés, efectos, animaciones, etc. Se guarda en `usables_lhr.cfg.lua` en Drive.")

    # --- Cargar contenido del archivo de metabolismos ---
    if '_metab_content' not in st.session_state:
        st.session_state._metab_content = _lmg.read_metabolism_file()

    metab_content = st.session_state.get('_metab_pending') or st.session_state._metab_content

    # --- Botones de aplicar/descartar cambios de metabolismo (arriba) ---
    metab_pending = st.session_state.get('_metab_pending')
    if metab_pending and metab_pending != st.session_state._metab_content:
        st.warning("⚠️ Tienes cambios pendientes en metabolismos sin subir a Drive.")
        col_ma, col_md, _ = st.columns([2, 1, 2])
        with col_ma:
            if st.button("☁️ Aplicar cambios a Drive", key="metab_apply", use_container_width=True, type="primary"):
                ok = _lmg.save_metabolism_file(metab_pending)
                if ok:
                    st.session_state._metab_content = metab_pending
                    st.session_state.pop('_metab_pending', None)
                    st.toast("✅ Metabolismos guardados en Drive")
                    st.rerun()
                else:
                    st.error("Error al guardar en Drive")
        with col_md:
            if st.button("🗑️ Descartar", key="metab_discard", use_container_width=True):
                st.session_state.pop('_metab_pending', None)
                st.rerun()

    render_apply_button("tab_metabolismo")

    @st.cache_data(show_spinner=False)
    def _cached_parse_metabolism(content: str):
        items = _lmg.parse_metabolism_items(content)
        anims = _lmg.extract_unique_animations(items)
        props = _lmg.extract_unique_props(items)
        return items, anims, props

    if not metab_content:
        st.error("No se pudo leer `usables_lhr.cfg.lua` desde Drive.")
    else:
        metab_items, _known_anims, _known_props = _cached_parse_metabolism(metab_content)
        active_items = [i for i in metab_items if not i['commented']]
        commented_items = [i for i in metab_items if i['commented']]
        active_items.sort(key=lambda x: x['item_id'].lower())
        commented_items.sort(key=lambda x: x['item_id'].lower())

        # Sub-tabs: Gestionar existentes | Crear nuevo
        mtab_gestionar, mtab_nuevo = st.tabs(["📋 Gestionar existentes", "➕ Crear nuevo"])

        # ==========================
        # SUB-TAB: GESTIONAR EXISTENTES
        # ==========================
        with mtab_gestionar:
            # Resumen
            mc1, mc2, mc3 = st.columns(3)
            mc1.metric("Items activos", len(active_items))
            mc2.metric("Desactivados", len(commented_items))
            mc3.metric("Total", len(metab_items))

            # Buscador
            metab_search = st.text_input("🔍 Buscar item", placeholder="Escribe el ID o nombre del item...",
                                          key="metab_search")
            if metab_search:
                s = metab_search.lower()
                active_items = [i for i in active_items if s in i['item_id'].lower() or s in i.get('name', '').lower()]
                commented_items = [i for i in commented_items if s in i['item_id'].lower() or s in i.get('name', '').lower()]

            # --- Items activos ---
            if active_items:
                st.markdown(f"**Items activos ({len(active_items)})**")
                for idx, item in enumerate(active_items):
                    _item_id = item['item_id']
                    _item_name = item.get('name', _item_id)
                    _anim = item.get('effects_animationName', 'eat')
                    _hunger = item.get('hunger', 0)
                    _thirst = item.get('thirst', 0)
                    _stress = item.get('stress', 0)

                    _label = f"{_item_name} ({_item_id}) — {_anim}"
                    _is_editing = st.session_state.get('_metab_editing') == _item_id

                    with st.expander(_label, expanded=_is_editing):
                        # Vista resumen
                        col_stats, col_acts = st.columns([4, 1])
                        with col_stats:
                            s1, s2, s3, s4 = st.columns(4)
                            s1.metric("🍗 Hambre", f"{_hunger}")
                            s2.metric("💧 Sed", f"{_thirst}")
                            s3.metric("😰 Estrés", f"{_stress}")
                            s4.metric("🎬 Anim.", _anim)

                            # Info adicional resumida
                            extras = []
                            if item.get('has_tempModifier'):
                                tv = item.get('tempModifier_value', 0)
                                extras.append(f"🌡️ Temp: {'+' if tv > 0 else ''}{tv}")
                            if item.get('player_staminaCore', 0):
                                extras.append(f"⚡ Stamina: {item['player_staminaCore']}")
                            if item.get('player_healthCore', 0):
                                extras.append(f"❤️ Salud: {item['player_healthCore']}")
                            if item.get('has_returnItems') and item.get('returnItems'):
                                ri_txt = ", ".join(f"{r['amount']}x {r['name']}" for r in item['returnItems'])
                                extras.append(f"♻️ Devuelve: {ri_txt}")
                            if item.get('effects_prop'):
                                extras.append(f"🎮 Prop: {item['effects_prop']}")
                            if item.get('keepWhenUse'):
                                extras.append("🔒 Se mantiene al usar")
                            if item.get('snakePoisonAntidote'):
                                extras.append("🐍 Antídoto de serpiente")
                            if extras:
                                st.caption(" · ".join(extras))

                        with col_acts:
                            if st.button("✏️ Editar", key=f"metab_edit_{idx}", use_container_width=True):
                                st.session_state._metab_editing = _item_id
                            if st.button("🚫 Desactivar", key=f"metab_dis_{idx}", use_container_width=True):
                                new_content = _lmg.comment_item_in_config(metab_content, _item_id)
                                if new_content:
                                    st.session_state._metab_pending = new_content
                                    st.toast(f"'{_item_name}' desactivado (pendiente)")
                                    st.rerun()
                            if st.button("🗑️ Eliminar", key=f"metab_del_{idx}", use_container_width=True):
                                st.session_state[f"_metab_confirm_del_{idx}"] = True
                            if st.session_state.get(f"_metab_confirm_del_{idx}"):
                                st.warning("¿Seguro?")
                                _da, _db = st.columns(2)
                                with _da:
                                    if st.button("Sí", key=f"metab_yd_{idx}", use_container_width=True):
                                        new_content = _lmg.delete_item_from_config(metab_content, _item_id)
                                        if new_content:
                                            st.session_state._metab_pending = new_content
                                            del st.session_state[f"_metab_confirm_del_{idx}"]
                                            st.toast(f"'{_item_name}' eliminado (pendiente)")
                                            st.rerun()
                                with _db:
                                    if st.button("No", key=f"metab_nd_{idx}", use_container_width=True):
                                        del st.session_state[f"_metab_confirm_del_{idx}"]
                                        st.rerun()

                        # --- Formulario de edición inline ---
                        if _is_editing:
                            st.markdown("---")
                            st.markdown('<div class="section-label">✏️ Editar Metabolismo</div>', unsafe_allow_html=True)
                            _render_metabolism_form(item, f"edit_{idx}", metab_content, is_new=False,
                                                     known_anims=_known_anims, known_props=_known_props)
            else:
                st.info("No hay items activos" + (" con ese filtro." if metab_search else "."))

            # --- Items desactivados ---
            if commented_items:
                st.markdown("---")
                st.markdown(f"**Items desactivados ({len(commented_items)})**")
                for idx_c, item_c in enumerate(commented_items):
                    col_d1, col_d2 = st.columns([4, 1])
                    with col_d1:
                        st.markdown(f'<div class="item-row" style="border-left-color:#ff4444;opacity:.7"><div><span class="name">🚫 {item_c.get("name", "?")} ({item_c["item_id"]})</span></div></div>', unsafe_allow_html=True)
                    with col_d2:
                        if st.button("✅ Reactivar", key=f"metab_react_{idx_c}", use_container_width=True):
                            new_content = _lmg.uncomment_item_in_config(metab_content, item_c['item_id'])
                            if new_content:
                                st.session_state._metab_pending = new_content
                                st.toast(f"'{item_c.get('name', item_c['item_id'])}' reactivado (pendiente)")
                                st.rerun()

        # ==========================
        # SUB-TAB: CREAR NUEVO
        # ==========================
        with mtab_nuevo:
            st.markdown("Crea un metabolismo para un item que no lo tenga configurado aún.")
            _render_metabolism_form({}, "new_0", metab_content, is_new=True,
                                     known_anims=_known_anims, known_props=_known_props)


# ============================================================================
# TAB 7: EDITOR LUA (lectura/escritura directa en Drive)
# ============================================================================
with tab_editor:
    st.markdown('<div class="card"><div class="card-title">✏️ Editor de Código Lua (Drive)</div></div>', unsafe_allow_html=True)

    if not config_keys:
        st.warning("No hay configs disponibles en Drive.")
    else:
        ed_config = st.selectbox("Archivo a editar", config_keys,
            format_func=lambda x: f"config_{x}.lua", key="ed_cfg_sel")

        ed_content = get_config_file_content(ed_config)
        if ed_content:
            edited = st.text_area("Código Lua", ed_content, height=500, key=f"editor_{ed_config}",
                                  label_visibility="collapsed")

            has_changes = edited != ed_content

            # Validar en tiempo real
            if has_changes:
                v_errors = validate_full_config(edited)
                if v_errors:
                    st.warning("⚠️ Problemas detectados:")
                    for ve in v_errors:
                        st.caption(f"- {ve}")
                else:
                    st.success("✅ Sintaxis válida")

            c1, c2, c3 = st.columns([2, 1, 1])
            with c1:
                if st.button(
                    "💾 Guardar cambios" if has_changes else "Sin cambios",
                    disabled=not has_changes, use_container_width=True, type="primary",
                    key=f"save_ed_{ed_config}"
                ):
                    stage_change(ed_config, edited)
                    st.success(f"config_{ed_config}.lua guardado (pendiente de aplicar)")
                    st.rerun()
            with c2:
                if st.button("↩️ Revertir", disabled=not has_changes, use_container_width=True, key=f"rev_{ed_config}"):
                    st.rerun()
            with c3:
                st.download_button("📥 Descargar", edited, f"config_{ed_config}.lua",
                    "text/plain", use_container_width=True, key=f"dl_ed_{ed_config}")
        else:
            st.error(f"No se pudo leer config_{ed_config}.lua desde Drive")

    render_apply_button("tab_editor")


# ============================================================================
# FOOTER
# ============================================================================
st.markdown("---")
st.markdown("""
<div style="text-align:center;padding:20px 15px">
    <span style="font-family:'Rye',cursive;color:#c9a227;font-size:.9rem;letter-spacing:2px">⚒️ CRAFTSMAN'S FORGE</span><br>
    <span style="font-family:'IM Fell English',serif;color:#d4c5a9;font-size:.8rem;font-style:italic;margin-top:4px;display:inline-block">
        « Gracias por aportar tu granito de arena a La Hermandad »
    </span><br>
    <span style="color:#8b6914;font-size:.7rem;margin-top:6px;display:inline-block">VORP Crafting System — ☁️ Google Drive</span>
</div>
""", unsafe_allow_html=True)
