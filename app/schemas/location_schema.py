from marshmallow import Schema, fields, post_dump

class LocationSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    type = fields.Str()
    dimension = fields.Str()
    residents_count = fields.Method("get_residents_count")
    
    def get_residents_count(self, obj):
        """Calculates the number of residents"""
        return obj.residents_count()