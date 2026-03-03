from app.repositories import CharacterRepository
from app.schemas.characters_schema import character_schema, characters_schema
from app.utils.exceptions import NotFoundError, BusinessLogicError, DatabaseError
from sqlalchemy.exc import SQLAlchemyError

class CharacterService:
    """Business logic layer for characters"""
    
    def __init__(self, repository=None, schema=None, many_schema=None):
        """
        Initialize service with dependencies
        Allows dependency injection for testing
        """
        self.repository = repository or CharacterRepository()
        self.schema = schema or character_schema
        self.many_schema = many_schema or characters_schema
    
    def get_all_characters(self, page=None, per_page=20):
        """
        Get all characters with optional pagination
        """
        try:
            if page:
                pagination = self.repository.get_all_paginated(page, per_page)
                
                if pagination.total == 0:
                    raise NotFoundError("No characters found")
                
                return {
                    'items': self.many_schema.dump(pagination.items),
                    'total': pagination.total,
                    'page': pagination.page,
                    'pages': pagination.pages,
                    'per_page': pagination.per_page,
                    'has_next': pagination.has_next,
                    'has_prev': pagination.has_prev
                }
            else:
                characters = self.repository.get_all()
                
                if not characters:
                    raise NotFoundError("No characters found")
                
                return self.many_schema.dump(characters)
                
        except SQLAlchemyError as e:
            raise DatabaseError("Failed to fetch characters", detail=str(e))
    
    def get_character_by_id(self, character_id):
        """
        Get a specific character by ID
        """
        try:
            character = self.repository.get_by_id(character_id)
            
            if not character:
                raise NotFoundError("Character", character_id)
            
            return self.schema.dump(character)
            
        except SQLAlchemyError as e:
            raise DatabaseError(f"Failed to fetch character {character_id}", 
                              detail=str(e))
    
    def create_character(self, data):
        """
        Create a new character
        """
        try:
            # Validation
            if not data.get('name'):
                from app.utils.exceptions import ValidationError
                raise ValidationError("Character name is required", 
                                     errors={"name": "This field is required"})
            
            # Business logic
            if len(data.get('name', '')) < 3:
                raise BusinessLogicError(
                    "Character name must be at least 3 characters long",
                    data={"name": data.get('name')}
                )
            
            # Check if character already exists
            existing = self.repository.get_by_id(data.get('id'))
            if existing:
                raise BusinessLogicError(
                    f"Character with ID {data.get('id')} already exists",
                    data={"id": data.get('id')}
                )
            
            # Create character
            new_character = self.repository.create(data)
            return self.schema.dump(new_character)
            
        except SQLAlchemyError as e:
            raise DatabaseError("Failed to create character", detail=str(e))
    
    def update_character(self, character_id, data):
        """
        Update an existing character
        """
        try:
            character = self.repository.get_by_id(character_id)
            
            if not character:
                raise NotFoundError("Character", character_id)
            
            # Validation
            if 'name' in data and len(data['name']) < 3:
                from app.utils.exceptions import ValidationError
                raise ValidationError(
                    "Character name must be at least 3 characters",
                    errors={"name": "Minimum length is 3"}
                )
            
            updated = self.repository.update(character_id, data)
            return self.schema.dump(updated)
            
        except SQLAlchemyError as e:
            raise DatabaseError(f"Failed to update character {character_id}", 
                              detail=str(e))
    
    def delete_character(self, character_id):
        """
        Delete a character
        """
        try:
            character = self.repository.get_by_id(character_id)
            
            if not character:
                raise NotFoundError("Character", character_id)
            
            # Business logic - prevent deleting main characters
            if character.name in ['Rick Sanchez', 'Morty Smith']:
                raise BusinessLogicError(
                    f"Cannot delete main character: {character.name}",
                    data={"character_id": character_id, "name": character.name}
                )
            
            success = self.repository.delete(character_id)
            
            if not success:
                raise DatabaseError(f"Failed to delete character {character_id}")
            
            return {"message": f"Character {character_id} deleted successfully"}
            
        except SQLAlchemyError as e:
            raise DatabaseError(f"Failed to delete character {character_id}", 
                              detail=str(e))