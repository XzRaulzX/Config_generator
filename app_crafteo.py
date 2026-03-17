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
)
import lua_crafteo_generator as _lcg
from lua_crafteo_generator import (
    generate_crafting_block, add_crafting_to_config,
    parse_crafting_blocks, replace_crafting_in_config, delete_crafting_from_config,
    comment_crafting_in_config, uncomment_crafting_in_config, parse_commented_blocks,
    save_config_file, set_storage_mode, get_storage_mode, get_available_configs,
    get_config_name, register_config_name, create_empty_config,
    validate_lua_syntax, validate_full_config,
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
</style>
""", unsafe_allow_html=True)


# ============================================================================
# HELPERS — PENDING CHANGES SYSTEM
# ============================================================================

_original_get_content = _lcg.get_config_file_content


def get_config_file_content(job_key):
    """Lee contenido: primero busca en cambios pendientes, luego en Drive."""
    pending = st.session_state.get('pending_changes', {})
    if job_key in pending:
        return pending[job_key]
    return _original_get_content(job_key)


# Monkey-patch para que funciones internas (comment, delete, etc.) usen pending
_lcg.get_config_file_content = get_config_file_content


def stage_change(key, content):
    """Almacena un cambio pendiente en session state."""
    if 'pending_changes' not in st.session_state:
        st.session_state.pending_changes = {}
    st.session_state.pending_changes[key] = content


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
        drive_manager.clear_cache()
        return True, []
    # Eliminar los que sí se guardaron
    for key in list(pending.keys()):
        if not any(key in err for err in errors):
            del st.session_state.pending_changes[key]
    drive_manager.clear_cache()
    return False, errors


def discard_all_changes():
    """Descarta todos los cambios pendientes."""
    st.session_state.pending_changes = {}


def filter_items(items_dict, search_term):
    if not search_term:
        return items_dict
    s = search_term.lower()
    return {k: v for k, v in items_dict.items() if s in k.lower() or s in v.lower()}


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
    'pending_changes': {},
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ============================================================================
# HEADER
# ============================================================================
st.markdown("""
<div class="main-header">
    <h1>⚒️ CRAFTSMAN'S FORGE</h1>
    <p>~ Gestor de Configs VORP Crafting — La Hermandad ~</p>
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
# DATOS DE DRIVE
# ============================================================================
config_keys = list(set(get_available_configs()) | set(st.session_state.get('pending_changes', {}).keys()))
config_keys.sort()

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
        drive_manager.clear_cache()
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
tab_recetas, tab_nueva, tab_config, tab_editor = st.tabs([
    "📋 Gestionar Recetas", "➕ Nueva Receta", "🏭 Nuevo Config", "✏️ Editor Lua"
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
            comentados = parse_commented_blocks(content)

            st.markdown('<div class="card"><div class="card-title">📋 Recetas del Config</div></div>', unsafe_allow_html=True)

            # Resumen rápido
            c1, c2, c3 = st.columns(3)
            c1.metric("Recetas activas", len(crafteos))
            c2.metric("Desactivadas", len(comentados))
            c3.metric("Líneas", content.count('\n') + 1)

            # --- Crafteos activos ---
            if crafteos:
                st.markdown(f"**Recetas activas ({len(crafteos)})**")
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

                    with st.expander(label, expanded=False):
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
                            # Desactivar
                            if st.button("🚫 Desactivar", key=f"dis_{sel_config}_{idx}", use_container_width=True):
                                new_content = comment_crafting_in_config(sel_config, nombre_c)
                                if new_content:
                                    stage_change(sel_config, new_content)
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
                                            stage_change(sel_config, new_content)
                                            st.success(f"'{nombre_c}' eliminado (pendiente de aplicar)")
                                            del st.session_state[f"_confirm_del_{sel_config}_{idx}"]
                                            st.rerun()
                                with cb:
                                    if st.button("No", key=f"no_{sel_config}_{idx}", use_container_width=True):
                                        del st.session_state[f"_confirm_del_{sel_config}_{idx}"]
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
                                stage_change(sel_config, new_content)
                                st.success(f"'{bloque_d.get('nombre', '')}' reactivado (pendiente de aplicar)")
                                st.rerun()
                            else:
                                st.error("Error al reactivar la receta")

    render_apply_button("tab_recetas")


# ============================================================================
# TAB 2: NUEVA RECETA / EDITAR
# ============================================================================
with tab_nueva:
    if not config_keys:
        st.warning("Crea un config primero en la pestaña **Nuevo Config**.")
    else:
        col_form, col_preview = st.columns([1, 1], gap="large")

        with col_form:
            st.markdown('<div class="card"><div class="card-title">📝 Formulario de Receta</div></div>', unsafe_allow_html=True)

            # Config destino
            config_destino = st.selectbox(
                "Config destino",
                options=config_keys,
                format_func=lambda x: f"config_{x}.lua — {get_job_display_name(x)}",
                key="tab2_config_dest",
            )
            job_data = get_job_metadata(config_destino)

        # Modo crear / editar
        modo = st.radio(
            "Modo",
            ["crear", "editar"],
            format_func=lambda x: "✨ Crear nueva" if x == "crear" else "✏️ Editar existente",
            horizontal=True, key="tab2_modo"
        )

        # Defaults
        d_nombre, d_nivel, d_tipo, d_cat_idx = "", 0, "item", None
        d_take, d_use_curr, d_curr_type, d_location = True, False, 0, 0
        d_animation, d_pack = "craft", ""

        if modo == "editar":
            existing = get_config_file_content(config_destino)
            if existing:
                crafteos_edit = parse_crafting_blocks(existing)
                if crafteos_edit:
                    nombres = [c.get('nombre', '???') for c in crafteos_edit]
                    sel_idx = st.selectbox("Receta a editar", range(len(nombres)),
                                           format_func=lambda i: nombres[i], key="edit_sel")
                    cd = crafteos_edit[sel_idx]

                    # Detectar cambio de selección
                    nom_sel = cd.get('nombre', '')
                    if st.session_state.nombre_original != nom_sel:
                        st.session_state.nombre_original = nom_sel
                        st.session_state.crafteo_editando = cd
                        st.session_state.ingredientes = [
                            {'name': i.get('name', ''), 'label': ALL_ITEMS.get(i.get('name', ''), i.get('name', '')), 'count': i.get('count', 1)}
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
                    d_take = cd.get('take_items', True)
                    d_use_curr = cd.get('use_currency', False)
                    d_curr_type = cd.get('currency_type', 0)
                    d_location = cd.get('location', 0)
                    d_animation = cd.get('animation', 'craft')
                    d_pack = cd.get('pack', '')
                    loaded_cat = cd.get('categoria', '')
                    cat_keys = list(CATEGORIAS_CRAFTEO.keys())
                    d_cat_idx = cat_keys.index(loaded_cat) if loaded_cat in cat_keys else None

                    st.info(f"Editando: **{d_nombre}**")
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

        # --- Categoría ---
        cat_keys = list(CATEGORIAS_CRAFTEO.keys())
        if d_cat_idx is not None:
            cat_idx = d_cat_idx
        else:
            default_cat = job_data['category']
            cat_idx = cat_keys.index(default_cat) if default_cat in cat_keys else 0

        categoria = st.selectbox("Categoría del crafteo", cat_keys, index=cat_idx,
                                  format_func=lambda x: CATEGORIAS_CRAFTEO[x], key="cat_sel")

        # --- Nombre y nivel ---
        c1, c2 = st.columns([3, 1])
        nombre = c1.text_input("Nombre *", value=d_nombre, placeholder="Ej: Munición de pistola")
        nivel = c2.number_input("Nivel mín.", 0, 100, d_nivel)

        # --- Tipo ---
        tipo_keys = list(TIPOS_CRAFTEO.keys())
        tipo_idx = tipo_keys.index(d_tipo) if d_tipo in tipo_keys else 0
        tipo = st.selectbox("Tipo", tipo_keys, tipo_idx, format_func=lambda x: TIPOS_CRAFTEO[x])

        # --- RECOMPENSAS ---
        st.markdown('<div class="card"><div class="card-title">🎁 Recompensas</div></div>', unsafe_allow_html=True)

        search_rew = st.text_input("🔍 Buscar item de recompensa", placeholder="Filtrar...", key="s_rew")
        items_f = filter_items(ALL_ITEMS, search_rew)
        if search_rew:
            st.caption(f"{len(items_f)} encontrados")

        cr1, cr2, cr3 = st.columns([3, 1, 1])
        with cr1:
            use_manual_rew = st.checkbox("ID manual", key="m_rew")
            if use_manual_rew:
                new_rew = st.text_input("ID item", key="mr_id", placeholder="weapon_revolver_cattleman")
                new_rew_label = new_rew
            else:
                new_rew = st.selectbox("Item", [""] + list(items_f.keys()),
                    format_func=lambda x: f"{items_f[x]} ({x})" if x else "-- Seleccionar --", key="sr_sel")
                new_rew_label = items_f.get(new_rew, new_rew)
        cnt_rew = cr2.number_input("Cant.", 1, 999, 1, key="cr_cnt")
        with cr3:
            st.write(""); st.write("")
            if st.button("➕", key="add_rew", use_container_width=True):
                if new_rew:
                    st.session_state.recompensas.append({'name': new_rew, 'label': new_rew_label, 'count': cnt_rew})
                    st.rerun()

        for i, r in enumerate(st.session_state.recompensas):
            c_a, c_b = st.columns([5, 1])
            c_a.markdown(f'<div class="item-row" style="border-left-color:#00d26a"><div><span class="name">🎁 {r["label"]}</span> <span class="id">({r["name"]})</span></div><span class="count" style="background:#00d26a">x{r["count"]}</span></div>', unsafe_allow_html=True)
            if c_b.button("🗑️", key=f"dr_{i}"):
                st.session_state.recompensas.pop(i); st.rerun()

        if st.session_state.recompensas:
            if st.button("🗑️ Limpiar recompensas", key="cl_rew"):
                st.session_state.recompensas = []; st.rerun()

        # --- INGREDIENTES ---
        st.markdown('<div class="card"><div class="card-title">🧪 Ingredientes</div></div>', unsafe_allow_html=True)

        search_ing = st.text_input("🔍 Buscar ingrediente", placeholder="Filtrar...", key="s_ing")
        ings_f = filter_items(ALL_ITEMS, search_ing)
        if search_ing:
            st.caption(f"{len(ings_f)} encontrados")

        ci1, ci2, ci3 = st.columns([3, 1, 1])
        with ci1:
            use_manual_ing = st.checkbox("ID manual", key="m_ing")
            if use_manual_ing:
                new_ing = st.text_input("ID ingrediente", key="mi_id", placeholder="gunpowder")
                new_ing_label = new_ing
            else:
                new_ing = st.selectbox("Ingrediente", [""] + list(ings_f.keys()),
                    format_func=lambda x: f"{ings_f[x]} ({x})" if x else "-- Seleccionar --", key="si_sel")
                new_ing_label = ings_f.get(new_ing, new_ing)
        cnt_ing = ci2.number_input("Cant.", 1, 999, 1, key="ci_cnt")
        with ci3:
            st.write(""); st.write("")
            if st.button("➕", key="add_ing", use_container_width=True):
                if new_ing:
                    st.session_state.ingredientes.append({'name': new_ing, 'label': new_ing_label, 'count': cnt_ing})
                    st.rerun()

        for i, ing in enumerate(st.session_state.ingredientes):
            c_a, c_b = st.columns([5, 1])
            c_a.markdown(f'<div class="item-row"><div><span class="name">📦 {ing["label"]}</span> <span class="id">({ing["name"]})</span></div><span class="count">x{ing["count"]}</span></div>', unsafe_allow_html=True)
            if c_b.button("🗑️", key=f"di_{i}"):
                st.session_state.ingredientes.pop(i); st.rerun()

        if st.session_state.ingredientes:
            if st.button("🗑️ Limpiar ingredientes", key="cl_ing"):
                st.session_state.ingredientes = []; st.rerun()

        # --- OPCIONES AVANZADAS ---
        with st.expander("⚙️ Opciones avanzadas"):
            ca1, ca2 = st.columns(2)
            with ca1:
                take_items = st.checkbox("Consumir ingredientes", d_take, key="take")
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

            # Pack: predefinido o custom
            st.markdown("**Pack (opcional)**")
            pack_mode = st.radio("Tipo de pack", ["Predefinido", "Personalizado"], horizontal=True, key="pack_mode", label_visibility="collapsed")
            if pack_mode == "Predefinido":
                pack_idx = PACKS_PREDEFINIDOS.index(d_pack) if d_pack in PACKS_PREDEFINIDOS else 0
                pack = st.selectbox("Pack", PACKS_PREDEFINIDOS, pack_idx,
                    format_func=lambda x: "-- Sin pack --" if x == "" else x.capitalize(), key="pack_sel")
            else:
                pack = st.text_input("Nombre del pack", value=d_pack, placeholder="Ej: nomada", key="pack_custom")

            # Job override
            st.markdown("**Job (valor para filtro de trabajo)**")
            job_override = st.text_input("Job value", value=str(job_data['job_value']),
                help='0 = cualquiera. Para jobs específicos: {"medicoAR", "medicoBW"}', key="job_ov")
            if job_override.strip().startswith('{'):
                job_final = job_override.strip()
            else:
                try:
                    job_final = int(job_override)
                except ValueError:
                    job_final = 0

        # --- PREVIEW Y GUARDADO ---
        with col_preview:
            st.markdown('<div class="card"><div class="card-title">📤 Preview y Guardado</div></div>', unsafe_allow_html=True)

            errores = []
            if not nombre: errores.append("Nombre del crafteo")
            if not st.session_state.recompensas: errores.append("Al menos una recompensa")
            if not st.session_state.ingredientes: errores.append("Al menos un ingrediente")

            if errores:
                st.warning("**Campos requeridos:**")
                for e in errores:
                    st.markdown(f"- {e}")
            else:
                # Generar descripción automática
                desc = ", ".join(f"{i['count']}x {i['label']}" for i in st.session_state.ingredientes)

                datos = {
                    'nombre': nombre, 'descripcion': desc, 'categoria': categoria,
                    'tipo': tipo, 'nivel_minimo': nivel, 'recompensas': st.session_state.recompensas,
                    'ingredientes': st.session_state.ingredientes, 'take_items': take_items,
                    'currency_type': currency_type, 'location': location, 'animation': animation,
                    'use_currency': use_currency, 'job': job_final, 'pack': pack,
                }
                codigo_lua = generate_crafting_block(datos)

                # Validar sintaxis
                syntax_errors = validate_lua_syntax(codigo_lua)
                if syntax_errors:
                    st.error("⚠️ Errores de sintaxis Lua detectados:")
                    for se in syntax_errors:
                        st.markdown(f"- {se}")

                # Resumen
                st.markdown(f"""
                <div class="card">
                    <div class="card-title">✅ Resumen</div>
                    <table style="width:100%;color:#d4c5a9;font-family:'IM Fell English',serif">
                        <tr><td>Config destino</td><td style="text-align:right"><b>config_{config_destino}.lua</b></td></tr>
                        <tr><td>Nombre</td><td style="text-align:right"><b>{nombre}</b></td></tr>
                        <tr><td>Categoría</td><td style="text-align:right">{categoria}</td></tr>
                        <tr><td>Recompensas</td><td style="text-align:right">{len(st.session_state.recompensas)} items</td></tr>
                        <tr><td>Ingredientes</td><td style="text-align:right">{len(st.session_state.ingredientes)} items</td></tr>
                        <tr><td>Nivel mínimo</td><td style="text-align:right">{nivel}</td></tr>
                        <tr><td>Pack</td><td style="text-align:right">{pack or '—'}</td></tr>
                    </table>
                </div>
                """, unsafe_allow_html=True)

                # Código
                with st.expander("💻 Código Lua generado", expanded=True):
                    st.code(codigo_lua, language="lua")

                st.download_button("📥 Descargar bloque", codigo_lua,
                    f"crafteo_{config_destino}_{nombre.lower().replace(' ', '_')}.lua", "text/plain",
                    use_container_width=True, key="dl_block")

                st.markdown("---")

                # === MODO EDICIÓN: guardar cambios ===
                if modo == "editar" and st.session_state.nombre_original:
                    st.markdown(f"**Editando:** {st.session_state.nombre_original} → {nombre}")

                    config_editado = replace_crafting_in_config(config_destino, st.session_state.nombre_original, codigo_lua)
                    if config_editado:
                        # Validar config completo
                        full_errors = validate_full_config(config_editado)
                        if full_errors:
                            st.warning("Advertencias en el config resultante:")
                            for fe in full_errors:
                                st.caption(f"⚠️ {fe}")

                        if st.button("💾 Guardar cambios",
                                     use_container_width=True, type="primary", key="save_edit"):
                            stage_change(config_destino, config_editado)
                            st.success("Cambios guardados (pendiente de aplicar)")
                            st.session_state.ingredientes = []
                            st.session_state.recompensas = []
                            st.session_state.nombre_original = None
                            st.rerun()

                        with st.expander("Preview config editado"):
                            st.code(config_editado, language="lua")
                    else:
                        st.error("No se encontró el crafteo original para reemplazar")

                    # Opción desactivar
                    st.markdown("---")
                    if st.button("🚫 Desactivar este crafteo", key="disable_edit", use_container_width=True):
                        config_dis = comment_crafting_in_config(config_destino, st.session_state.nombre_original)
                        if config_dis:
                            stage_change(config_destino, config_dis)
                            st.success(f"'{st.session_state.nombre_original}' desactivado (pendiente de aplicar)")
                            st.session_state.ingredientes = []
                            st.session_state.recompensas = []
                            st.session_state.nombre_original = None
                            st.rerun()

                # === MODO CREACIÓN: añadir nuevo ===
                else:
                    existing = get_config_file_content(config_destino)
                    if existing:
                        config_completo = add_crafting_to_config(config_destino, codigo_lua)
                        n_existentes = len(parse_crafting_blocks(existing))

                        # Validar config completo
                        full_errors = validate_full_config(config_completo)
                        if full_errors:
                            st.warning("Advertencias en el config resultante:")
                            for fe in full_errors:
                                st.caption(f"⚠️ {fe}")

                        st.success(f"Config tiene {n_existentes} recetas. Se añadirá una nueva.")

                        if st.button(
                            f"💾 Guardar receta (config_{config_destino}.lua)",
                            use_container_width=True, type="primary", key="save_new"
                        ):
                            stage_change(config_destino, config_completo)
                            st.success("Receta añadida (pendiente de aplicar)")
                            st.session_state.ingredientes = []
                            st.session_state.recompensas = []
                            st.rerun()

                        with st.expander("Preview config completo"):
                            st.code(config_completo, language="lua")
                    else:
                        st.info(f"No existe config_{config_destino}.lua. Se creará uno nuevo en Drive.")
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
                            st.success("Config creado (pendiente de aplicar)")
                            st.rerun()

    render_apply_button("tab_nueva")


# ============================================================================
# TAB 3: CREAR NUEVO CONFIG (JOB)
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

            if new_category and new_category not in CATEGORIAS_CRAFTEO:
                CATEGORIAS_CRAFTEO[new_category] = f"📄 {new_display or new_category}"

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
# TAB 4: EDITOR LUA (lectura/escritura directa en Drive)
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
<div style="text-align:center;padding:15px">
    <span style="color:#888;font-size:.85rem">⚒️ <b>Craftsman's Forge</b> — VORP Crafting System</span><br>
    <span style="color:#666;font-size:.75rem">Desarrollado para La Hermandad — ☁️ Google Drive</span>
</div>
""", unsafe_allow_html=True)
