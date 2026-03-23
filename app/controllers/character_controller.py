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
        page = request.args.get('page', type=int)
        per_page = request.args.get('per_page', 20, type=int)
        
        result = self.service.get_all_characters(page, per_page)
        
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
        result = self.service.get_character_by_id(character_id)
        
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
        data = request.get_json()
        
        result = self.service.create_character(data)
        
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
        data = request.get_json()
        
        result = self.service.update_character(character_id, data)
        
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
        result = self.service.delete_character(character_id)
        
        return ApiResponse.success(
            data=result,
            message="Character deleted successfully"
        )
    
    def search_characters(self):
        """
        GET /api/characters/search?name=rick&page=1&per_page=20
        Search characters by name with pagination
        """
        print("🟠 PASSO 2: Controller search_characters foi chamado!")
        
        # Get query parameters
        name = request.args.get('name', '')
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 20, type=int)
        
        print(f"   Nome recebido: '{name}', página: {page}")
        
        # Validate
        if not name:
            print("❌ Nome vazio! Retornando erro 400")
            return ApiResponse.error(
                message="Name parameter is required",
                status_code=400
            )
        
        # Call service
        print("🟡 Chamando service.search_characters...")
        result = self.service.search_characters(name, page, per_page)
        print("✅ Service retornou resultado")
        
        return ApiResponse.success(
            data=result,
            message=f"Characters matching '{name}' retrieved successfully"
        )