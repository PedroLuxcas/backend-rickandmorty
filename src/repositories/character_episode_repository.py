from src.models import CharacterEpisode
from src import db

class CharacterEpisodeRepository:
    @staticmethod
    def get_all():
        return CharacterEpisode.query.order_by(CharacterEpisode.character_id, CharacterEpisode.episode_id).all()
    
    @staticmethod
    def get_by_character(character_id):
        return CharacterEpisode.query.filter_by(character_id=character_id).order_by(CharacterEpisode.episode_id).all()
    
    @staticmethod
    def get_by_episode(episode_id):
        return CharacterEpisode.query.filter_by(episode_id=episode_id).order_by(CharacterEpisode.character_id).all()
    
    @staticmethod
    def get_by_both(character_id, episode_id):
        return CharacterEpisode.query.filter_by(character_id=character_id, episode_id=episode_id).first()
    
    @staticmethod
    def create(character_id, episode_id):
        relationship = CharacterEpisode(character_id=character_id, episode_id=episode_id)
        db.session.add(relationship)
        db.session.commit()
        return relationship
    
    @staticmethod
    def delete(character_id, episode_id):
        relationship = CharacterEpisode.query.filter_by(character_id=character_id, episode_id=episode_id).first()
        if relationship:
            db.session.delete(relationship)
            db.session.commit()
            return True
        return False