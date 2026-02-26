from src.models import Location
from src import db

class LocationRepository:
    @staticmethod
    def get_all():
        return Location.query.order_by(Location.id).all()
    
    @staticmethod
    def get_by_id(location_id):
        return Location.query.get(location_id)
    
    @staticmethod
    def get_by_type(location_type):
        return Location.query.filter_by(type=location_type).all()
    
    @staticmethod
    def get_by_dimension(dimension):
        return Location.query.filter_by(dimension=dimension).all()
    
    @staticmethod
    def search_by_name(name):
        return Location.query.filter(Location.name.ilike(f'%{name}%')).all()
    
    @staticmethod
    def create(data):
        location = Location(**data)
        db.session.add(location)
        db.session.commit()
        return location
    
    @staticmethod
    def update(location_id, data):
        location = Location.query.get(location_id)
        if location:
            for key, value in data.items():
                setattr(location, key, value)
            db.session.commit()
        return location
    
    @staticmethod
    def delete(location_id):
        location = Location.query.get(location_id)
        if location:
            db.session.delete(location)
            db.session.commit()
            return True
        return False