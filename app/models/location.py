from .. import db

class Location(db.Model):
    """Location model representing places in the Rick and Morty universe"""
    __tablename__ = 'locations'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    type = db.Column(db.String(100))
    dimension = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
    # Relationships
    characters_origin = db.relationship('Character', 
                                       foreign_keys='Character.origin_id',
                                       back_populates='origin_location',
                                       lazy='dynamic')
    
    characters_current = db.relationship('Character',
                                        foreign_keys='Character.location_id',
                                        back_populates='current_location',
                                        lazy='dynamic')
    
    @property
    def residents_count(self):
        """
        Returns the number of CURRENT residents in this location.
        (characters with location_id = this location)
        """
        return self.characters_current.count()
    
    @property
    def origin_count(self):
        """
        Returns the number of characters that have this location as their ORIGIN.
        """
        return self.characters_origin.count()
    
    def to_dict(self):
        """Basic location representation without relationships"""
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'dimension': self.dimension
        }