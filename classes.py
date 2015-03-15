import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('media/img/background.png')
        self.rect  = self.image.get_rect()
        self.rect.left, self.rect.top = location

class RedLine(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('media/img/line.png')
        self.rect  = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Block(pygame.sprite.Sprite):
    def __init__(self, location):
        self.velocity = 1
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('media/img/black.png')
        self.rect  = self.image.get_rect()
        self.rect.left, self.rect.top =  location
