"""
Google Drive Manager para Config Generator
Gestiona la lectura/escritura de archivos Lua en una carpeta de Google Drive.
Usa una cuenta de servicio (Service Account) configurada vía st.secrets.
"""

import json
import os
import tempfile
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaInMemoryUpload

# ============================================================================
# CONFIGURACIÓN
# ============================================================================

SCOPES = ['https://www.googleapis.com/auth/drive']
FOLDER_ID = '1gS373cidiKlUqb3FfxgvwlwmZ6odFaEO'

# ============================================================================
# ESTADO GLOBAL
# ============================================================================

_service = None
_file_cache = {}  # filename -> file_id


# ============================================================================
# AUTENTICACIÓN CON SERVICE ACCOUNT
# ============================================================================

def _debug_private_key(pk: str) -> str:
    """Genera un diagnóstico detallado del private_key para depuración."""
    import re
    import base64
    
    lines = pk.split('\n')
    non_empty = [l for l in lines if l.strip()]
    info = []
    info.append(f"Longitud total: {len(pk)} chars")
    info.append(f"Líneas totales: {len(lines)}, no vacías: {len(non_empty)}")
    info.append(f"Tipo: {type(pk).__name__}")
    
    # Verificar estructura PEM
    has_begin = '-----BEGIN PRIVATE KEY-----' in pk or '-----BEGIN RSA PRIVATE KEY-----' in pk
    has_end = '-----END PRIVATE KEY-----' in pk or '-----END RSA PRIVATE KEY-----' in pk
    info.append(f"Tiene BEGIN: {has_begin}, Tiene END: {has_end}")
    
    # Verificar \n literales vs reales
    literal_backslash_n = pk.count('\\n')
    real_newlines = pk.count('\n')
    info.append(f"Newlines reales: {real_newlines}, Literales \\n: {literal_backslash_n}")
    
    # Detectar \r (Windows line endings)
    cr_count = pk.count('\r')
    if cr_count:
        info.append(f"⚠ Tiene \\r (carriage return): {cr_count}")
    
    # Detectar caracteres invisibles problemáticos
    invisible_chars = {}
    for i, c in enumerate(pk):
        cp = ord(c)
        if cp > 127:
            invisible_chars[f"U+{cp:04X}"] = invisible_chars.get(f"U+{cp:04X}", 0) + 1
        elif cp < 32 and c not in '\n\r\t':
            invisible_chars[f"0x{cp:02X}"] = invisible_chars.get(f"0x{cp:02X}", 0) + 1
    if invisible_chars:
        info.append(f"⚠ Caracteres invisibles/non-ASCII: {invisible_chars}")
    
    # Verificar espacios al final de las líneas
    lines_with_trailing = [i+1 for i, l in enumerate(lines) if l != l.rstrip(' \t')]
    if lines_with_trailing:
        info.append(f"⚠ Líneas con espacios al final: {lines_with_trailing[:5]}")
    
    if non_empty:
        info.append(f"Primera línea: {repr(non_empty[0][:60])}")
        info.append(f"Última línea: {repr(non_empty[-1][:60])}")
    
    # Verificar body base64
    if len(non_empty) > 2:
        body_lines = non_empty[1:-1]
        body = ''.join(l.strip() for l in body_lines)
        invalid_chars_set = set(re.findall(r'[^A-Za-z0-9+/=]', body))
        if invalid_chars_set:
            info.append(f"⚠ Caracteres inválidos en body: {invalid_chars_set}")
        else:
            info.append(f"Body base64: {len(body)} chars, OK")
        
        # Intentar decodificar base64
        try:
            decoded = base64.b64decode(body)
            info.append(f"Base64 decodificado: {len(decoded)} bytes")
            info.append(f"Primeros 8 bytes (hex): {decoded[:8].hex()}")
            # PKCS#8 empieza con 0x30 (SEQUENCE)
            if decoded[0] == 0x30:
                info.append("Estructura ASN.1: Empieza con SEQUENCE (0x30) ✓")
            else:
                info.append(f"⚠ Estructura ASN.1: Primer byte es 0x{decoded[0]:02X}, esperado 0x30")
        except Exception as b64_err:
            info.append(f"⚠ Error decodificando base64: {b64_err}")
        
        # Intentar cargar con cryptography directamente
        try:
            from cryptography.hazmat.primitives.serialization import load_pem_private_key
            load_pem_private_key(pk.encode('utf-8'), password=None)
            info.append("✓ cryptography.load_pem_private_key: ÉXITO")
        except Exception as crypto_err:
            info.append(f"✗ cryptography.load_pem_private_key: {type(crypto_err).__name__}: {crypto_err}")
            # Intentar con la key limpia (sin \r, sin trailing spaces)
            try:
                clean_pk = '\n'.join(l.rstrip() for l in pk.replace('\r', '').split('\n'))
                if not clean_pk.endswith('\n'):
                    clean_pk += '\n'
                load_pem_private_key(clean_pk.encode('utf-8'), password=None)
                info.append("✓ Con key limpia (sin \\r, sin trailing spaces): ÉXITO")
                info.append(">>> SOLUCIÓN: La key tiene \\r o trailing spaces")
            except Exception as crypto_err2:
                info.append(f"✗ Con key limpia: {type(crypto_err2).__name__}: {crypto_err2}")
    
    return '\n'.join(info)


