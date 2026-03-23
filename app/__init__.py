from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from config import config_by_name
import os

db = SQLAlchemy()
ma = Marshmallow()

def create_app(config_name='default'):
    app = Flask(__name__)
    
    # Configuration
    app.config.from_object(config_by_name[config_name])
    
    frontend_urls = [
        "http://localhost:3000",
        "http://localhost:5173",
        "https://frontend-rickandmorty.vercel.app",
        "http://frontend-rickandmorty.vercel.app"
    ]
    
    # Configuração simplificada e mais permissiva
    CORS(app, origins=frontend_urls, supports_credentials=True)
    
    
    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)
    
    # Registers blueprints
    from app.routes import character_bp
    app.register_blueprint(character_bp)
    
    # Create tables ONLY in development
    if app.config.get('DEBUG', False):
        with app.app_context():
            db.create_all()
            print("✅ Database synchronized (development only)")
    else:
        print("🏭 Production mode - tables must be created manually or via migrations")
    
    return app