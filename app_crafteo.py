"""
Generador de Crafteos para RedM - VORP Crafting System
Aplicación Streamlit interactiva con diseño mejorado
"""

import streamlit as st
from config_items import (
    JOBS, TIPOS_CRAFTEO, ITEMS_RECOMPENSA, ITEMS_INGREDIENTES, 
    ANIMACIONES, CONFIG_PATH, ALL_ITEMS, CATEGORIAS_CRAFTEO
)
from lua_crafteo_generator import (
    generate_crafting_block, 
    add_crafting_to_config,
    get_config_file_content,
    parse_crafting_blocks,
    replace_crafting_in_config,
    delete_crafting_from_config
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
# ESTILOS CSS PERSONALIZADOS - TEMA RED DEAD REDEMPTION 2
# ============================================================================
st.markdown("""
<style>
    /* Importar fuentes Western */
    @import url('https://fonts.googleapis.com/css2?family=Rye&family=Cinzel:wght@400;600;700&family=IM+Fell+English:ital@0;1&family=UnifrakturMaguntia&display=swap');
    
    /* FIX: Los emojis NO deben heredar italic */
    .emoji, [class*="icon"], .empty-state-icon {
        font-style: normal !important;
    }
    
    /* Reset y variables - Paleta RDR2 Auténtica */
    :root {
        --rdr-gold: #c9a227;
        --rdr-gold-light: #dbb84d;
        --rdr-gold-dark: #8b6914;
        --rdr-red: #8b0000;
        --rdr-red-dark: #5c0000;
        --rdr-red-blood: #6b1c1c;
        --rdr-brown: #3d2914;
        --rdr-brown-light: #5c3d1e;
        --rdr-brown-dark: #1a1108;
        --rdr-brown-warm: #4a3728;
        --rdr-leather: #8b4513;
        --rdr-leather-dark: #654321;
        --rdr-parchment: #d4c5a9;
        --rdr-parchment-dark: #c4b089;
        --rdr-ink: #1a1a1a;
        --rdr-cream: #f5e6c8;
        --rdr-rust: #b7410e;
        --rdr-sepia: #704214;
        --border-radius: 3px;
    }
    
    /* ====== TEXTURAS BASE64 PARA EVITAR DEPENDENCIAS EXTERNAS ====== */
    
    /* Fondo general - Textura de cuero oscuro con grano */
    .stApp {
        background: 
            /* Capa de oscurecimiento */
            linear-gradient(rgba(18, 12, 8, 0.92), rgba(26, 17, 8, 0.95)),
            /* Textura de cuero marrón oscuro */
            url('https://images.unsplash.com/photo-1531685250784-7569952593d2?w=1920&q=80');
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
    }
    
    /* Header principal - Estilo WANTED POSTER auténtico */
    .main-header {
        text-align: center;
        padding: 50px 40px 40px 40px;
        background: 
            /* Textura de papel viejo/pergamino */
            linear-gradient(rgba(212, 197, 169, 0.97), rgba(196, 176, 137, 0.95)),
            url('https://images.unsplash.com/photo-1541123603104-512919d6a96c?w=1200&q=80');
        background-size: cover;
        background-position: center;
        border-radius: var(--border-radius);
        margin-bottom: 30px;
        border: none;
        box-shadow: 
            0 0 0 3px var(--rdr-brown-dark),
            0 0 0 6px var(--rdr-leather),
            0 0 0 8px var(--rdr-brown-dark),
            0 12px 40px rgba(0, 0, 0, 0.7),
            inset 0 0 100px rgba(139, 69, 19, 0.15);
        position: relative;
        /* Efecto de papel desgastado */
        clip-path: polygon(
            0% 2%, 2% 0%, 98% 0%, 100% 2%,
            100% 98%, 98% 100%, 2% 100%, 0% 98%
        );
    }
    
    /* Decoraciones de esquina estilo cartel */
    .main-header::before {
        content: "★ WANTED ★";
        position: absolute;
        top: 12px;
        left: 50%;
        transform: translateX(-50%);
        font-family: 'Rye', cursive;
        font-size: 0.85rem;
        color: var(--rdr-red-dark);
        letter-spacing: 8px;
        opacity: 0.7;
    }
    
    .main-header::after {
        content: "— DEAD OR ALIVE —";
        position: absolute;
        bottom: 12px;
        left: 50%;
        transform: translateX(-50%);
        font-family: 'IM Fell English', serif;
        font-size: 0.75rem;
        color: var(--rdr-sepia);
        letter-spacing: 3px;
        font-style: italic;
        opacity: 0.6;
    }
    
    .main-header h1 {
        font-family: 'Rye', cursive;
        color: var(--rdr-brown-dark);
        margin: 15px 0;
        font-size: 3rem;
        font-weight: 400;
        text-shadow: 
            2px 2px 0 rgba(212, 197, 169, 0.8),
            -1px -1px 0 rgba(0, 0, 0, 0.1);
        letter-spacing: 4px;
        text-transform: uppercase;
    }
    
    .main-header p {
        font-family: 'IM Fell English', serif;
        color: var(--rdr-sepia);
        margin: 10px 0 15px 0;
        font-size: 1.15rem;
        font-style: italic;
        letter-spacing: 1px;
    }
    
    /* Tarjetas de sección - Estilo cuero curtido */
    .section-card {
        background: 
            /* Textura de cuero */
            linear-gradient(145deg, rgba(74, 55, 40, 0.95) 0%, rgba(42, 28, 15, 0.98) 50%, rgba(26, 17, 8, 0.99) 100%),
            url('https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&q=80');
        background-size: cover;
        padding: 25px;
        border-radius: var(--border-radius);
        margin-bottom: 20px;
        border: 3px solid var(--rdr-leather-dark);
        box-shadow: 
            inset 0 2px 4px rgba(255,255,255,0.05),
            inset 0 -2px 4px rgba(0,0,0,0.3),
            inset 0 0 40px rgba(0,0,0,0.4),
            0 6px 20px rgba(0,0,0,0.5);
        position: relative;
    }
    
    /* Efecto de costuras en las tarjetas */
    .section-card::before {
        content: "";
        position: absolute;
        top: 8px;
        left: 8px;
        right: 8px;
        bottom: 8px;
        border: 1px dashed rgba(201, 162, 39, 0.2);
        border-radius: 2px;
        pointer-events: none;
    }
    
    .section-card:hover {
        border-color: var(--rdr-gold-dark);
        box-shadow: 
            inset 0 2px 4px rgba(255,255,255,0.08),
            inset 0 -2px 4px rgba(0,0,0,0.3),
            inset 0 0 40px rgba(0,0,0,0.4),
            0 8px 25px rgba(201, 162, 39, 0.15);
    }
    
    .section-title {
        font-family: 'Cinzel', serif;
        color: var(--rdr-gold);
        font-weight: 600;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        gap: 10px;
        text-transform: uppercase;
        letter-spacing: 2px;
        border-bottom: 1px solid var(--rdr-leather);
        padding-bottom: 10px;
    }
    
    /* Ingredientes - Estilo lista de materiales */
    .ingredient-box {
        background: linear-gradient(90deg, rgba(139, 69, 19, 0.3) 0%, rgba(61, 41, 20, 0.5) 100%);
        padding: 15px 20px;
        border-radius: var(--border-radius);
        margin: 10px 0;
        border-left: 4px solid var(--rdr-gold);
        border-right: 1px solid var(--rdr-leather);
        border-top: 1px solid rgba(139, 69, 19, 0.3);
        border-bottom: 1px solid rgba(139, 69, 19, 0.3);
        display: flex;
        align-items: center;
        justify-content: space-between;
        transition: all 0.3s ease;
        position: relative;
    }
    
    .ingredient-box::before {
        content: "◆";
        position: absolute;
        left: -12px;
        color: var(--rdr-gold);
        font-size: 0.6rem;
    }
    
    .ingredient-box:hover {
        transform: translateX(8px);
        background: linear-gradient(90deg, rgba(201, 162, 39, 0.15) 0%, rgba(61, 41, 20, 0.6) 100%);
        border-left-color: var(--rdr-gold-light);
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
        font-family: 'Cinzel', serif;
        font-weight: 600;
        color: var(--rdr-cream);
        text-transform: uppercase;
        font-size: 0.9rem;
        letter-spacing: 1px;
    }
    
    .ingredient-id {
        font-family: 'IM Fell English', serif;
        color: var(--rdr-parchment);
        font-size: 0.85rem;
        font-style: italic;
        opacity: 0.8;
    }
    
    .ingredient-count {
        background: linear-gradient(135deg, var(--rdr-gold) 0%, var(--rdr-gold-light) 100%);
        color: var(--rdr-brown-dark);
        padding: 6px 14px;
        border-radius: 2px;
        font-family: 'Cinzel', serif;
        font-weight: 700;
        font-size: 0.9rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }
    
    /* Stats cards - Estilo WANTED POSTER pequeño */
    .stats-container {
        display: flex;
        gap: 15px;
        margin-bottom: 20px;
    }
    
    .stat-card {
        background: 
            linear-gradient(rgba(212, 197, 169, 0.95), rgba(188, 169, 129, 0.92)),
            url('https://images.unsplash.com/photo-1541123603104-512919d6a96c?w=400&q=60');
        background-size: cover;
        padding: 20px;
        border-radius: var(--border-radius);
        flex: 1;
        text-align: center;
        border: 3px solid var(--rdr-brown);
        box-shadow: 
            0 0 0 1px var(--rdr-leather-dark),
            inset 0 0 25px rgba(139, 69, 19, 0.2),
            0 5px 15px rgba(0,0,0,0.4);
        position: relative;
        /* Efecto de papel rasgado */
        clip-path: polygon(
            1% 0%, 99% 1%, 100% 99%, 0% 98%
        );
    }
    
    .stat-card::before {
        content: "★";
        position: absolute;
        top: 5px;
        right: 8px;
        color: var(--rdr-red);
        font-size: 0.9rem;
        text-shadow: 0 0 2px rgba(0,0,0,0.3);
    }
    
    .stat-card::after {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: repeating-linear-gradient(
            0deg,
            transparent,
            transparent 2px,
            rgba(139, 69, 19, 0.03) 2px,
            rgba(139, 69, 19, 0.03) 4px
        );
        pointer-events: none;
    }
    
    .stat-number {
        font-family: 'Rye', cursive;
        font-size: 2.4rem;
        font-weight: 400;
        color: var(--rdr-red-dark);
        text-shadow: 1px 1px 0 rgba(255,255,255,0.4);
        position: relative;
        z-index: 1;
    }
    
    .stat-label {
        font-family: 'Cinzel', serif;
        color: var(--rdr-brown);
        font-size: 0.8rem;
        margin-top: 5px;
        text-transform: uppercase;
        letter-spacing: 1px;
        position: relative;
        z-index: 1;
    }
    
    /* Job badges - Estilo placas de sheriff */
    .job-badge {
        display: inline-block;
        padding: 10px 18px;
        border-radius: 2px;
        font-family: 'Cinzel', serif;
        font-size: 0.8rem;
        font-weight: 600;
        margin: 4px;
        background: 
            linear-gradient(145deg, rgba(74, 55, 40, 0.95) 0%, rgba(42, 28, 15, 0.98) 100%),
            url('https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=200&q=60');
        background-size: cover;
        border: 2px solid var(--rdr-gold-dark);
        color: var(--rdr-gold);
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 
            inset 0 1px 2px rgba(255,255,255,0.1),
            0 3px 8px rgba(0,0,0,0.4);
        transition: all 0.3s ease;
        position: relative;
    }
    
    .job-badge::before {
        content: "◆";
        margin-right: 6px;
        font-size: 0.6rem;
        opacity: 0.7;
    }
    
    .job-badge:hover {
        transform: scale(1.05) translateY(-2px);
        background: linear-gradient(145deg, var(--rdr-gold) 0%, var(--rdr-gold-dark) 100%);
        color: var(--rdr-brown-dark);
        border-color: var(--rdr-gold-light);
        box-shadow: 
            0 6px 20px rgba(201, 162, 39, 0.4),
            inset 0 1px 3px rgba(255,255,255,0.2);
    }
    
    /* Resumen crafteo - Estilo receta/documento antiguo */
    .craft-summary {
        background: 
            linear-gradient(rgba(212, 197, 169, 0.97), rgba(196, 176, 137, 0.95)),
            url('https://images.unsplash.com/photo-1541123603104-512919d6a96c?w=800&q=70');
        background-size: cover;
        border: none;
        border-radius: var(--border-radius);
        padding: 30px;
        margin: 15px 0;
        box-shadow: 
            0 0 0 2px var(--rdr-brown),
            0 0 0 4px var(--rdr-leather-dark),
            inset 0 0 40px rgba(139, 69, 19, 0.15),
            0 8px 25px rgba(0,0,0,0.4);
        position: relative;
    }
    
    .craft-summary::before {
        content: "✦ RECETA DE CRAFTEO ✦";
        position: absolute;
        top: -12px;
        left: 50%;
        transform: translateX(-50%);
        font-family: 'Rye', cursive;
        font-size: 0.75rem;
        color: var(--rdr-sepia);
        background: var(--rdr-parchment);
        padding: 4px 15px;
        letter-spacing: 2px;
        border: 1px solid var(--rdr-leather);
    }
    
    .craft-summary::after {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: repeating-linear-gradient(
            0deg,
            transparent,
            transparent 3px,
            rgba(139, 69, 19, 0.02) 3px,
            rgba(139, 69, 19, 0.02) 6px
        );
        pointer-events: none;
        border-radius: var(--border-radius);
    }
    
    .craft-summary-title {
        font-family: 'Rye', cursive;
        color: var(--rdr-red-dark);
        font-size: 1.4rem;
        font-weight: 400;
        margin-bottom: 20px;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 3px;
        position: relative;
        z-index: 1;
    }
    
    .summary-row {
        display: flex;
        justify-content: space-between;
        padding: 12px 0;
        border-bottom: 1px dashed rgba(139, 69, 19, 0.4);
        position: relative;
        z-index: 1;
    }
    
    .summary-label {
        font-family: 'IM Fell English', serif;
        color: var(--rdr-sepia);
        font-style: italic;
        font-size: 1rem;
    }
    
    .summary-value {
        font-family: 'Cinzel', serif;
        color: var(--rdr-brown-dark);
        font-weight: 600;
    }
    
    /* Código Lua - Estilo telegrama/documento oficial */
    .lua-code-container {
        background: 
            linear-gradient(rgba(30, 24, 18, 0.98), rgba(22, 18, 14, 0.99)),
            url('https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=600&q=60');
        background-size: cover;
        border-radius: var(--border-radius);
        border: 3px solid var(--rdr-leather-dark);
        overflow: hidden;
        box-shadow: 
            inset 0 0 30px rgba(0,0,0,0.6),
            0 6px 20px rgba(0,0,0,0.5);
    }
    
    .lua-code-header {
        background: 
            linear-gradient(90deg, rgba(61, 41, 20, 0.95) 0%, rgba(92, 61, 30, 0.9) 50%, rgba(61, 41, 20, 0.95) 100%);
        padding: 15px 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 2px solid var(--rdr-gold);
        position: relative;
    }
    
    .lua-code-header::before {
        content: "◆ CÓDIGO LUA ◆";
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-family: 'Cinzel', serif;
        font-size: 0.7rem;
        color: var(--rdr-gold);
        letter-spacing: 3px;
        opacity: 0.6;
    }
    
    .lua-code-title {
        font-family: 'Cinzel', serif;
        color: var(--rdr-gold);
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    /* Botones personalizados - Estilo western */
    .stButton > button {
        font-family: 'Cinzel', serif !important;
        border-radius: 2px !important;
        font-weight: 600 !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        transition: all 0.3s ease !important;
        border: 2px solid var(--rdr-gold) !important;
        background: 
            linear-gradient(145deg, rgba(74, 55, 40, 0.95) 0%, rgba(42, 28, 15, 0.98) 100%) !important;
        color: var(--rdr-gold) !important;
        box-shadow: 
            inset 0 1px 2px rgba(255,255,255,0.1),
            0 3px 8px rgba(0,0,0,0.3) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        background: linear-gradient(145deg, var(--rdr-gold) 0%, var(--rdr-gold-dark) 100%) !important;
        color: var(--rdr-brown-dark) !important;
        box-shadow: 
            0 6px 20px rgba(201, 162, 39, 0.4),
            inset 0 1px 3px rgba(255,255,255,0.2) !important;
    }
    
    /* Download button - Estilo REWARD/BOUNTY */
    .stDownloadButton > button {
        background: 
            linear-gradient(145deg, var(--rdr-red) 0%, var(--rdr-red-dark) 100%) !important;
        border: 3px solid var(--rdr-gold) !important;
        border-radius: 2px !important;
        font-family: 'Rye', cursive !important;
        font-weight: 400 !important;
        color: var(--rdr-gold) !important;
        text-transform: uppercase !important;
        letter-spacing: 2px !important;
        box-shadow: 
            0 0 0 1px var(--rdr-brown-dark),
            0 4px 12px rgba(139, 0, 0, 0.4) !important;
    }
    
    .stDownloadButton > button:hover {
        transform: translateY(-3px) scale(1.02) !important;
        background: linear-gradient(145deg, #a50000 0%, var(--rdr-red) 100%) !important;
        box-shadow: 
            0 0 0 1px var(--rdr-gold),
            0 8px 25px rgba(139, 0, 0, 0.5) !important;
    }
    
    /* Selectbox mejorado */
    .stSelectbox > div > div {
        border-radius: 2px !important;
        border: 2px solid var(--rdr-leather) !important;
        background: var(--rdr-brown-dark) !important;
        font-family: 'Cinzel', serif !important;
    }
    
    .stSelectbox label {
        font-family: 'Cinzel', serif !important;
        color: var(--rdr-gold) !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
    }
    
    /* Number input */
    .stNumberInput > div > div > input {
        border: 2px solid var(--rdr-leather) !important;
        border-radius: 2px !important;
        background: var(--rdr-brown-dark) !important;
        color: var(--rdr-cream) !important;
        font-family: 'Cinzel', serif !important;
    }
    
    .stNumberInput label {
        font-family: 'Cinzel', serif !important;
        color: var(--rdr-gold) !important;
    }
    
    /* Text input */
    .stTextInput > div > div > input {
        border: 2px solid var(--rdr-leather) !important;
        border-radius: 2px !important;
        background: var(--rdr-brown-dark) !important;
        color: var(--rdr-cream) !important;
        font-family: 'IM Fell English', serif !important;
    }
    
    .stTextInput label {
        font-family: 'Cinzel', serif !important;
        color: var(--rdr-gold) !important;
        text-transform: uppercase !important;
    }
    
    /* Expander - Estilo acordeón western */
    .streamlit-expanderHeader {
        background: linear-gradient(90deg, var(--rdr-brown) 0%, var(--rdr-brown-light) 100%) !important;
        border: 2px solid var(--rdr-leather) !important;
        border-radius: 2px !important;
        font-family: 'Cinzel', serif !important;
        color: var(--rdr-gold) !important;
    }
    
    /* Sidebar - Estilo tablón de madera del saloon */
    .css-1d391kg, [data-testid="stSidebar"] {
        background: 
            linear-gradient(rgba(26, 17, 8, 0.94), rgba(42, 28, 15, 0.96)),
            url('https://images.unsplash.com/photo-1558591710-4b4a1ae0f04d?w=500&q=80');
        background-size: cover;
        background-position: center;
        border-right: 4px solid var(--rdr-leather-dark);
        box-shadow: 
            inset -5px 0 20px rgba(0,0,0,0.3),
            5px 0 15px rgba(0,0,0,0.4);
    }
    
    [data-testid="stSidebar"]::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: repeating-linear-gradient(
            90deg,
            transparent,
            transparent 48px,
            rgba(0,0,0,0.1) 48px,
            rgba(0,0,0,0.1) 50px
        );
        pointer-events: none;
    }
    
    [data-testid="stSidebar"] .stMarkdown {
        font-family: 'IM Fell English', serif;
    }
    
    .sidebar-stat {
        background: 
            linear-gradient(145deg, rgba(212, 197, 169, 0.92), rgba(188, 169, 129, 0.88)),
            url('https://images.unsplash.com/photo-1541123603104-512919d6a96c?w=300&q=60');
        background-size: cover;
        padding: 20px 15px;
        border-radius: 2px;
        margin: 12px 5px;
        text-align: center;
        border: 2px solid var(--rdr-brown);
        box-shadow: 
            0 0 0 1px var(--rdr-leather-dark),
            inset 0 0 20px rgba(139, 69, 19, 0.15),
            0 4px 12px rgba(0,0,0,0.4);
        position: relative;
    }
    
    .sidebar-stat::before {
        content: "★";
        position: absolute;
        top: 3px;
        left: 50%;
        transform: translateX(-50%);
        color: var(--rdr-red-dark);
        font-size: 0.6rem;
    }
    
    .sidebar-stat-number {
        font-family: 'Rye', cursive;
        font-size: 2.2rem;
        font-weight: 400;
        color: var(--rdr-red-dark);
        text-shadow: 1px 1px 0 rgba(255,255,255,0.3);
    }
    
    .sidebar-stat-label {
        font-family: 'Cinzel', serif;
        color: var(--rdr-brown);
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-top: 5px;
    }
    
    /* Info boxes - Estilo nota clavada */
    .info-tip {
        background: 
            linear-gradient(rgba(212, 197, 169, 0.95), rgba(196, 176, 137, 0.9));
        border-left: none;
        border: 2px solid var(--rdr-brown);
        padding: 15px 20px;
        border-radius: 2px;
        margin: 12px 5px;
        font-family: 'IM Fell English', serif;
        color: var(--rdr-sepia);
        box-shadow: 
            3px 3px 8px rgba(0,0,0,0.3),
            inset 0 0 15px rgba(139, 69, 19, 0.1);
        position: relative;
        transform: rotate(-0.5deg);
    }
    
    .info-tip::before {
        content: "📌";
        position: absolute;
        top: -8px;
        left: 10px;
        font-size: 1rem;
        font-style: normal;
    }
    
    .info-tip strong {
        font-style: normal;
    }
    
    /* Empty state */
    .empty-state {
        text-align: center;
        padding: 50px 20px;
        color: var(--rdr-parchment);
        font-family: 'IM Fell English', serif;
    }
    
    .empty-state-icon {
        font-size: 3.5rem;
        margin-bottom: 15px;
        font-style: normal !important;
    }
    
    /* Divider decorativo */
    .western-divider {
        text-align: center;
        margin: 20px 0;
        color: var(--rdr-gold);
        font-size: 1.2rem;
        letter-spacing: 10px;
    }
    
    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .animate-in {
        animation: fadeIn 0.4s ease-out;
    }
    
    /* Scrollbar - Estilo cuero */
    ::-webkit-scrollbar {
        width: 12px;
        height: 12px;
    }
    
    ::-webkit-scrollbar-track {
        background: var(--rdr-brown-dark);
        border: 1px solid var(--rdr-leather);
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(145deg, var(--rdr-leather) 0%, var(--rdr-brown) 100%);
        border-radius: 2px;
        border: 1px solid var(--rdr-gold);
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(145deg, var(--rdr-gold) 0%, var(--rdr-leather) 100%);
    }
    
    /* Code block */
    code {
        white-space: pre-wrap !important;
        font-family: 'Courier New', monospace !important;
        background: var(--rdr-brown-dark) !important;
        color: var(--rdr-gold) !important;
    }
    
    /* Tabs - Estilo pestañas de saloon */
    .stTabs [data-baseweb="tab-list"] {
        gap: 4px;
        background: var(--rdr-brown-dark);
        padding: 5px;
        border-radius: 2px;
        border: 2px solid var(--rdr-leather);
    }
    
    .stTabs [data-baseweb="tab"] {
        font-family: 'Cinzel', serif !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: var(--rdr-parchment);
        background: transparent;
        border-radius: 2px;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(145deg, var(--rdr-gold) 0%, var(--rdr-gold-light) 100%) !important;
        color: var(--rdr-brown-dark) !important;
    }
    
    /* Checkbox */
    .stCheckbox label {
        font-family: 'IM Fell English', serif !important;
        color: var(--rdr-parchment) !important;
    }
    
    /* Success/Error messages */
    .stSuccess {
        background: linear-gradient(90deg, rgba(34, 139, 34, 0.2) 0%, transparent 100%) !important;
        border-left: 4px solid #228b22 !important;
        font-family: 'IM Fell English', serif !important;
    }
    
    .stError {
        background: linear-gradient(90deg, rgba(139, 0, 0, 0.2) 0%, transparent 100%) !important;
        border-left: 4px solid var(--rdr-red) !important;
        font-family: 'IM Fell English', serif !important;
    }
    
    /* Decoración de esquinas */
    .corner-decoration {
        position: relative;
    }
    
    .corner-decoration::before,
    .corner-decoration::after {
        content: "✦";
        color: var(--rdr-gold);
        position: absolute;
        font-size: 0.8rem;
    }
    
    .corner-decoration::before {
        top: 5px;
        left: 5px;
    }
    
    .corner-decoration::after {
        bottom: 5px;
        right: 5px;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Custom footer */
    .rdr-footer {
        text-align: center;
        padding: 20px;
        margin-top: 30px;
        border-top: 2px solid var(--rdr-leather);
        font-family: 'IM Fell English', serif;
        color: var(--rdr-parchment);
        font-style: italic;
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

# Estado para modo edición
if 'modo_edicion' not in st.session_state:
    st.session_state.modo_edicion = False

if 'crafteo_editando' not in st.session_state:
    st.session_state.crafteo_editando = None

if 'nombre_original' not in st.session_state:
    st.session_state.nombre_original = None

# ============================================================================
# HEADER PRINCIPAL
# ============================================================================
st.markdown("""
<div class="main-header animate-in">
    <h1>⚒️ CRAFTSMAN'S FORGE</h1>
    <p>~ VORP Crafting System ~ Herramienta de Configuración para La Hermandad ~</p>
</div>
<div class="western-divider">✦ ✦ ✦</div>
""", unsafe_allow_html=True)

# ============================================================================
# SIDEBAR - INFORMACIÓN Y ESTADÍSTICAS
# ============================================================================
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 10px 0 20px 0;">
        <span style="font-family: 'Rye', cursive; font-size: 1.5rem; color: #c9a227;">⭐ REGISTRO ⭐</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Stats
    st.markdown(f"""
    <div class="sidebar-stat">
        <div class="sidebar-stat-number">{len(ALL_ITEMS):,}</div>
        <div class="sidebar-stat-label">📦 Objetos en Almacén</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="sidebar-stat">
        <div class="sidebar-stat-number">{len(JOBS)}</div>
        <div class="sidebar-stat-label">🏪 Oficios Registrados</div>
    </div>
    """, unsafe_allow_html=True)
    
    col_stat1, col_stat2 = st.columns(2)
    with col_stat1:
        st.markdown(f"""
        <div class="sidebar-stat">
            <div class="sidebar-stat-number">{len(st.session_state.recompensas)}</div>
            <div class="sidebar-stat-label">🎁 Productos</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col_stat2:
        st.markdown(f"""
        <div class="sidebar-stat">
            <div class="sidebar-stat-number">{len(st.session_state.ingredientes)}</div>
            <div class="sidebar-stat-label">🧰 Materiales</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div class="western-divider">◆ ◆ ◆</div>', unsafe_allow_html=True)
    
    # Jobs disponibles con badges
    st.markdown("""
    <div style="text-align: center; margin-bottom: 15px;">
        <span style="font-family: 'Cinzel', serif; font-size: 1rem; color: #c9a227; text-transform: uppercase; letter-spacing: 2px;">Oficios Disponibles</span>
    </div>
    """, unsafe_allow_html=True)
    
    jobs_html = ""
    for job_key, job_data in JOBS.items():
        jobs_html += f'<span class="job-badge">{job_data["nombre"]}</span>'
    
    st.markdown(f'<div style="line-height: 2.5;">{jobs_html}</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="western-divider">◆ ◆ ◆</div>', unsafe_allow_html=True)
    
    # Tips
    st.markdown("""
    <div style="text-align: center; margin-bottom: 15px;">
        <span style="font-family: 'Cinzel', serif; font-size: 1rem; color: #c9a227; text-transform: uppercase; letter-spacing: 2px;">📜 Consejos del Viejo Oeste</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-tip">
        <strong>🔍 Búsqueda:</strong> El campo de búsqueda te permite encontrar entre más de 1000 objetos del territorio.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-tip">
        <strong>📦 Materiales:</strong> Un mismo material puede añadirse varias veces con diferentes cantidades.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="rdr-footer">
        "En el Oeste, los artesanos forjan su destino"<br>
        <small>~ La Hermandad ~</small>
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
    st.markdown("""
    <div style="text-align: center; margin-bottom: 20px;">
        <span style="font-family: 'Rye', cursive; font-size: 1.8rem; color: #c9a227;">📝 RECETA DE CRAFTEO</span>
    </div>
    """, unsafe_allow_html=True)
    
    # ----- PASO 1: SELECCIONAR JOB -----
    st.markdown("""
    <div class="section-card">
        <div class="section-title">🏷️ Seleccionar Oficio</div>
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
        st.session_state.modo_edicion = False
        st.session_state.crafteo_editando = None
        st.session_state.nombre_original = None
    
    job_data = JOBS[job_seleccionado]
    
    # ----- MODO: CREAR / EDITAR -----
    st.markdown("""
    <div class="section-card">
        <div class="section-title">🔧 Modo de Trabajo</div>
    </div>
    """, unsafe_allow_html=True)
    
    modo = st.radio(
        "¿Qué deseas hacer?",
        options=["crear", "editar"],
        format_func=lambda x: "✨ Crear nuevo crafteo" if x == "crear" else "✏️ Editar crafteo existente",
        horizontal=True,
        key="modo_trabajo"
    )
    
    # Si cambia de modo, limpiar estado
    nuevo_modo_edicion = (modo == "editar")
    if nuevo_modo_edicion != st.session_state.modo_edicion:
        st.session_state.modo_edicion = nuevo_modo_edicion
        st.session_state.ingredientes = []
        st.session_state.recompensas = []
        st.session_state.crafteo_editando = None
        st.session_state.nombre_original = None
    
    # Variables por defecto para campos del formulario
    default_nombre = ""
    default_nivel = 0
    default_tipo = "item"
    default_categoria_idx = None
    default_take_items = True
    default_use_currency = False
    default_currency_type = 0
    default_location = 0
    default_animation = "craft"
    
    # Si estamos en modo edición, cargar crafteos existentes
    if st.session_state.modo_edicion:
        existing_config = get_config_file_content(job_seleccionado)
        if existing_config:
            crafteos_existentes = parse_crafting_blocks(existing_config)
            
            if crafteos_existentes:
                nombres_crafteos = [c.get('nombre', '???') for c in crafteos_existentes]
                
                crafteo_selected = st.selectbox(
                    "📋 Selecciona el crafteo a editar",
                    options=range(len(nombres_crafteos)),
                    format_func=lambda i: nombres_crafteos[i],
                    key="crafteo_editar_select"
                )
                
                crafteo_data = crafteos_existentes[crafteo_selected]
                
                # Detectar si cambió la selección del crafteo
                nombre_sel = crafteo_data.get('nombre', '')
                if st.session_state.nombre_original != nombre_sel:
                    st.session_state.nombre_original = nombre_sel
                    st.session_state.crafteo_editando = crafteo_data
                    
                    # Cargar ingredientes
                    ingredientes_cargados = []
                    for ing in crafteo_data.get('ingredientes', []):
                        ingredientes_cargados.append({
                            'name': ing.get('name', ''),
                            'label': ALL_ITEMS.get(ing.get('name', ''), ing.get('name', '')),
                            'count': ing.get('count', 1)
                        })
                    st.session_state.ingredientes = ingredientes_cargados
                    
                    # Cargar recompensas
                    recompensas_cargadas = []
                    for rew in crafteo_data.get('recompensas', []):
                        recompensas_cargadas.append({
                            'name': rew.get('name', ''),
                            'label': ALL_ITEMS.get(rew.get('name', ''), rew.get('name', '')),
                            'count': rew.get('count', 1)
                        })
                    st.session_state.recompensas = recompensas_cargadas
                    
                    st.rerun()
                
                # Cargar defaults del crafteo seleccionado
                default_nombre = crafteo_data.get('nombre', '')
                default_nivel = crafteo_data.get('nivel_minimo', 0)
                default_tipo = crafteo_data.get('tipo', 'item')
                default_take_items = crafteo_data.get('take_items', True)
                default_use_currency = crafteo_data.get('use_currency', False)
                default_currency_type = crafteo_data.get('currency_type', 0)
                default_location = crafteo_data.get('location', 0)
                default_animation = crafteo_data.get('animation', 'craft')
                
                # Determinar categoría por defecto del crafteo cargado
                loaded_cat = crafteo_data.get('categoria', '')
                category_keys_temp = list(CATEGORIAS_CRAFTEO.keys())
                if loaded_cat in category_keys_temp:
                    default_categoria_idx = category_keys_temp.index(loaded_cat)
                
                st.success(f"📝 Editando: **{default_nombre}**")
            else:
                st.warning("⚠️ No se encontraron crafteos en este archivo de configuración")
                st.session_state.modo_edicion = False
        else:
            st.warning(f"⚠️ No existe el archivo `config_{job_seleccionado}.lua`")
            st.session_state.modo_edicion = False
    
    # Categoría del crafteo (puede ser diferente al job del config)
    st.markdown("""
    <div class="info-tip">
        <strong>Categoría del crafteo:</strong> Define en qué menú aparecerá este crafteo para el jugador.
        Por defecto coincide con el oficio, pero puedes cambiarlo.
    </div>
    """, unsafe_allow_html=True)
    
    # Obtener el índice por defecto basado en el job seleccionado o el crafteo cargado
    if default_categoria_idx is not None:
        cat_default_index = default_categoria_idx
    else:
        default_category = job_data['category']
        category_keys = list(CATEGORIAS_CRAFTEO.keys())
        cat_default_index = category_keys.index(default_category) if default_category in category_keys else 0
    
    category_keys = list(CATEGORIAS_CRAFTEO.keys())
    
    categoria_crafteo = st.selectbox(
        "Categoría del Crafteo",
        options=category_keys,
        index=cat_default_index,
        format_func=lambda x: CATEGORIAS_CRAFTEO[x],
        help="En qué categoría aparecerá este crafteo en el menú del jugador"
    )
    
    # ----- PASO 2: INFORMACIÓN BÁSICA -----
    st.markdown("""
    <div class="section-card">
        <div class="section-title">✏️ Detalles del Producto</div>
    </div>
    """, unsafe_allow_html=True)
    
    col_info1, col_info2 = st.columns([2, 1])
    
    with col_info1:
        nombre = st.text_input(
            "Nombre del Crafteo *",
            value=default_nombre,
            placeholder="Ej: Munición de pistola",
            help="Nombre que verá el jugador en el menú"
        )
    
    with col_info2:
        nivel_minimo = st.number_input(
            "Nivel Mínimo",
            min_value=0,
            max_value=100,
            value=default_nivel,
            help="Nivel requerido para craftear"
        )
    
    # Tipo de crafteo
    if job_seleccionado in ['armero', 'bandas']:
        tipo_options = {'item': '📦 Item Normal', 'weapon': '🔫 Arma'}
    else:
        tipo_options = {'item': '📦 Item Normal'}
    
    tipo_keys = list(tipo_options.keys())
    tipo_default_idx = tipo_keys.index(default_tipo) if default_tipo in tipo_keys else 0
    
    tipo = st.selectbox(
        "Tipo de Crafteo",
        options=tipo_keys,
        index=tipo_default_idx,
        format_func=lambda x: tipo_options[x],
        help="Tipo de item que se craftea"
    )
    
    # ----- PASO 3: RECOMPENSAS -----
    st.markdown("""
    <div class="section-card">
        <div class="section-title">🎁 Productos a Fabricar</div>
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
        <div class="section-title">🧪 Materiales Requeridos</div>
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
                value=default_take_items,
                help="Los ingredientes se consumen al craftear"
            )
            
            use_currency = st.checkbox(
                "💰 Cobrar dinero",
                value=default_use_currency,
                help="Cobrar dinero además de ingredientes"
            )
            
            if use_currency:
                currency_type = st.selectbox(
                    "Tipo de moneda",
                    options=[0, 1],
                    index=default_currency_type,
                    format_func=lambda x: "💵 Cash ($)" if x == 0 else "🪙 Gold (oro)"
                )
            else:
                currency_type = 0
        
        with col_adv2:
            location = st.number_input(
                "📍 Location ID",
                min_value=0,
                value=default_location,
                help="ID de ubicación para el crafteo"
            )
            
            anim_keys = list(ANIMACIONES.keys())
            anim_default_idx = anim_keys.index(default_animation) if default_animation in anim_keys else 0
            
            animation = st.selectbox(
                "🎬 Animación",
                options=anim_keys,
                index=anim_default_idx,
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
        
        # Usar la categoría seleccionada por el usuario
        job_value = job_data['job_value']
        
        datos_crafteo = {
            'nombre': nombre,
            'descripcion': descripcion,
            'categoria': categoria_crafteo,
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
        
        # ===== MODO EDICIÓN: Guardar cambios =====
        if st.session_state.modo_edicion and st.session_state.nombre_original:
            st.markdown("""
            <div class="section-card">
                <div class="section-title">✏️ Guardar Cambios en Config</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.info(f"📝 Editando crafteo: **{st.session_state.nombre_original}** → **{nombre}**")
            
            config_editado = replace_crafting_in_config(
                job_seleccionado, 
                st.session_state.nombre_original, 
                codigo_lua
            )
            
            if config_editado:
                st.download_button(
                    label=f"📥 Descargar config_{job_seleccionado}.lua editado",
                    data=config_editado,
                    file_name=f"config_{job_seleccionado}.lua",
                    mime="text/plain",
                    use_container_width=True,
                    type="primary",
                    key="download_edited_config"
                )
                
                with st.expander("👁️ Ver preview del config editado", expanded=False):
                    st.code(config_editado, language="lua")
            else:
                st.error("⚠️ No se pudo encontrar el crafteo original para reemplazar")
        
        # ===== MODO CREACIÓN: Añadir nuevo =====
        else:
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
