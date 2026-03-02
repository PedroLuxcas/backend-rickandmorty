from .. import db

class Location(db.Model):
    __tablename__ = 'locations'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    type = db.Column(db.String(100))
    dimension = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
    characters_origin = db.relationship('Character', 
                                       foreign_keys='Character.origin_id',
                                       back_populates='origin_location',
                                       lazy='dynamic')
    
    characters_current = db.relationship('Character',
                                        foreign_keys='Character.location_id',
                                        back_populates='current_location',
                                        lazy='dynamic')
    
    def residents_count(self):
        """Returns total number of residents (original + current, without duplicates)"""
        origin_ids = {c.id for c in self.characters_origin.all()}
        current_ids = {c.id for c in self.characters_current.all()}
        return len(origin_ids | current_ids)  # Union of sets
    
    def __repr__(self):
        return f'<Location {self.id}: {self.name}>'