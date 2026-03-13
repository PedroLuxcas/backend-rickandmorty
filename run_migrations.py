import os
import sys
from app import create_app, db

def run_migrations():
    config_name = os.getenv('FLASK_ENV', 'production')

    print(f"\n Iniciando migrações no ambiente: {config_name}")
    print("=" * 50)

    app = create_app(config_name)

    with app.app_context():
        try:
            print("Conectando ao banco de dados...")
            print(f" URL: {app.config.get('SQALCHEMY_DATABASE_URI', 'Não configurado')}")

            db.create_all()
            print(" Tabelas criadas/verificadas com sucesso!")

            return True

        except Exception as e:
            print(f"Erro ao criar tabelas: {e}")
            return False
        
if __name__ == "__main__":
    sucess = run_migrations()
    sys.exit(0 if sucess else 1)