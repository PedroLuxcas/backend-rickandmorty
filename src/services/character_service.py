from src.repositories import CharacterRepository

class CharacterService:
    @staticmethod
    def get_all_characters():
        characters = CharacterRepository.get_all()
        return [char.to_dict() for char in characters]

    @staticmethod
    def get_character_by_id(character_id):
        character = CharacterRepository.get_by_id(character_id)
        return character.to_dict_complete() if character else None

    @staticmethod
    def get_characters_by_status(status):
        characters = CharacterRepository.get_by_status(status)
        return [char.to_dict() for char in characters]

    @staticmethod
    def search_characters(name):
        characters = CharacterRepository.search_by_name(name)
        return [char.to_dict() for char in characters]
    
    @staticmethod
    def get_characters_by_species(species):
        characters = CharacterService.get_by_species(species)
        return [char.to_dict() for char in characters]

    @staticmethod
    def create_character(data):
        new_character = CharacterRepository.create(data)
        return new_character.to_dict()

    @staticmethod
    def update_character(character_id, data):
        character = CharacterRepository.update(character_id, data)
        return character.to_dict() if character else None
    
    @staticmethod
    def delete_character(character_id):
        return CharacterRepository.delete(character_id)