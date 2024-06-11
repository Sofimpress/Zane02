import pygame
from settings import *
from meteor import Meteor
from random import randint

class MeteorManager:
    def __init__(self):
        filename_list = ["lit_zmea1.jpg", "lit_zmea2.jpg"]
##        filename_list2 = ["big_zmea2.jpg", "lit_zmea2.jpg"]"big_zmea1.jpg""big_zmea2.jpg"
        
        self.meteors = []
        for filename in filename_list:
            meteor = Meteor("images\\meteors\\" + filename)
            meteor.random_position()
##            if "big" in filename:
##                meteor.set_damage(50)
##                meteor.set_score(5)
##                meteor.set_anim_size("big")
            if "lit" in filename:
                meteor.set_damage(30)
                meteor.set_score(1)
                meteor.set_anim_size("lit")
##            elif "2" in filename:
##                SPEED = -SPEED 

            self.meteors.append(meteor)

    def update(self):
        for meteor in self.meteors:
            meteor.update()
            if meteor.rect.right <= 0 or meteor.rect.left >= SC_WIDTH \
            or meteor.rect.top >= SC_HEIGHT:
                meteor.random_position()
            

    def draw(self, screen):
        for meteor in self.meteors:
            meteor.draw(screen)
