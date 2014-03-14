from unit.base_unit import BaseUnit
import unit, helper
from tiles import Tile
import pygame

class StarWarsUnit(BaseUnit):
    """
    Similar to ground_unit class, except no vehicles.
    
    The basic ground-moving unit.
    
    - Only collides with other ground and infantry units
    - Gains even more bonuses (and debuffs) from tiles.
    """
    def __init__(self, **keywords):
        #load the base class
        super().__init__(**keywords)

        #set unit specific things.
        self.type = "StarWars Unit"
        self.day = 0
        self.new_turn = True
        
    def turn_ended(self):
        """
        Called when the turn is ended. Runs the aircraft out of fuel, or refuels
        if there's a carrier nearby.
        """
        super().turn_ended()
        
        self.day += 1
        self.new_turn = True
            
        return True
    
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
           #or u and u.team != self.team and isinstance(u, StarWarsUnit)):
            return False
        
        #for right now, our units are only ground themed, so water is impassable
        if (tile.type == 'water'):
            return False

        return True

