from src.models import Character
from src import db

class CharacterRepository:
    
        @staticmethod
        def get_all():
            return Character.query.order_by(Character.id).all()

        @staticmethod
        def get_by_id(character_id):
            return Character.query.get(character_id)
        
        @staticmethod
        def get_by_status(status):
            return Character.query.filter_by(status=status).all()

        @staticmethod
        def search_by_name(name):
            return Character.query.filter(Character.name.ilike(f'%{name}%')).all()

        @staticmethod
        def get_by_species(species):
            return Character.query.filter_by(species=species).all()

        @staticmethod
        def get_by_origin_location(location_id):
            return Character.query.filter_by(origin_id=location_id).all()

        @staticmethod
        def get_by_current_location(location_id):
            return Character.query.filter_by(location_id=location_id).all()

        @staticmethod 
        def create(data):
            character = Character(**data)
            db.session.add(character)
            db.session.commit()
            return character
        
        @staticmethod
        def update(character_id, data):
            character = Character.query.get(character_id)
            if character:
                for key, value in data.items():
                    setattr(character, key, value)
                db.session.commit()
            return character
        
        @staticmethod
        def delete(character_id):
            character = Character.query.get(character_id)
            if character:
                db.session.delete(character)
                db.session.commit()
                return True
            return False