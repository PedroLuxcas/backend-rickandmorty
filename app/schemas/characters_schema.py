from marshmallow import Schema, fields
from .location_schema import LocationSchema
from .episode_schema import EpisodeSchema

class CharacterSchema(Schema):
    """Schema for serializing Character objects"""
    
    id = fields.Int()
    name = fields.Str()
    status = fields.Str()
    species = fields.Str()
    type = fields.Str()
    gender = fields.Str()
    image = fields.Str()
    
    origin = fields.Nested(LocationSchema, attribute='origin_location')
    current_location = fields.Nested(LocationSchema, attribute='current_location')
    
    last_episode = fields.Method("get_last_episode")
    
    def get_last_episode(self, obj):
        if obj.episodes:
            last = max(obj.episodes, key=lambda e: e.id)
            return EpisodeSchema().dump(last)
        return None
    
# ⭐ THESE ARE THE INSTANCES YOU NEED TO IMPORT
character_schema = CharacterSchema()
characters_schema = CharacterSchema(many=True)