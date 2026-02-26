from .. import db

class Episode(db.Model):
    __tablename__ = 'episodes'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    air_date = db.Column(db.String(100))
    episode = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
    # Relationships
    characters = db.relationship('Character', secondary='character_episodes',
                                back_populates='episodes')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'air_date': self.air_date,
            'episode': self.episode
        }
    
    def to_dict_complete(self):
        data = self.to_dict()
        data['characters'] = [{'id': c.id, 'name': c.name, 'status': c.status} 
                             for c in self.characters]
        return data