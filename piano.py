import pygame
from pygame.locals import *
from classes import Background

def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption('Piano')

    # Fill background
    # background = pygame.Surface(screen.get_size())
    # background = background.convert()
    # background.fill((250, 250, 250))
    background = Background('media/img/background.png', [0,0])
    screen.blit(background.image, background.rect)

    # Blit everything to the screen
    pygame.display.flip()

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.blit(background.image, background.rect)
        pygame.display.flip()


if __name__ == '__main__':
    main()
