import pygame
from settings import *
from bonus import Bonus
from meteor import Meteor
from random import randint, choice

class BonusManager:
    def __init__(self):
        self.filename_list = ["pill_yellow.png",
                        "shield_gold.png"]
        self.bonuses = []
        
    def generate_bonus(self, meteor):
        chance = randint(1, 100)
        if chance <= BONUC_CHANCE:
            filename = choice(self.filename_list)
            bonus = Bonus(meteor.get_center(), filename)
            if filename.startswith("pill"):
                bonus.set_type("pill")
            elif filename.startswith("shield"):
                bonus.set_type("shield")
            self.bonuses.append(bonus)
            
    def update(self):
        for bonus in self.bonuses:
            bonus.update()
            if bonus.rect.top >= SC_HEIGHT:
                self.bonuses.remove(bonus)

    def draw(self, screen):
        for bonus in self.bonuses:
            bonus.draw(screen)
                
