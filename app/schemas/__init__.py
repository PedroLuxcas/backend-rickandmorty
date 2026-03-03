"""
Schemas package for Marshmallow serialization.
Export schema instances for easy importing.
"""

from .characters_schema import CharacterSchema
from .episode_schema import EpisodeSchema
from .location_schema import LocationSchema

# Create reusable instances
character_schema = CharacterSchema()
characters_schema = CharacterSchema(many=True)

episode_schema = EpisodeSchema()
episodes_schema = EpisodeSchema(many=True)

location_schema = LocationSchema()
locations_schema = LocationSchema(many=True)

__all__ = [
    'character_schema', 'characters_schema',
    'episode_schema', 'episodes_schema',
    'location_schema', 'locations_schema'
]