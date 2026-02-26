from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import config_by_name

db = SQLAlchemy()
ma = Marshmallow()

def create_app(config_name='default'):
    app = Flask(__name__)
    
    # Carrega configurações
    app.config.from_object(config_by_name[config_name])
    
    # Inicializa extensões
    db.init_app(app)
    ma.init_app(app)
    
    # Registra blueprints
    from src.routes.character_routes import character_bp
    from src.routes.episode_routes import episode_bp
    from src.routes.location_routes import location_bp
    from src.routes.character_episode_routes import character_episode_bp
    
    app.register_blueprint(character_bp)
    app.register_blueprint(episode_bp)
    app.register_blueprint(location_bp)
    app.register_blueprint(character_episode_bp)
    
    # Cria tabelas no banco
    with app.app_context():
        db.create_all()
        print("✅ Banco de dados sincronizado!")
    
    return app