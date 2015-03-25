import pygame
from pygame.locals import *
from classes import InfoBackground

def login():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    infobg = InfoBackground((0, 0))
    pygame.display.set_caption('Piano')

    while True:
        for event in pygame.event.get():
            if (event.type == KEYDOWN and event.key == 27) or (event.type == QUIT):
                # ESC key, exit game
                return

        screen.fill((255, 255, 255))
        screen.blit(infobg.image, infobg.rect)

        pygame.display.flip()

if __name__ == '__main__':
    login()
