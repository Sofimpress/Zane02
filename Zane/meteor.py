import pygame
from settings import *
from random import randint

class Meteor(pygame.sprite.Sprite):
    def __init__(self, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.damage = 0
        self.score = 0
        self.anim_size = ""
        self.random_position()
##        self.d = 0
        

    def update(self):
        self.rect.x += self.speedx


    def draw(self,screen):
        screen.blit(self.image, self.rect)

    def set_damage(self, damage):
        self.damage = damage

    def get_damage(self):
        return self.damage

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score= score
        
    def random_position(self):
        d = randint(1, 2)
        if d == 1:
            self.rect.x = SC_WIDTH
            self.speedx = randint(-2,-1)
            self.image = pygame.image.load("images\\meteors\\lit_zmea1.jpg").convert_alpha()
        if d == 2:
            self.rect.x = 0
            self.speedx = randint(1,2)
            self.image = pygame.image.load("images\\meteors\\lit_zmea2.jpg").convert_alpha()
        self.rect.y = SC_HEIGHT - 200
        
        


    def get_center(self):
        return self.rect.center

    def set_anim_size(self, size):
        self.anim_size = size

    def get_anim_size(self):
        return self.anim_size


