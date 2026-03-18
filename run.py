import os
import sys

print("="*60)
print("🚀 INICIANDO APLICAÇÃO RICK AND MORTY API")
print("="*60)

print(f"📂 Diretório atual: {os.getcwd()}")
print(f"🔧 FLASK_ENV: {os.getenv('FLASK_ENV', 'não definido')}")
print(f"🛢️ DATABASE_URL: {os.getenv('DATABASE_URL', 'não definido')[:30]}...")

try:
    from app import create_app
    print("✅ Importação bem-sucedida!")
except Exception as e:
    print(f"❌ ERRO NA IMPORTAÇÃO: {e}")
    sys.exit(1)

try:
    config_name = os.getenv('FLASK_ENV', 'production')
    print(f"🔄 Criando app com config_name='{config_name}'...")
    app = create_app(config_name)
    print("✅ App criado com sucesso!")
except Exception as e:
    print(f"❌ ERRO AO CRIAR APP: {e}")
    sys.exit(1)

application = app

print("="*60)
print("✅ APLICAÇÃO INICIALIZADA COM SUCESSO!")
print("="*60)

if __name__ == "__main__":
    port = int(os.getenv('PORT', 5000))
    print(f"🚀 Servidor rodando na porta {port}")
    app.run(host='0.0.0.0', port=port)