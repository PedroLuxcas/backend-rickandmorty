from .. import db

class Location(db.Model):
    __tablename__ = 'locations'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    type = db.Column(db.String(100))
    dimension = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
    # Relationships
    characters_origin = db.relationship('Character', 
                                       foreign_keys='Character.origin_id',
                                       backref='origin_location',
                                       lazy='dynamic')
    characters_current = db.relationship('Character',
                                        foreign_keys='Character.location_id',
                                        backref='current_location',
                                        lazy='dynamic')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'dimension': self.dimension
        }
    
    def to_dict_complete(self):
        data = self.to_dict()
        data['residents_origin'] = [c.to_dict() for c in self.characters_origin.limit(10)]
        data['residents_current'] = [c.to_dict() for c in self.characters_current.limit(10)]
        return data