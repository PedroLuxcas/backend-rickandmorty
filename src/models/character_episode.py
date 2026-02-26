from .. import db

class CharacterEpisode(db.Model):
    __tablename__ = 'character_episodes'
    
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'), primary_key=True)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
    # Relacionamentos
    character = db.relationship('Character', backref=db.backref('episode_links', cascade='all, delete-orphan'))
    episode = db.relationship('Episode', backref=db.backref('character_links', cascade='all, delete-orphan'))
    
    def to_dict(self):
        return {
            'character_id': self.character_id,
            'episode_id': self.episode_id,
            'character_name': self.character.name if self.character else None,
            'episode_name': self.episode.name if self.episode else None,
            'episode_code': self.episode.episode if self.episode else None
        }