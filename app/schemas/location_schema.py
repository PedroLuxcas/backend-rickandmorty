from marshmallow import Schema, fields

class LocationSchema(Schema):
    """Schema for serializing Location objects"""
    
    id = fields.Int(metadata={"description": "Location ID"})
    name = fields.Str(metadata={"description": "Location name"})
    type = fields.Str(metadata={"description": "Location type (Planet, Dimension, etc)"})
    dimension = fields.Str(metadata={"description": "Location dimension"})
    
    # Returns ONLY current residents count
    residents_count = fields.Method(
        "get_residents_count", 
        metadata={"description": "Number of current residents in this location"}
    )
    
    def get_residents_count(self, obj):
        """Returns only current residents count"""
        return obj.residents_count