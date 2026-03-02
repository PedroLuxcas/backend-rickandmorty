from .. import db

class Episode(db.Model):
    __tablename__ = 'episodes'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    air_date = db.Column(db.String(100))
    episode = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
    characters = db.relationship('Character', 
                                 secondary='character_episodes',
                                 back_populates='episodes')
    
    def __repr__(self):
        return f'<Episode {self.id}: {self.episode}>'