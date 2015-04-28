import pygame

def get_icon():
    return pygame.image.load('media/img/favicon.png')

class Background(pygame.sprite.Sprite):
    """Background image sprite"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('media/img/background.png')
        self.rect  = self.image.get_rect()
        self.rect.left, self.rect.top = (0, 0)

class InfoBackground(pygame.sprite.Sprite):
    """Background image sprite"""
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('media/img/%s.png'%name)
        self.rect  = self.image.get_rect()
        self.rect.left, self.rect.top = (0, 0)

class RedLine(pygame.sprite.Sprite):
    """The moving redline"""
    def __init__(self, start_x, loop_x, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('media/img/line.png')
        self.rect  = self.image.get_rect()
        self.rect.left, self.rect.top = (start_x, 20)
        self.speed = speed
        self.start_x = start_x
        self.loop_x = loop_x

    def move(self):
        """Moves the redline to the next position and return current column"""
        if self.rect.left < 780-self.speed:
            self.rect.left += self.speed
            return (self.rect.left-460)//80
        else:
            self.rect.left = self.loop_x
            return 4

class Block(pygame.sprite.Sprite):
    """Black blocks that indicate the note to be played"""
    def __init__(self, location, note, scale):
        self.velocity = 1
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('media/img/black.png')
        self.rect  = self.image.get_rect()
        self.rect.left, self.rect.top =  location
        self.note  = note
        self.scale = int(scale)

class Scale(pygame.sprite.Sprite):
    """The sprite for the 4 available scales"""
    def __init__(self, scale):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('media/img/scale_{0}.png'.format(scale))
        self.rect  = self.image.get_rect()
        self.rect.left, self.rect.top =  (20,20)

# Compute the only four scales used
scales = {
    i:Scale(i) for i in range(1, 5)
}
