from src.repositories import LocationRepository

class LocationService:
    @staticmethod
    def get_all_locations():
        locations = LocationRepository.get_all()
        return [loc.to_dict() for loc in locations]
    
    @staticmethod
    def get_location_by_id(location_id):
        location = LocationRepository.get_by_id(location_id)
        return location.to_dict_complete() if location else None
    
    @staticmethod
    def get_locations_by_type(location_type):
        locations = LocationRepository.get_by_type(location_type)
        return [loc.to_dict() for loc in locations]
    
    @staticmethod
    def get_locations_by_dimension(dimension):
        locations = LocationRepository.get_by_dimension(dimension)
        return [loc.to_dict() for loc in locations]
    
    @staticmethod
    def search_locations(name):
        locations = LocationRepository.search_by_name(name)
        return [loc.to_dict() for loc in locations]
    
    @staticmethod
    def create_location(data):
        new_location = LocationRepository.create(data)
        return new_location.to_dict()
    
    @staticmethod
    def update_location(location_id, data):
        location = LocationRepository.update(location_id, data)
        return location.to_dict() if location else None
    
    @staticmethod
    def delete_location(location_id):
        return LocationRepository.delete(location_id)