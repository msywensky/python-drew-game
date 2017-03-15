import pygame as pg
from os import path
import math, random

class Balloon(object):
    """Class that represents a Balloon
    """

    def __init__(self, screen, xLow, xHigh, yLow, yHigh):
        """Create a new balloon within the provided width (x) and height (y) ranges
        """
    
        self.screen = screen

        # Each balloon has a randomized velocity.  
        # It is turned negative to to match the python coordinates
        self.velocity = (-1) * (random.randrange(30,60,1) / 1000.0)
        self.x = random.randint(xLow,xHigh)
        self.y = random.randint(yLow, yHigh)

        self.get_balloon_image = self.image 

        self.size = self.image.get_rect().size


    def get_balloon_image(self):
        """for now just return a red balloon.  
        """
        return pg.image.load(path.join('images','balloon-red.png'))


    def update(self):
        """move the balloon.  The balloon goes up by adding velocity to self.y
        """
        pass
        # TODO: remove pass and add velocity to self.y

    def draw(self):
        """Add the balloon to the screen
        """
        self.screen.blit(self.image, (self.x, self.y))

    def is_offscreen(self):
        pass 
    # TODO: A balloon is off the screen when it's y coordinate is <= 0
    # return True if the balloon is off screen
     
