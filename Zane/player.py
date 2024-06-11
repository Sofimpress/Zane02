import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        
        self.pers_name = ['Zane', 'Kai', 'Jay', 'Cole']
        self.index = 0
        self.imageHolder= {}
        self.imageHolder['ZaneL'] = pygame.image.load(PLAYER_FILE_NAME11).convert_alpha()
        self.imageHolder['ZaneR'] = pygame.image.load(PLAYER_FILE_NAME12).convert_alpha()
        self.imageHolder['KaiL'] = pygame.image.load(PLAYER_FILE_NAME21).convert_alpha()
        self.imageHolder['KaiR'] = pygame.image.load(PLAYER_FILE_NAME22).convert_alpha()
        self.imageHolder['JayL'] = pygame.image.load(PLAYER_FILE_NAME31).convert_alpha()
        self.imageHolder['JayR'] = pygame.image.load(PLAYER_FILE_NAME32).convert_alpha()
        self.imageHolder['ColeL'] = pygame.image.load(PLAYER_FILE_NAME41).convert_alpha()
        self.imageHolder['ColeR'] = pygame.image.load(PLAYER_FILE_NAME42).convert_alpha()
        self.image =  self.imageHolder['ZaneL']
        self.rect = self.image.get_rect()
        self.laser_sprites = []
        self.rect.centerx = SC_WIDTH//2
        self.rect.bottom = SC_HEIGHT - 100
        self.hp = PLAYER_MAX_HP
        self.speed = 0
        self.storona = 0
        self.fire_timer = pygame.time.get_ticks()
        self.laser = Laser(self.rect.centerx - 40, self.rect.bottom + 100)
        
        self.laser_name = ['Zan', 'Ka', 'Ja', 'Col']
        self.laser.index = 0
        self.laser.imageHolder= {}
        self.laser.imageHolder['ZanL'] = pygame.image.load(LASER_FILE_NAME11).convert_alpha()
        self.laser.imageHolder['ZanR'] = pygame.image.load(LASER_FILE_NAME12).convert_alpha()
        self.laser.imageHolder['KaL'] = pygame.image.load(LASER_FILE_NAME21).convert_alpha()
        self.laser.imageHolder['KaR'] = pygame.image.load(LASER_FILE_NAME22).convert_alpha()
        self.laser.imageHolder['JaL'] = pygame.image.load(LASER_FILE_NAME31).convert_alpha()
        self.laser.imageHolder['JaR'] = pygame.image.load(LASER_FILE_NAME32).convert_alpha()
        self.laser.imageHolder['ColL'] = pygame.image.load(LASER_FILE_NAME41).convert_alpha()
        self.laser.imageHolder['ColR'] = pygame.image.load(LASER_FILE_NAME42).convert_alpha()
        self.laser.image =  self.laser.imageHolder['ZanL']


    def update(self):
        
        self.speedy = 0
        self.speedx = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1] :
            self.index = 0
            self.laser.index = 0
            self.image = self.imageHolder[self.pers_name[self.index] + 'L']
            self.laser.image = self.laser.imageHolder[self.laser_name[self.laser.index] + 'L']
        if keys[pygame.K_2] :
            self.index = 1
            self.laser.index = 1
            self.image = self.imageHolder[self.pers_name[self.index] + 'L']
            self.laser.image = self.laser.imageHolder[self.laser_name[self.laser.index] + 'L']
        if keys[pygame.K_3] :
            self.index = 2
            self.laser.index = 2
            self.image = self.imageHolder[self.pers_name[self.index] + 'L']
            self.laser.image = self.laser.imageHolder[self.laser_name[self.laser.index] + 'L']
        if keys[pygame.K_4] :
            self.index = 3
            self.laser.index = 3
            self.image = self.imageHolder[self.pers_name[self.index] + 'L']
            self.laser.image = self.laser.imageHolder[self.laser_name[self.laser.index] + 'L']
        if keys[pygame.K_a]:
            self.image = self.imageHolder[self.pers_name[self.index] + 'L']
        if keys[pygame.K_d]:
            self.image = self.imageHolder[self.pers_name[self.index] + 'R']
        if keys[pygame.K_a]:
            self.speedx = -8
        if keys[pygame.K_d]:
            self.speedx = 8
        self.rect.x += self.speedx


        if self.rect.right > SC_WIDTH:
            self.rect.right = SC_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        self.fire()


        for laser in self.laser_sprites:
            laser.update()
            if laser.rect.bottom < 0:
                self.laser_sprites.remove(laser)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        for laser in self.laser_sprites:
            screen.blit(laser.image, laser.rect)

    def fire(self):
        now = pygame.time.get_ticks()
        keys = pygame.key.get_pressed()            
        if keys[pygame.K_SPACE] and now - self.fire_timer > FIRE_DELAY:
            self.fire_timer = now

            laser = Laser(self.rect.centerx, self.rect.top)
            self.laser_sprites.append(laser)

    def get_hp(self):
        return self.hp
    
    def njo(self):
        return self.index

    def reduce_hp(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def add_hp(self, hp):
        self.hp += hp
        if self.hp > 100:
            self.hp = 100
            
    def dis(self):
        if self.laser_sprites.rect.right <= 0 or laser_sprites.rect.left >= SC_WIDTH:
            self.laser_sprites.remove(laser) 
            
    def get_centerx(self):
        return self.rect.centerx

    def get_center(self):
        return self.rect.center

    def get_top(self):
        return self.rect.top

class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.pers_name = ['Zan', 'Ka', 'Ja', 'Col']
        self.index = 0
        self.imageHolder= {}
        self.imageHolder['ZanL'] = pygame.image.load(LASER_FILE_NAME11).convert_alpha()
        self.imageHolder['ZanR'] = pygame.image.load(LASER_FILE_NAME12).convert_alpha()
        self.imageHolder['KaL'] = pygame.image.load(LASER_FILE_NAME21).convert_alpha()
        self.imageHolder['KaR'] = pygame.image.load(LASER_FILE_NAME22).convert_alpha()
        self.imageHolder['JaL'] = pygame.image.load(LASER_FILE_NAME31).convert_alpha()
        self.imageHolder['JaR'] = pygame.image.load(LASER_FILE_NAME32).convert_alpha()
        self.imageHolder['ColL'] = pygame.image.load(LASER_FILE_NAME41).convert_alpha()
        self.imageHolder['ColR'] = pygame.image.load(LASER_FILE_NAME42).convert_alpha()
        self.image =  self.imageHolder['ZanL']
        self.rect = self.image.get_rect() 
        self.rect.centerx = x - 40
        self.rect.bottom = y + 110
        self.speedx = LASER_SPEEDY
        self.storona = 3
        
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.storona = 0
        if keys[pygame.K_d]:
            self.storona = 1
            
        if self.storona == 0:
            self.rect.x -= self.speedx
        if self.storona == 1:
            self.rect.x += self.speedx
            
        if keys[pygame.K_1] :
            self.index = 0
            self.image = self.imageHolder[self.pers_name[self.index] + 'L']
        if keys[pygame.K_2] :
            self.index = 1
            self.image = self.imageHolder[self.pers_name[self.index] + 'L']
        if keys[pygame.K_3] :
            self.index = 2
            self.image = self.imageHolder[self.pers_name[self.index] + 'L']
        if keys[pygame.K_4] :
            self.index = 3
            self.image = self.imageHolder[self.pers_name[self.index] + 'L']
        if keys[pygame.K_a]:
            self.image = self.imageHolder[self.pers_name[self.index] + 'L']
        if keys[pygame.K_d]:
            self.image = self.imageHolder[self.pers_name[self.index] + 'R']
        self.image =  self.imageHolder[self.pers_name[self.index] + 'L']

            
            
    def draw(self, screen):
        screen.blit(self.image, self.rect)





