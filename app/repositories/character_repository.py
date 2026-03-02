from app.models import Character

class CharacterRepository:
    """Database access layer"""
    
    def get_all():
        """Returns all characters ordered by ID"""
        return Character.query.order_by(Character.id).all()
    
    def get_all_paginated(page=1, per_page=20):
        """Returns characters with pagination"""
        return Character.query.order_by(Character.id).paginate(
            page=page,
            per_page=per_page,
            error_out=False
        )
    
    def get_by_id(character_id):
        """Returns a character by ID"""
        return Character.query.get(character_id)