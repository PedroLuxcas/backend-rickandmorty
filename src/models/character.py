from .. import db

class Character(db.Model):
    __tablename__ = 'characters'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    status = db.Column(db.String(50))
    species = db.Column(db.String(100))
    type = db.Column(db.String(100))
    gender = db.Column(db.String(50))
    image = db.Column(db.Text)
    origin_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    origin = db.Column(db.JSON)
    location = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
    # Relationships
    episodes = db.relationship('Episode', secondary='character_episodes',
                              back_populates='characters')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status,
            'species': self.species,
            'type': self.type,
            'gender': self.gender,
            'image': self.image,
            'origin': self.origin,
            'location': self.location
        }
    
    def to_dict_complete(self):
        data = self.to_dict()
        data['episodes'] = [{'id': e.id, 'name': e.name, 'episode': e.episode} 
                           for e in self.episodes]
        return data