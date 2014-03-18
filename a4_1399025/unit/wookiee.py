#wookiee class
from unit.starwars_unit import StarWarsUnit
import unit, helper, effects
import pygame

class Wookiee(StarWarsUnit):
    """
    A classic wookiee from the Star Wars universe.
    This unit is equipped with a crossbow, and generally does little
    damage. However, the longer they spend in the forests, they recieve 
    more range and damge. Effective against other star wars units aligned
    with the Galactic Emipre (just the stormtroopers for now).
    
    Armour: Low
    Speed: Low
    Range: Medium
    Damage: Low (High against stormtroopers, increases in forests)
    
    Other notes:
    - Slightly slowed by mountains and sand.
    - Can move through any land terrain.
    - Can't hit air units.
    """
    sprite = pygame.image.load("assets/wookiees.png")
    
    def __init__(self, **keywords):
        #load the image for the base class.
        self._base_image = Wookiee.sprite

        #load the base class
        super().__init__(**keywords)
        
        #sounds
        self.move_sound = "FeetMove"
        self.hit_sound = "Wookiee" 
        self.die_sound = "Wookiee"

        #set unit specific things.
        self.alliance = "Rebel_Alliance"
        self.type = "Wookiee"
        self.speed = 4
        self.max_atk_range = 3
        self.damage = 3
        self.bonus_damage = 4
        self.defense = 1
        self.hit_effect = effects.Ricochet
        self._move_costs = {'mountain': 1.5,
                             'sand': 1.5}
                             
    def can_hit(self, target_unit):
        """
        Determines whether a unit can hit another unit.
        
        Overrides because wookiees can't hit planes.
        """
        # If it's an air unit return false
        if isinstance(target_unit, unit.air_unit.AirUnit):
            return False
            
        # Not an air unit, return true
        return True

    def begin_round(self, tile):
        """
        Gives Wookiees a boost of attack range and damage when it begins
        a round in the forest. Once it leaves, the values go back to
        stock values. Takes tile type from gui.py as a parameter.
        
        Damage is capped at 8, and range is capped at 5.
        """
        if tile == 'forest':
            if self.damage < 8:
                self.damage += 1
            if self.max_atk_range < 5:
                self.max_atk_range += 1
        elif tile != 'forest':
            self.damage = 4
            self.max_atk_range = 3
            
        super().begin_round(tile)
    
    def get_damage(self, target, target_tile):
        """
        Returns the potential attack damage against a given enemy.
        
        This overrides the super class function for special damage
        against Galactic Empire units.
        """
        
        # Only proceed if it's a Star_Wars unit type, because non-SW
        # units don't have 'self.alliance' pre-defined
        if isinstance(target, unit.starwars_unit.StarWarsUnit) and target.alliance == "Galactic_Empire":
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

unit.unit_types["Wookiee"] = Wookiee