def _normalize_private_key(pk: str) -> str:
    """Normaliza el private_key asegurando formato PEM limpio."""
    # Paso 1: Reemplazar \n literales (2 chars: backslash + n) por newlines reales
    pk = pk.replace('\\n', '\n')
    # Paso 2: Eliminar \r (Windows line endings)
    pk = pk.replace('\r', '')
    # Paso 3: Eliminar trailing spaces en cada línea
    pk = '\n'.join(line.rstrip() for line in pk.split('\n'))
    # Paso 4: Limpiar espacios sobrantes al inicio/final
    pk = pk.strip()
    # Paso 5: Asegurar que termina con newline (requerido por PEM)
    if not pk.endswith('\n'):
        pk += '\n'
    return pk


def get_service(secrets_info=None):
    """
    Obtiene el servicio autenticado de Google Drive.
    Acepta un dict-like (incluido AttrDict de Streamlit).
    """
    global _service
    
    if _service is not None:
        return _service
    
    if secrets_info is None:
        raise ValueError(
            "Se necesitan las credenciales de la cuenta de servicio.\n"
            "Configura [gcp_service_account] en los secrets de Streamlit."
        )
    
    creds = Credentials.from_service_account_info(secrets_info, scopes=SCOPES)
    _service = build('drive', 'v3', credentials=creds)
    return _service


def _get_service_via_file(secrets_dict: dict):
    """
    Método alternativo: escribe JSON temporal y usa from_service_account_file.
    """
    global _service
    tmp_fd, tmp_path = tempfile.mkstemp(suffix='.json', prefix='gcp_sa_')
    try:
        with os.fdopen(tmp_fd, 'w', encoding='utf-8') as f:
            json.dump(secrets_dict, f)
        creds = Credentials.from_service_account_file(tmp_path, scopes=SCOPES)
        _service = build('drive', 'v3', credentials=creds)
    finally:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
    return _service


def init_from_secrets(secrets_raw) -> tuple:
    """
    Inicializa la conexión a Drive usando los secrets de Streamlit.
    Intenta 3 métodos progresivos.
    
    Args:
        secrets_raw: st.secrets["gcp_service_account"] (AttrDict o dict)
    
    Returns:
        tuple: (success: bool, debug_info: str)
    """
    debug_lines = []
    pk_raw = secrets_raw.get('private_key', '')
    debug_lines.append("=== DIAGNÓSTICO PRIVATE KEY ===")
    debug_lines.append(_debug_private_key(str(pk_raw)))
    debug_lines.append("")
    
    # ─── INTENTO 1: Método oficial (pasar st.secrets directamente) ───
    debug_lines.append("--- Intento 1: Directo (método oficial Streamlit) ---")
    try:
        reset_service()
        service = get_service(secrets_raw)
        service.files().list(pageSize=1, q=f"'{FOLDER_ID}' in parents").execute()
        debug_lines.append("✓ Conexión exitosa con método directo!")
        return True, '\n'.join(debug_lines)
    except Exception as e1:
        reset_service()
        debug_lines.append(f"✗ Falló: {type(e1).__name__}: {e1}")
    
    # ─── INTENTO 2: Dict con private_key normalizado ───
    debug_lines.append("")
    debug_lines.append("--- Intento 2: Dict + normalización de private_key ---")
    try:
        reset_service()
        # Convertir a dict Python puro
        secrets_dict = dict(secrets_raw)
        for k, v in secrets_dict.items():
            if not isinstance(v, (str, int, float, bool, type(None))):
                secrets_dict[k] = str(v)
        # Normalizar private_key
        if 'private_key' in secrets_dict:
            secrets_dict['private_key'] = _normalize_private_key(str(secrets_dict['private_key']))
            debug_lines.append("  Key normalizada:")
            debug_lines.append('  ' + _debug_private_key(secrets_dict['private_key']).replace('\n', '\n  '))
        
        service = get_service(secrets_dict)
        service.files().list(pageSize=1, q=f"'{FOLDER_ID}' in parents").execute()
        debug_lines.append("✓ Conexión exitosa con dict normalizado!")
        return True, '\n'.join(debug_lines)
    except Exception as e2:
        reset_service()
        debug_lines.append(f"✗ Falló: {type(e2).__name__}: {e2}")
    
    # ─── INTENTO 3: Archivo JSON temporal ───
    debug_lines.append("")
    debug_lines.append("--- Intento 3: Archivo JSON temporal ---")
    try:
        reset_service()
        # Reconstruir dict limpio con JSON roundtrip
        clean_dict = json.loads(json.dumps({k: str(v) if not isinstance(v, (str, int, float, bool, type(None))) else v for k, v in dict(secrets_raw).items()}))
        if 'private_key' in clean_dict:
            clean_dict['private_key'] = _normalize_private_key(clean_dict['private_key'])
        
        service = _get_service_via_file(clean_dict)
        service.files().list(pageSize=1, q=f"'{FOLDER_ID}' in parents").execute()
        debug_lines.append("✓ Conexión exitosa con archivo temporal!")
        return True, '\n'.join(debug_lines)
    except Exception as e3:
        reset_service()
        debug_lines.append(f"✗ Falló: {type(e3).__name__}: {e3}")
    
    debug_lines.append("")
    debug_lines.append("=== TODOS LOS MÉTODOS FALLARON ===")
    debug_lines.append("Revisa que en Streamlit Cloud secrets tengas:")
    debug_lines.append('  [gcp_service_account]')
    debug_lines.append('  private_key = "-----BEGIN PRIVATE KEY-----\\nMIIE...\\n-----END PRIVATE KEY-----\\n"')
    debug_lines.append("Copia el valor EXACTO del campo private_key del JSON de Google.")
    debug_lines.append("Usa comillas dobles normales \"...\" (NO triples, NO simples).")
    
    return False, '\n'.join(debug_lines)


