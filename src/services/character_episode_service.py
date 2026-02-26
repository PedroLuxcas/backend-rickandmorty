from src.repositories import CharacterEpisodeRepository, CharacterRepository, EpisodeRepository

class CharacterEpisodeService:
    @staticmethod
    def get_all_relationships():
        relationships = CharacterEpisodeRepository.get_all()
        return [rel.to_dict() for rel in relationships]
    
    @staticmethod
    def get_by_character(character_id):
        character = CharacterRepository.get_by_id(character_id)
        if not character:
            return None
        
        relationships = CharacterEpisodeRepository.get_by_character(character_id)
        return {
            'character': character.to_dict(),
            'episodes': [{'id': rel.episode_id, 
                         'name': rel.episode.name, 
                         'code': rel.episode.episode} 
                        for rel in relationships if rel.episode]
        }
    
    @staticmethod
    def get_by_episode(episode_id):
        episode = EpisodeRepository.get_by_id(episode_id)
        if not episode:
            return None
        
        relationships = CharacterEpisodeRepository.get_by_episode(episode_id)
        return {
            'episode': episode.to_dict(),
            'characters': [{'id': rel.character_id,
                           'name': rel.character.name,
                           'status': rel.character.status}
                          for rel in relationships if rel.character]
        }
    
    @staticmethod
    def add_relationship(character_id, episode_id):
        character = CharacterRepository.get_by_id(character_id)
        episode = EpisodeRepository.get_by_id(episode_id)
        
        if not character or not episode:
            return None
        
        existing = CharacterEpisodeRepository.get_by_both(character_id, episode_id)
        if existing:
            return {'message': 'Relationship already exists', 'data': existing.to_dict()}
        
        relationship = CharacterEpisodeRepository.create(character_id, episode_id)
        return relationship.to_dict()
    
    @staticmethod
    def remove_relationship(character_id, episode_id):
        return CharacterEpisodeRepository.delete(character_id, episode_id)