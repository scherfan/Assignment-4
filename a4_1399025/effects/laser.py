import animation

class Laser(animation.Animation):
    """
    An animated laser effect.
    """
    def __init__(self, pos):
        """
        Initialize the sprite effect.
        """
        animation.Animation.__init__(self,
                                     "assets/laser.png",
                                     20,
                                     20,
                                     0.15,
                                     animation.Mode.OneShot)
        self.rect.topleft = pos
