import pygame
from pygame.locals import *
from classes import Background, Block
from datetime import datetime

def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Piano')

    # Fill background
    background = Background([0,0])
    screen.blit(background.image, background.rect)

    # Blit everything to the screen
    pygame.display.flip()

    sound = pygame.mixer.Sound('media/sound/13.wav')
    
    # Create seven blocks and their y-positions
    block = [0]*7
    position_y = [2, 88, 174, 260, 346, 432, 518]
    for i in range(7):
        block[i] = Block()
        block[i].y = position_y[i]
    velocity = 2
 
    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.unicode == 'h':
                sound.play()
            if event.type == QUIT:
                return

        move = datetime.now().microsecond%1 == 0
        screen.blit(background.image, background.rect)
        for i in range(7):
            screen.blit(block[i].image, block[i].rect)
            if  move and block[i].x>150: block[i].x-=velocity
            else : block[i].x = 800
            block[i].move()
        pygame.display.flip()


if __name__ == '__main__':
    main()
