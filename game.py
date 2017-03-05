import pygame as pg
import sys
from os import path
from person import Person
from movingitems import Rock, Balloon
from pygame.locals import Color, KEYUP, KEYDOWN, K_ESCAPE, K_s,\
    K_LEFT, K_RIGHT, K_UP, K_DOWN, K_SPACE, K_RETURN


class Game(object):
    """Primary class of the application.  
    """

    def __init__(self):
        """Constructor class.  This is executed when an instance of the class is created
        """

        # TODO: create screen_width and screen_height properties with values 800 and 480

        self.frames_per_second = 60
        self.show_instructions = True
        self.sound_on = True
        self.sound_supported = True
        self.score = 0

        # TODO: create game_over property, assign False

    def generate_balloons(self):
        """create balloons for the level
        Given the level property, determine how many balloons to create
        Use a for loop to create balloons and add them to the balloons list
        """
        pass

    
    

    def new_game(self):
        """Starts a new game.  
        Balloons and Rocks from the previous game are discarded.
        A new Person object is created.
        Score is reset.
        New balllons for level 1 are created
        """

        # TODO: create a rocks list property
        # TODO: create a balloons list property
        # TODO: create a person object
        # TODO: set the game_over property to False
        # TODO: set the score to 0
        # TODO: set the level property = 1
        # TODO: generate_balloons for the level      