from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from config import config_by_name
import os

db = SQLAlchemy()
ma = Marshmallow()

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    
    # ⭐ CORS PRIMEIRO
    CORS(app, origins="*", supports_credentials=True)
    
    # ⭐ HANDLER GLOBAL PARA GARANTIR CORS
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        return response
    
    # Rota de teste
    @app.route('/api/health', methods=['GET', 'OPTIONS'])
    def health():
        if request.method == 'OPTIONS':
            return '', 200
        return jsonify({"status": "ok", "message": "API is running"}), 200
    
    db.init_app(app)
    ma.init_app(app)
    
    from app.routes import character_bp
    app.register_blueprint(character_bp)
    
    if app.config.get('DEBUG', False):
        with app.app_context():
            db.create_all()
            print("✅ Database synchronized (development only)")
    
    return app