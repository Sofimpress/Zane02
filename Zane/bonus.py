import pygame
from settings import *
from random import randint

class Bonus(pygame.sprite.Sprite):
    def __init__(self, center, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images\\" + filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speed = BONUS_SPEED
        self.type = ''

    def update(self):
        pass

    def draw(self,screen):
        screen.blit(self.image, self.rect)

    def set_type(self, sort):
        self.type = sort

    def get_type(self):
        return self.type
