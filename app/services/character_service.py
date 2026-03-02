from app.repositories import CharacterRepository
from app.schemas.characters_schema import character_schema, characters_schema  # ← CORRIGIDO

class CharacterService:
    """Business layer"""
    
    @staticmethod
    def get_all_characters(page=None, per_page=None):
        """Returns all characters"""
        if page and per_page:
            # with pagination
            pagination = CharacterRepository.get_all_paginated(page, per_page)
            return {
                'items': characters_schema.dump(pagination.items), 
                'total': pagination.total,
                'page': pagination.page,
                'pages': pagination.pages,
                'per_page': pagination.per_page,
                'has_next': pagination.has_next,
                'has_prev': pagination.has_prev
            }
        else:
            # without pagination
            characters = CharacterRepository.get_all()
            return characters_schema.dump(characters) 
    
    @staticmethod
    def get_character_by_id(character_id):
        """Returns a character by ID"""
        character = CharacterRepository.get_by_id(character_id)
        if character:
            return character_schema.dump(character) 
        return None