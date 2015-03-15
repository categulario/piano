import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.transform.scale(pygame.image.load('media/img/background.png'), (800, 600))
        self.rect  = self.image.get_rect()
        self.rect.left, self.rect.top = location

class RedLine(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load('media/img/background.png')
        self.rect  = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Block(pygame.sprite.Sprite):
    def __init__(self):
        self.velocity = 1
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load('media/img/black.png')
        self.rect  = self.image.get_rect()
        self.x = 800
        self.y = 0
        self.rect.left = self.x
        self.rect.top =  self.y
    def move(self):
        self.rect.left =  self.x
        self.rect.top =  self.y
