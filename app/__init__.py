from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from config import config_by_name

db = SQLAlchemy()
ma = Marshmallow()

def create_app(config_name='default'):
    app = Flask(__name__)
    
    # Configuration
    app.config.from_object(config_by_name[config_name])
    
    # ⭐ CONFIGURAÇÃO CORS MAIS ESPECÍFICA
    CORS(app, resources={
        r"/api/*": {  # Aplica apenas para rotas /api/*
            "origins": ["http://localhost:3000", "http://localhost:5173"],  # Frontend URLs
            "methods": ["GET", "POST", "PUT", "DELETE"],
            "allow_headers": ["Content-Type"]
        }
    })
    
    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)
    
    # Registers blueprints
    from app.routes import character_bp
    app.register_blueprint(character_bp)
    
    # Create tables (development only)
    with app.app_context():
        db.create_all()
        print("✅ Database synchronized")
    
    return app