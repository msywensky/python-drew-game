import pygame as pg
from os import path
import math

# TODO: create a Rock class
# create a constructor 
# The constructor should have the following parameters
#   self
#   screen
#   angle
#   velocity
#   
# in the constuctor, do the following
#   save all the parameters to property values
#   load the stone.png file to the image property
#   set a time property to 0.0
#        self.angle = angle / 180.0 * math.pi
#        self.xVelocity = math.cos(self.angle) * velocity
#        self.yVelocity = math.sin(self.angle) * velocity
#  
# Create a hit_balloon method, with parameters of 
#   self
#   balloons list
# The method will check if the rock hits one of the balloons
# by traversing the list of balloons and calling the balloon.is_hit method
# for each balloon
# if a balloon was hit, return it, otherwise return None
# 
# Create an update method, this will move the rock
#   update the time property by adding .05 to it
#   use the following values to update the rock
#        self.x += (self.xVelocity * self.time)
#        self.y += ((-1.0 * (self.yVelocity * self.time)) + (.5 * self.gravity * (self.time ** 2))) 
#
# Create a draw method, using the same code from balloon