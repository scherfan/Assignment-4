from unit.base_unit import BaseUnit
import unit, helper
from tiles import Tile
import pygame

class StarWarsUnit(BaseUnit):
    """
    This is our new unit type, based off of Star Wars
    characters.

    This was based off of the 'ground unit' class,
    but modified a bit.
    
    For instance, we've introduced an 'alliance'
    that certain Star Wars units can use to their
    advantage. Even though there's only 2 sub-units
    at the moment, this allows for easy integration
    of more units in the future.
    """
    def __init__(self, **keywords):
        #load the base class
        super().__init__(**keywords)

        #set unit specific things.
        self.alliance = "Unaligned"
        self.type = "StarWarsUnit"
    
    def is_passable(self, tile, pos):
        """
        Returns whether or not this unit can move over a certain tile.
        """
        # Return default
        if not super().is_passable(tile, pos):
            return False
            
        # We can't pass through enemy units.
        u = BaseUnit.get_unit_at_pos(pos)
        if (u and u.team != self.team and isinstance(u, StarWarsUnit)):
            return False
        
        #for right now, our units are only ground themed, so water is impassable
        if (tile.type == 'water'):
            return False

        return True

