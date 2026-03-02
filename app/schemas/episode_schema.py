from marshmallow import Schema, fields

class EpisodeSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    air_date = fields.Str()
    episode = fields.Str()