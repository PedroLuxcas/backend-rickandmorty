from flask import Flask, request, jsonify
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
    
    #  CORS: Libera tudo (para teste)
    CORS(app, origins="*", supports_credentials=True)
    
    #  Rota de teste para verificar se o backend está online
    @app.route('/api/health', methods=['GET'])
    def health():
        return jsonify({"status": "ok", "message": "API is running"}), 200
    
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
        print("🏭 Production mode")
    
    return app