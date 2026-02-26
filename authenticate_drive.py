"""
Script de verificación de conexión con Google Drive
=====================================================
Verifica que los secrets de Streamlit están configurados correctamente
y que la cuenta de servicio tiene acceso a la carpeta de Drive.

Uso:
    python authenticate_drive.py
"""

import sys
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent
SECRETS_FILE = BASE_DIR / '.streamlit' / 'secrets.toml'


def main():
    print("=" * 60)
    print("  Verificación de conexión con Google Drive")
    print("=" * 60)
    print()
    
    # Verificar dependencias
    try:
        from google.oauth2.service_account import Credentials
        from googleapiclient.discovery import build
        print("✅ Dependencias instaladas correctamente")
    except ImportError:
        print("❌ Faltan dependencias. Instálalas con:")
        print("   pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib")
        sys.exit(1)
    
    # Verificar secrets.toml
    if SECRETS_FILE.exists():
        print(f"✅ Encontrado: {SECRETS_FILE}")
    else:
        print(f"⚠️  No se encontró: {SECRETS_FILE}")
        print("   (No es necesario en Streamlit Cloud, solo en local)")
        print()
        print("   Para desarrollo local:")
        print(f"   1. Crea la carpeta: {BASE_DIR / '.streamlit'}")
        print(f"   2. Crea el archivo: {SECRETS_FILE}")
        print("   3. Usa secrets.toml.example como referencia")
    
    print()
    
    # Intentar leer secrets
    try:
        # Intento 1: usar tomllib (Python 3.11+)
        try:
            import tomllib
            with open(SECRETS_FILE, 'rb') as f:
                secrets = tomllib.load(f)
        except (ImportError, ModuleNotFoundError):
            # Intento 2: toml (pip install toml)
            try:
                import toml
                secrets = toml.load(str(SECRETS_FILE))
            except ImportError:
                print("⚠️  Para verificación local, instala: pip install toml")
                print("   O usa Python 3.11+ (incluye tomllib)")
                sys.exit(0)
        
        if 'gcp_service_account' not in secrets:
            print("❌ No se encontró la sección [gcp_service_account] en secrets.toml")
            sys.exit(1)
        
        sa = secrets['gcp_service_account']
        print(f"✅ Cuenta de servicio: {sa.get('client_email', '???')}")
        print(f"   Proyecto: {sa.get('project_id', '???')}")
        
    except FileNotFoundError:
        print("❌ No se pudo abrir secrets.toml")
        sys.exit(1)
    
    # Verificar conexión a Drive
    print()
    print("🔄 Probando conexión a Google Drive...")
    
    try:
        import drive_manager
        
        if drive_manager.init_from_secrets(sa):
            print("✅ ¡Conexión exitosa!")
            
            # Listar archivos
            files = drive_manager.list_config_files()
            print(f"   Archivos encontrados: {len(files)}")
            for f in files[:5]:
                print(f"   - {f['name']}")
            if len(files) > 5:
                print(f"   ... y {len(files) - 5} más")
        else:
            print("❌ No se pudo conectar a Drive")
            print("   Verifica que la carpeta está compartida con la cuenta de servicio")
    
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
    
    print()
    print("=" * 60)
    print("  ✅ Todo listo para usar la aplicación")
    print("     streamlit run app_crafteo.py")
    print("=" * 60)


if __name__ == '__main__':
    main()
