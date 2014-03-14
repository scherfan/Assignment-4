from unit.starwars_unit import StarWarsUnit
import unit, helper, effects
from tiles import Tile
import pygame
import random

class Stormtrooper(StarWarsUnit):
    """
    An infantry unit armed with an anti-armour missile launcher. Very 
    effective against tanks and battleships, but otherwise not especially
    powerful.
    
    Armour: None
    Speed: Low
    Range: Medium
    Damage: Medium (High against armoured vehicles)
    
    Other notes:
    - Slightly slowed by forests and sand.
    - Slowed somewhat more by mountains.
    - Can move through any land terrain.
    - Can't hit air units.
    - Can't hit any units for that matter... (Stormtrooper Fire)
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

        #set unit specific things.
        self.type = "Stormtrooper"
        self.speed = 4
        self.max_atk_range = 3
        self.damage = 4
        self.bonus_damage = 4
        self.defense = 0
        self.hit_effect = effects.Explosion
        self._move_costs = {'mountain': 2,
                             'forest': 1.5,
                             'sand': 1.5}
        self._accuracy = 100
                             
    def can_hit(self, target_unit):
        """
        Determines whether a unit can hit another unit.
         
        Overrides because anti-armour can't hit planes.
        """
        # If it's an air unit return false
        if isinstance(target_unit, unit.air_unit.AirUnit):
            return False

        # Not an air unit, return true
        return True
    
    def get_accuracy(self):
        """
        Our stormtrooper units have accuracy modifiers, determining how often they'll hit
        """
        if self.new_turn == True:
            self.new_turn = False
            
            if self.day > 19:
                day_modifier = 19
            else:
                day_modifier = self.day
                
            self._accuracy = 2.5 * random.randint(1, 40 - day_modifier)
            if self._accuracy < 50:
                print(str(self._accuracy) + ' ' + str(self.day))
            else:
                print("Hit" + ' ' + str(self.day))
        return self._accuracy
        
    def get_damage(self, target, target_tile):
        """
        Returns the potential attack damage against a given enemy.
        
        This overrides the super class function for special damage
        and because anti-armour can't hit air units.
        """
        if self.get_accuracy() < 50:
            return 0.01
        # Do bonus damage to armored vehicles
        if target.type == "Tank" or target.type == "Battleship":
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

unit.unit_types["Stormtrooper"] = Stormtrooper
