"""
Character Routes
Defines URL endpoints for character-related operations.
"""

from flask import Blueprint, request  # ← IMPORT request
from app.controllers import CharacterController

# Create blueprint for character endpoints
character_bp = Blueprint('characters', __name__, url_prefix='/api/characters')

# ⭐ Create a SINGLE INSTANCE of the controller (Option 2)
character_controller = CharacterController()

# ============ GET ROUTES ============

@character_bp.route('/', methods=['GET'])
def get_all_characters():
    """GET /api/characters/ - List all characters (paginated)"""
    return character_controller.get_all_characters()

@character_bp.route('/<int:character_id>', methods=['GET'])
def get_character_by_id(character_id):
    """GET /api/characters/<id> - Get character by ID"""
    return character_controller.get_character_by_id(character_id)

# ⭐ NOVA ROTA DE SEARCH
@character_bp.route('/search', methods=['GET'])
def search_characters():
    """GET /api/characters/search?name=rick&page=1 - Search characters by name"""
    return character_controller.search_characters()

# ============ POST ROUTES ============

@character_bp.route('/', methods=['POST'])
def create_character():
    """POST /api/characters/ - Create a new character"""
    return character_controller.create_character()

# ============ PUT ROUTES ============

@character_bp.route('/<int:character_id>', methods=['PUT'])
def update_character(character_id):
    """PUT /api/characters/<id> - Update an existing character"""
    return character_controller.update_character(character_id)

# ============ DELETE ROUTES ============

@character_bp.route('/<int:character_id>', methods=['DELETE'])
def delete_character(character_id):
    """DELETE /api/characters/<id> - Delete a character"""
    return character_controller.delete_character(character_id)
