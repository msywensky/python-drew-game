import pygame as pg
import sys
from os import path
from person import Person
from rock import Rock
from balloon import Balloon
from pygame.locals import Color, KEYUP, KEYDOWN, K_ESCAPE, K_s,\
    K_LEFT, K_RIGHT, K_UP, K_DOWN, K_SPACE, K_RETURN


class Game(object):
    """Primary class of the application.  
    """

    def __init__(self):
        """Constructor class.  This is executed when an instance of the class is created
        """
        self.frames_per_second = 60
        self.background = pg.image.load(path.join('images','background.png'))

        self.screen_width = 800 
        self.screen_height = 480
        self.screen_width = 800
        self.screen_height = 480
        self.game_over = False
        self.score = 0
        self.is_playing = False

    def generate_balloons(self):
        """create balloons for the level
        Given the level property, determine how many balloons to create
        Use a for loop to create balloons and add them to the balloons list
        """
        for i in range(1, self.level+1):
            self.balloons.append(Balloon(self.screen, 200, 750, 400, 450))
            
        
    def add_rock(self, velocity):
        rock = Rock (self.screen,self.person.x,self.person.y,self.person.angle,velocity)
        self.rocks.append(rock)


    def new_game(self):
        """Starts a new game.  
        Balloons and Rocks from the previous game are discarded.
        A new Person object is created.
        Score is reset.
        New balllons for level 1 are created
        """
        self.is_playing = True
        self.rocks = []
        self.balloons = [] 
        self.initial_angle = 30
        self.game_over = False
        self.score = 0
        self.level= 1

        self.person = Person(self.screen, (self.screen_width / 3, self.screen_height - 65), self.initial_angle)

        self.generate_balloons()   


    
    def run_game(self):
        """The method that contains the main loop
        """
        pg.init() 
        self.font = pg.font.SysFont(None, 30)
        clock = pg.time.Clock()        
        self.screen = pg.display.set_mode((self.screen_width, self.screen_height)) 
        pg.display.set_caption("Balloon Pop") 


        self.new_game()

        new_rock_velocity = 0
        release_slingshot = False

        # Start main loop. 
        while True: 
            clock.tick(self.frames_per_second)
            keys = pg.key.get_pressed()

            # Start event loop. 
            for e in pg.event.get():

                # Window was closed, clean up
                if e.type == pg.QUIT:
                    sys.exit()

                if e.type == KEYDOWN:

                    # Esc key was pressed, quit the app
                    if e.key == K_ESCAPE:
                        sys.exit()

                    # Enter key was pressed, start a new game if not in a game
                    if e.key == K_RETURN:
                        if self.game_over:
                            self.is_playing = True
                            self.new_game()

                    # Space bar pressed down, start the slingshot sequence
                    if e.key == K_SPACE and self.is_playing:
                        new_rock_velocity = 0
                        self.person.aim()

                if e.type == KEYUP:
                    # Space bar was released
                    # Complete the throwing sequence
                    if e.key == K_SPACE and self.is_playing:
                        release_slingshot = True

            # draw background first
            # this will overwrite everything that was previously on the screen
            # all other items and text will need to be redrawn after this
            self.screen.blit(self.background, (0,0))

            if self.is_playing:
                # Begin the slingshot release sequence
                if release_slingshot:

                    # There are multiple images to release the rock
                    release_slingshot_completed = self.person.fire()
                    if release_slingshot_completed:
                        release_slingshot = False
                        # Release the rock to begin it's journey
                        self.add_rock(new_rock_velocity)
                        new_rock_velocity = 0

                # holding keys down is outside of event loop
                if keys[K_LEFT]:          
                    self.person.move_left(4)

                if keys[K_RIGHT]:
                    self.person.move_right(4)

                if keys[K_UP]:
                    
                    self.person.increase_angle(2)

                if keys[K_DOWN]:
                    
                    self.person.decrease_angle(2)

                if keys[K_SPACE]:
                    # longer the space bar is held, the faster the rock will be thrown
                    new_rock_velocity += 1.5

                # Loop through the list of balloons
                for balloon in self.balloons:
                    if not self.game_over:
                        # Update the balloon's coordinates
                        balloon.update()

                        # Game ends when balloon reaches top of screen
                        if balloon.is_offscreen():
                            self.game_over = True
                            self.is_playing = False
                if self.is_playing:
                    # Loop through the list of thrown rocks on the screen
                    for rock in self.rocks:
                        
                        rock.update()
                        # Update the rock's location
                        

                        # remove rocks that fall off the bottom or sides
                        # rocks that go straight up (less than 0) are not removed
                        if rock.x > self.screen_width or rock.y > self.screen_height:
                            self.rocks.remove(rock)
                        else:
                            # Get the balloon that was hit (hopefully) or get None
                            temp_balloon = rock.hit_balloon(self.balloons)
                            if temp_balloon == None:
                                # Rock is still on the screen and did not hit a balloon
                                rock.draw()
                            else:
                                # Rock hit a balloon
                                # Remove the rock from the Rocks list
                                self.rocks.remove(rock)
                                self.balloons.remove(temp_balloon)
                       

                    if len(self.balloons) <= 0:
                        self.level += 1
                        self.generate_balloons()


                    # Add the balloons to the screen
                    for balloon in self.balloons:
                        balloon.draw()

                    # Add the person to the screen
                    self.person.draw()

            # Add all text to the screen
            self.screen
           
            # Redraw the screen to reflect all changes
            pg.display.flip() 

game = Game()            
game.run_game()
