from flask import request
from app.services import CharacterService
from app.utils.api_response import ApiResponse

class CharacterController:
    
    def get_all_characters():
        page = request.args.get('page', type=int)
        per_page = request.args.get('per_page', 20, type=int)
        
        if page:
            result = CharacterService.get_all_characters(page, per_page)
            return ApiResponse.success(
                data=result,
                message="Characters retrieved successfully"
            )
        else:
            characters = CharacterService.get_all_characters()
            return ApiResponse.success(
                data=characters,
                message="All characters retrieved successfully"
            )

    def get_character_by_id(character_id):
        character = CharacterService.get_character_by_id(character_id)
        
        if character:
            return ApiResponse.success(
                data=character,
                message="Character retrieved successfully"
            )
        
        return ApiResponse.not_found("Character")