from marshmallow import Schema, fields

class EpisodeSchema(Schema):
    """Schema for serializing Episode objects"""
    
    id = fields.Int(metadata={"description": "Episode ID"})
    name = fields.Str(metadata={"description": "Episode name"})
    air_date = fields.Str(metadata={"description": "Original air date"})
    episode = fields.Str(metadata={"description": "Episode code (e.g., S01E01)"})