from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import config_by_name

db = SQLAlchemy()
ma = Marshmallow()

def create_app(config_name='default'):
    app = Flask(__name__)
    
    # Configuration
    app.config.from_object(config_by_name[config_name])
    
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