from unit.starwars_unit import StarWarsUnit
import unit, helper, effects
from tiles import Tile
import pygame
import random

class Stormtrooper(StarWarsUnit):
    """
    A classic stormtrooper from the Star Wars universe.
    This unit carries around a blaster rifle that shoots a partile beam.
    Effective against other star wars units not aligned with the Galactic
    Emipre (just the wookiees for now).
    
    Complete with crappy accuracy! Their 'accuracy' goes down a little
    bit every day that goes by, up until the 20th day when it caps
    (or is it 'hits rock bottom'?) and roughly 1-out-of-6 shots will hit.
    Now, when we say 'will hit', what is actually meant is that damage is
    reduced to just 0.1. Also, bonus damage is ignored if it's a miss.
    
    Armour: Low
    Speed: Low
    Range: Medium
    Damage: Medium (High against wookiees)
    
    Other notes:
    - Slightly slowed by forests and mountains.
    - Can move through any land terrain.
    - Can't hit air units.
    - Can hardly hit any units for that matter... (Stormtrooper Fire)
    """
    sprite = pygame.image.load("assets/stormtrooper.png")
    
    def __init__(self, **keywords):
        #load the image for the base class.
        self._base_image = Stormtrooper.sprite

        #load the base class
        super().__init__(**keywords)
        
        #sounds
        self.move_sound = "FeetMove"
        self.hit_sound = "Stormtrooper"
        self.die_sound = "Wilhelm_Scream" # The classic hollywood scream

        #set unit specific things.
        self.alliance = "Galactic_Empire"
        self.type = "Stormtrooper"
        self.phony_damage = True
        self.speed = 4
        self.max_atk_range = 3
        self.damage = 5
        self.bonus_damage = 4
        self.defense = 1
        self.hit_effect = effects.Laser # A newly added laser effect!
        self._move_costs = {'mountain': 1.5,
                             'forest': 1.5}
        self._accuracy = 100

    def begin_round(self, tile):
        """
        Calculate the accuracy for stormtroopers at
        the beginning of every round.
        """
        super().begin_round(tile)
        self.get_accuracy()
                          
    def can_hit(self, target_unit):
        """
        Determines whether a unit can hit another unit.
        
        Overrides because stormtroopers can't hit planes.
        """
        # If it's an air unit return false
        if isinstance(target_unit, unit.air_unit.AirUnit):
            return False

        # Not an air unit, return true
        return True
    
    def get_accuracy(self):
        """
        Our stormtrooper units have accuracy modifiers, determining how often they'll hit.

        The acuracy is calculated with random numbers and the number of days that have gone
        by. Generally, the longer the time has passed, the worse chance they have at
        landing a hit.

        The line '2 * random.randint(1, 50 - day_modifier)' was created so that at best,
        you have a possibility of getting 100, and as time goes by this eventually
        drops to 60.
        """
        if self.day > 20:
            day_modifier = 20
        else:
            day_modifier = self.day
                
        self._accuracy = 2 * random.randint(1, 50 - day_modifier)

    def get_false_damage(self, target, target_tile):
        """
        Returns the potential attack damage against a given enemy.
        This was created separately so that in the gui.py file,
        I could just tell it to grab this instead of 'get_damage()'
        and it won't give away when a stormtrooper would 'miss'.
    
        This overrides the super class function for special damage
        against non Galactic Empire units.
        """
        
        # Only proceed if it's a Star_Wars unit type, because non-SW
        # units don't have 'self.alliance' pre-defined
        if isinstance(target, unit.starwars_unit.StarWarsUnit) and target.alliance != "Galactic_Empire":
            # Calculate the total damage
            damage = self.damage + self.bonus_damage
        
            # Calculate the unit's defense
            defense = target.get_defense(tile = target_tile)
            
            # Don't do negative damage
            if (damage - defense < 0):
                return 0

            return damage - defense

        else:
            return super().get_damage(target, target_tile)
     
    def get_damage(self, target, target_tile):
        """
        Returns the potential attack damage against a given enemy.
        If the accuracy isn't high enough, a damage of just
        0.1 is returned.
        """
        if self._accuracy < 50:
            return 0.1 # returning just zero caused issues

        return self.get_false_damage(target, target_tile)        

unit.unit_types["Stormtrooper"] = Stormtrooper
