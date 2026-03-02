from flask import Blueprint
from app.controllers import CharacterController

character_bp = Blueprint('characters', __name__, url_prefix='/api/characters')

# Rotas
character_bp.route('/', methods=['GET'])(CharacterController.get_all_characters)
character_bp.route('/<int:character_id>', methods=['GET'])(CharacterController.get_character_by_id)