def reset_service():
    """Resetea el servicio (útil si falla la conexión)"""
    global _service
    _service = None


def is_authenticated():
    """
    Verifica si hay una conexión válida con Google Drive.
    
    Returns:
        bool: True si la autenticación es válida
    """
    try:
        if _service is None:
            return False
        _service.files().list(pageSize=1).execute()
        return True
    except Exception:
        return False


# ============================================================================
# OPERACIONES CON ARCHIVOS
# ============================================================================

def _get_file_id(filename: str) -> str:
    """
    Obtiene el ID de un archivo en Drive por nombre (con caché).
    
    Args:
        filename: Nombre del archivo (ej: 'config_armero.lua')
    
    Returns:
        str: ID del archivo o None si no existe
    """
    if filename in _file_cache:
        return _file_cache[filename]
    
    service = get_service()
    query = f"'{FOLDER_ID}' in parents and name = '{filename}' and trashed = false"
    results = service.files().list(q=query, fields="files(id, name)").execute()
    files = results.get('files', [])
    
    if files:
        _file_cache[filename] = files[0]['id']
        return files[0]['id']
    
    return None


def list_config_files() -> list:
    """
    Lista todos los archivos config_*.lua en la carpeta de Drive.
    
    Returns:
        list: Lista de dicts con 'id' y 'name' de cada archivo
    """
    service = get_service()
    query = (
        f"'{FOLDER_ID}' in parents "
        f"and name contains 'config_' "
        f"and name contains '.lua' "
        f"and trashed = false"
    )
    results = service.files().list(
        q=query, 
        fields="files(id, name)",
        orderBy="name"
    ).execute()
    
    files = results.get('files', [])
    
    # Actualizar caché
    for f in files:
        _file_cache[f['name']] = f['id']
    
    return files


def get_available_config_keys() -> list:
    """
    Obtiene las claves de jobs disponibles en Drive (ej: ['armero', 'medicos']).
    
    Returns:
        list: Lista ordenada de claves de jobs
    """
    files = list_config_files()
    keys = []
    for f in files:
        name = f['name']
        # config_armero.lua → armero
        key = name.replace('config_', '').replace('.lua', '')
        keys.append(key)
    return sorted(keys)


def read_file(filename: str) -> str:
    """
    Lee el contenido de un archivo desde Drive.
    
    Args:
        filename: Nombre del archivo (ej: 'config_armero.lua')
    
    Returns:
        str: Contenido del archivo o None si no existe
    """
    file_id = _get_file_id(filename)
    if not file_id:
        return None
    
    service = get_service()
    content = service.files().get_media(fileId=file_id).execute()
    return content.decode('utf-8')


def write_file(filename: str, content: str) -> bool:
    """
    Escribe/actualiza un archivo en la carpeta de Drive.
    Si el archivo ya existe, lo actualiza. Si no, lo crea.
    
    Args:
        filename: Nombre del archivo (ej: 'config_armero.lua')
        content: Contenido del archivo
    
    Returns:
        bool: True si se guardó correctamente
    """
    service = get_service()
    file_id = _get_file_id(filename)
    
    media = MediaInMemoryUpload(
        content.encode('utf-8'), 
        mimetype='text/plain',
        resumable=False
    )
    
    if file_id:
        # Actualizar archivo existente
        service.files().update(
            fileId=file_id,
            media_body=media
        ).execute()
    else:
        # Crear archivo nuevo
        file_metadata = {
            'name': filename,
            'parents': [FOLDER_ID]
        }
        result = service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()
        _file_cache[filename] = result['id']
    
    return True


def delete_file(filename: str) -> bool:
    """
    Elimina un archivo de la carpeta de Drive.
    
    Args:
        filename: Nombre del archivo (ej: 'config_armero.lua')
    
    Returns:
        bool: True si se eliminó correctamente, False si no existía
    """
    file_id = _get_file_id(filename)
    if not file_id:
        return False
    
    service = get_service()
    service.files().delete(fileId=file_id).execute()
    _file_cache.pop(filename, None)
    return True


def clear_cache():
    """Limpia la caché de IDs de archivos"""
    global _file_cache
    _file_cache = {}
