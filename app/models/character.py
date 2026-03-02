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
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
    # Relationships
    origin_location = db.relationship('Location', 
                                     foreign_keys=[origin_id],
                                     back_populates='characters_origin')
    
    current_location = db.relationship('Location',
                                       foreign_keys=[location_id],
                                       back_populates='characters_current')
    
    episodes = db.relationship('Episode', 
                               secondary='character_episodes',
                               back_populates='characters',
                               order_by='Episode.id')
    
    def __repr__(self):
        return f'<Character {self.id}: {self.name}>'