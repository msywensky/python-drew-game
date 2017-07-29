import pygame as pg
from os import path
import math

class Rock(object):
    def __init__(self,screen,x,y,angle,velocity):
        self.image = self.get_rock_image()
        self.screen = screen
        self.angle = angle
        self.velocity = velocity
        self.time = 0.0
        self.angle = angle / 180.0 * math.pi
        self.yVelocity = math.sin(self.angle) * velocity
        self.xVelocity = math.cos(self.angle) * velocity
        self.x = x+30
        self.y = y+10
        self.gravity = 9.0

    def get_rock_image(self):
        """for now just return a rock.  
        """
        return pg.image.load(path.join('images','stone.png'))
        
    def hit_balloon(self, balloons):
        for b in balloons:            
            if b.is_hit(self.x,self.y): 
                return b
        return None

    def update(self):
        self.time += .05
        self.x += (self.xVelocity * self.time)
        self.y += ((-1.0 * (self.yVelocity * self.time)) + (.5 * self.gravity * (self.time ** 2)))
    def draw(self):
        """memes
        """
        self.screen.blit(self.image, (self.x, self.y))
