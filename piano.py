import pygame
from pygame.locals import *
from classes import Background, Block
from datetime import datetime

notes  = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
scales = [1, 2, 3, 4]

tile_positions = {(note, scale):(460+(scale-1)*80, 500-(80*note_index)) for note_index, note in enumerate(notes) for scale in scales}

def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((800, 600)) # FULLSCREEN
    pygame.display.set_caption('Piano')

    # Fill background
    background = Background([0,0])
    screen.fill((255, 255, 255))
    screen.blit(background.image, background.rect)

    sound = pygame.mixer.Sound('media/sound/5.wav')

    # Blocks

    block = Block(tile_positions['E', 1])
    screen.blit(block.image, block.rect)

    # Blit everything to the screen
    pygame.display.flip()

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == 27:
                return
            elif event.type == KEYDOWN and event.unicode == 'h':
                sound.play()
            elif event.type == QUIT:
                return

        screen.fill((255, 255, 255))
        screen.blit(background.image, background.rect)

        screen.blit(block.image, block.rect)

        pygame.display.flip()


if __name__ == '__main__':
    main()
