"""
Script de autenticación con Google Drive
=========================================
Ejecutar UNA VEZ para generar el archivo token.json necesario.

Prerequisitos:
1. Tener un archivo 'credentials.json' en esta misma carpeta
   (descargado desde Google Cloud Console)
2. Tener acceso a un navegador web

Uso:
    python authenticate_drive.py
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent
CREDENTIALS_FILE = BASE_DIR / 'credentials.json'
TOKEN_FILE = BASE_DIR / 'token.json'
SCOPES = ['https://www.googleapis.com/auth/drive']


def main():
    print("=" * 60)
    print("  Autenticación con Google Drive")
    print("=" * 60)
    print()
    
    # Verificar que existe credentials.json
    if not CREDENTIALS_FILE.exists():
        print("❌ ERROR: No se encontró 'credentials.json'")
        print()
        print("Para obtenerlo:")
        print("  1. Ve a https://console.cloud.google.com/")
        print("  2. Crea un proyecto (o usa uno existente)")
        print("  3. Habilita la API de Google Drive:")
        print("     → APIs y servicios → Biblioteca → busca 'Google Drive API' → Habilitar")
        print("  4. Crea credenciales OAuth 2.0:")
        print("     → APIs y servicios → Credenciales → Crear credenciales")
        print("     → ID de cliente OAuth → Tipo: Aplicación de escritorio")
        print("  5. Descarga el JSON y renómbralo a 'credentials.json'")
        print(f"  6. Colócalo en: {BASE_DIR}")
        print()
        print("  NOTA: En 'Pantalla de consentimiento OAuth', añade tu email como")
        print("  usuario de prueba si el proyecto está en modo 'Pruebas'.")
        sys.exit(1)
    
    print(f"✅ Encontrado: {CREDENTIALS_FILE}")
    print()
    
    try:
        from google_auth_oauthlib.flow import InstalledAppFlow
        from google.oauth2.credentials import Credentials
        from google.auth.transport.requests import Request
    except ImportError:
        print("❌ ERROR: Faltan dependencias. Instálalas con:")
        print("  pip install google-auth-oauthlib google-api-python-client")
        sys.exit(1)
    
    # Verificar si ya existe un token válido
    if TOKEN_FILE.exists():
        print(f"⚠️  Ya existe un token en: {TOKEN_FILE}")
        creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)
        if creds and creds.valid:
            print("✅ El token existente es válido. No es necesario re-autenticarse.")
            print()
            choice = input("¿Quieres generar un token nuevo de todas formas? (s/n): ").strip().lower()
            if choice != 's':
                print("Usando token existente.")
                return
        elif creds and creds.expired and creds.refresh_token:
            print("🔄 Token expirado, renovando...")
            try:
                creds.refresh(Request())
                with open(TOKEN_FILE, 'w') as f:
                    f.write(creds.to_json())
                print("✅ Token renovado correctamente.")
                return
            except Exception as e:
                print(f"⚠️  No se pudo renovar: {e}")
                print("Generando token nuevo...")
    
    # Iniciar flujo OAuth2
    print("🌐 Se abrirá el navegador para autorizar la aplicación...")
    print("   Inicia sesión con la cuenta de Google que tiene acceso a la carpeta de Drive.")
    print()
    
    try:
        flow = InstalledAppFlow.from_client_secrets_file(str(CREDENTIALS_FILE), SCOPES)
        creds = flow.run_local_server(port=0)
        
        # Guardar token
        with open(TOKEN_FILE, 'w') as f:
            f.write(creds.to_json())
        
        print()
        print("=" * 60)
        print(f"✅ ¡Autenticación exitosa!")
        print(f"   Token guardado en: {TOKEN_FILE}")
        print()
        print("   Ahora puedes ejecutar la aplicación:")
        print("   streamlit run app_crafteo.py")
        print("=" * 60)
        
    except Exception as e:
        print(f"❌ Error durante la autenticación: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
