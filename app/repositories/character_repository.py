from app.models import Character
from app import db

class CharacterRepository:
    """Repository for character data access"""
    
    def __init__(self, model_class=None):
        self.model = model_class or Character
    
    def get_all(self):
        """Get all characters ordered by ID"""
        return self.model.query.order_by(self.model.id).all()
    
    def get_all_paginated(self, page=1, per_page=20):
        """Get characters with pagination"""
        return self.model.query.order_by(self.model.id).paginate(
            page=page,
            per_page=per_page,
            error_out=False
        )
    
    def get_by_id(self, character_id):
        """Get character by ID"""
        return self.model.query.get(character_id)
    
    def create(self, data):
        """Create a new character"""
        character = self.model(**data)
        db.session.add(character)
        db.session.commit()
        return character
    
    def update(self, character_id, data):
        """Update an existing character"""
        character = self.get_by_id(character_id)
        if character:
            for key, value in data.items():
                setattr(character, key, value)
            db.session.commit()
        return character
    
    def delete(self, character_id):
        """Delete a character"""
        character = self.get_by_id(character_id)
        if character:
            db.session.delete(character)
            db.session.commit()
            return True
        return False
    
    def search_by_name(name: str, page: int = 1, per_page: int = 20):
        """
        Search characters by name with pagination
        Uses ilike for case-insensitive search
        """
        return Character.query.filter(
            Character.name.ilike(f'%{name}%')
        ).order_by(Character.id).paginate(
            page=page,
            per_page=per_page,
            error_out=False
        )