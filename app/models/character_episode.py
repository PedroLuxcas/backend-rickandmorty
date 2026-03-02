from .. import db

class CharacterEpisode(db.Model):
    __tablename__ = 'character_episodes'
    
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'), primary_key=True)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
    character = db.relationship(
        'Character', 
        backref=db.backref('episode_associations', cascade='all, delete-orphan'),
        overlaps="characters,episodes"  
    )
    
    episode = db.relationship(
        'Episode', 
        backref=db.backref('character_associations', cascade='all, delete-orphan'),
        overlaps="characters,episodes" 
    )
    
    def __repr__(self):
        return f'<CharacterEpisode {self.character_id}-{self.episode_id}>'