"""
Character Controller
Handles HTTP requests for character endpoints.
"""

from flask import request
from app.services import CharacterService
from app.utils.api_response import ApiResponse

class CharacterController:
    """Controller for character-related HTTP requests"""
    
    def __init__(self, service=None):
        """
        Initialize controller with service dependency.
        
        Args:
            service: CharacterService instance (optional, for dependency injection)
        """
        self.service = service or CharacterService()
    
    def get_all_characters(self):
        """
        GET /api/characters/
        Retrieve all characters with optional pagination.
        
        Query Parameters:
            page (int): Page number (optional)
            per_page (int): Items per page, default 20
            
        Returns:
            JSON response with paginated or all characters
        """
        # Get pagination parameters from query string
        page = request.args.get('page', type=int)
        per_page = request.args.get('per_page', 20, type=int)
        
        # Delegate to service layer
        result = self.service.get_all_characters(page, per_page)
        
        # Return standardized success response
        return ApiResponse.success(
            data=result,
            message="Characters retrieved successfully"
        )
    
    def get_character_by_id(self, character_id):
        """
        GET /api/characters/<id>
        Retrieve a specific character by ID.
        
        Args:
            character_id (int): Character ID from URL
            
        Returns:
            JSON response with character details
        """
        # Delegate to service layer
        result = self.service.get_character_by_id(character_id)
        
        # Return standardized success response
        return ApiResponse.success(
            data=result,
            message="Character retrieved successfully"
        )
    
    def create_character(self):
        """
        POST /api/characters/
        Create a new character.
        
        Request Body:
            JSON with character data (name, status, species, etc.)
            
        Returns:
            JSON response with created character
        """
        # Parse JSON request body
        data = request.get_json()
        
        # Delegate to service layer
        result = self.service.create_character(data)
        
        # Return standardized success response with 201 Created
        return ApiResponse.success(
            data=result,
            message="Character created successfully",
            status_code=201
        )
    
    def update_character(self, character_id):
        """
        PUT /api/characters/<id>
        Update an existing character.
        
        Args:
            character_id (int): Character ID from URL
            
        Request Body:
            JSON with fields to update
            
        Returns:
            JSON response with updated character
        """
        # Parse JSON request body
        data = request.get_json()
        
        # Delegate to service layer
        result = self.service.update_character(character_id, data)
        
        # Return standardized success response
        return ApiResponse.success(
            data=result,
            message="Character updated successfully"
        )
    
    def delete_character(self, character_id):
        """
        DELETE /api/characters/<id>
        Delete a character.
        
        Args:
            character_id (int): Character ID from URL
            
        Returns:
            JSON response with deletion confirmation
        """
        # Delegate to service layer
        result = self.service.delete_character(character_id)
        
        # Return standardized success response
        return ApiResponse.success(
            data=result,
            message="Character deleted successfully"
        )