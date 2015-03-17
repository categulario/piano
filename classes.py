import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('media/img/background.png')
        self.rect  = self.image.get_rect()
        self.rect.left, self.rect.top = location

class RedLine(pygame.sprite.Sprite):
    def __init__(self, start_x, loop_x, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('media/img/line.png')
        self.rect  = self.image.get_rect()
        self.rect.left, self.rect.top = (start_x, 20)
        self.speed = speed
        self.start_x = start_x
        self.loop_x = loop_x

    def move(self):
        if self.rect.left < 780-self.speed:
            self.rect.left += self.speed
            return (self.rect.left-460)//80
        else:
            self.rect.left = self.loop_x
            return 4

class Block(pygame.sprite.Sprite):
    def __init__(self, location, note, scale):
        self.velocity = 1
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('media/img/black.png')
        self.rect  = self.image.get_rect()
        self.rect.left, self.rect.top =  location
        self.note  = note
        self.scale = int(scale)

class Scale(pygame.sprite.Sprite):
    def __init__(self, slcale):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('media/img/scale_{0}.png'.format(slcale))
        self.rect  = self.image.get_rect()
        self.rect.left, self.rect.top =  (20,20)