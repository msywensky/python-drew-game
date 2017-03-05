import pygame as pg
from os import path

class Person(object):
    """The slingshot boy class.
    """

    def __init__(self, screen, (x, y), angle):
        """ Constructor is called when the class has been instantiated
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.angle = angle
        # four images are used for walking
        self.moving_images = [pg.image.load(path.join('images','walk1.png')),
            pg.image.load(path.join('images','walk2.png')),
            pg.image.load(path.join('images','walk3.png')),
            pg.image.load(path.join('images','walk4.png'))]
        self.image = self.moving_images[0]
        self.image_number = 0

        # One image for aiming the slingshot
        self.aim_image = pg.image.load(path.join('images','stayattack1.png'))

    def move_left(self, step):
        """Move the person left, along the x axis, don't let him off the screen
        """
        self.x -= step
        if self.x < 0:
            self.x = 0

        self.image_number -= 1
        if self.image_number < 0:
            self.image_number = 3
        self.image = self.moving_images[self.image_number]
    
    def move_right(self, step):
        """Move the person right, along the x axis
        Invisible barrier to make it more difficult
        """
        self.x += step
        if self.x > 500:
            self.x = 500
            
        self.image_number += 1
        if self.image_number > 3:
            self.image_number = 0
        self.image = self.moving_images[self.image_number]
    
    # TODO: create the draw method, same as balloon
    def draw(self):
        pass
    # TODO: create an increase_angle method
    # this method should be called when the user arrows up
    # 

    # TODO: create a decrease_angle method, when arrow down

    def aim(self):
        """Assign the aim image
        """
        self.image = self.aim_image
        self.image_number = 0
        self.fire_image_number = 0

    def fire(self):
        """assign the fire image, increasing the fire image counter
        return true when the last image has been loaded
        """

        #for now assign the first first image and return true
        self.image = self.fire_images[0] # self.fire_image_number]
        return True

