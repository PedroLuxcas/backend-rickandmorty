import os
import sys

print("="*60)
print("🚀 INICIANDO APLICAÇÃO RICK AND MORTY API")
print("="*60)

print(f"📂 Diretório atual: {os.getcwd()}")
print(f"🔧 FLASK_ENV: {os.getenv('FLASK_ENV', 'não definido')}")
print(f"🛢️ DATABASE_URL: {os.getenv('DATABASE_URL', 'não definido')[:30]}...")

try:
    print("🔄 Importando create_app de app...")
    from app import create_app
    print("✅ Importação bem-sucedida!")
except Exception as e:
    print(f"❌ ERRO NA IMPORTAÇÃO: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

try:
    config_name = os.getenv('FLASK_ENV', 'production')
    print(f"🔄 Criando app com config_name='{config_name}'...")
    app = create_app(config_name)
    print("✅ App criado com sucesso!")
except Exception as e:
    print(f"❌ ERRO AO CRIAR APP: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

application = app

print("="*60)
print("✅ APLICAÇÃO INICIALIZADA COM SUCESSO!")
print("="*60)
