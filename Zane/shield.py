import pygame
from settings import *
from random import randint

class Shield(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(SHIELD_FILENAME).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = SHIELD_INACTIVE_POS
        self.is_active = False
        self.shield_timer = pygame.time.get_ticks()
        
    def update(self, center):
        now =  pygame.time.get_ticks()
        if now - self.shield_timer > SHIELD_RUNTIME:
            self.is_active = False
            self.shield_timer = now
        if self.is_active:
            self.rect.center = center
        else:
            self.rect.center = SHIELD_INACTIVE_POS

    def draw(self,screen):
        screen.blit(self.image, self.rect)

    def set_active(self):
        self.is_active = True

    def get_center(self):
        return self.rect.center    
