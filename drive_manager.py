"""
Google Drive Manager para Config Generator
Gestiona la lectura/escritura de archivos Lua en una carpeta de Google Drive.
"""

import os
import json
from pathlib import Path

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaInMemoryUpload

# ============================================================================
# CONFIGURACIÓN
# ============================================================================

SCOPES = ['https://www.googleapis.com/auth/drive']
FOLDER_ID = '1gS373cidiKlUqb3FfxgvwlwmZ6odFaEO'

BASE_DIR = Path(__file__).parent
TOKEN_FILE = BASE_DIR / 'token.json'
CREDENTIALS_FILE = BASE_DIR / 'credentials.json'

# ============================================================================
# ESTADO GLOBAL
# ============================================================================

_service = None
_file_cache = {}  # filename -> file_id


# ============================================================================
# AUTENTICACIÓN
# ============================================================================

def get_service():
    """
    Obtiene el servicio autenticado de Google Drive.
    Usa token.json existente o lanza error si no hay credenciales.
    
    Returns:
        googleapiclient.discovery.Resource: Servicio de Drive autenticado
    
    Raises:
        FileNotFoundError: Si no existe credentials.json ni token.json
        Exception: Si la autenticación falla
    """
    global _service
    
    if _service is not None:
        return _service
    
    creds = None
    
    # Intentar cargar token existente
    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)
    
    # Si no hay credenciales válidas
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            # Token expirado pero con refresh_token → renovar
            creds.refresh(Request())
            # Guardar token renovado
            with open(TOKEN_FILE, 'w') as f:
                f.write(creds.to_json())
        else:
            # No hay token válido → necesita autenticación
            raise FileNotFoundError(
                "No se encontró un token válido de Google Drive.\n"
                "Ejecuta 'python authenticate_drive.py' para autenticarte."
            )
    
    _service = build('drive', 'v3', credentials=creds)
    return _service


def reset_service():
    """Resetea el servicio (útil si el token expira durante la sesión)"""
    global _service
    _service = None


def is_authenticated():
    """
    Verifica si hay una conexión válida con Google Drive.
    
    Returns:
        bool: True si la autenticación es válida
    """
    try:
        service = get_service()
        # Test rápido: listar 1 archivo
        service.files().list(pageSize=1).execute()
        return True
    except Exception:
        return False


def has_credentials():
    """Verifica si existe el archivo credentials.json"""
    return CREDENTIALS_FILE.exists()


def has_token():
    """Verifica si existe un token.json"""
    return TOKEN_FILE.exists()


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
