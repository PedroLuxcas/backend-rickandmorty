from src.models import Episode
from src import db

class EpisodeRepository:
    
        @staticmethod
        def get_all():
            return Episode.query.order_by(Episode.id).all()

        @staticmethod
        def get_by_id(episode_id):
            return Episode.query.get(episode_id)
        
        @staticmethod
        def get_by_code(episode_code):
            return Episode.query.filter_by(episode=episode_code).first()

        @staticmethod
        def get_by_season(season):
            return Episode.query.filter(Episode.episode.like(f'{season}%')).order_by(Episode.episode).all()

        @staticmethod
        def search_by_name(name):
            return Episode.query.filter(Episode.name.ilike(f'%{name}%')).all()
            
        @staticmethod 
        def create(data):
            episode = Episode(**data)
            db.session.add(episode)
            db.session.commit()
            return episode
        
        @staticmethod
        def update(episode_id, data):
            episode = Episode.query.get(episode_id)
            if episode:
                for key, value in data.items():
                    setattr(episode, key, value)
                db.session.commit()
            return episode
        
        @staticmethod
        def delete(episode_id):
            episode = Episode.query.get(episode_id)
            if episode:
                db.session.delete(episode)
                db.session.commit()
                return True
            return False