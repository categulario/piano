import pygame
from pygame.locals import *
from classes import Background, Block, RedLine
from data import tile_positions, sound_keys
import json

def gen_blocks(note_tuple):
    return Block(tile_positions[note_tuple[0], note_tuple[1]["note"]])

def main(session):
    trial = 0
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((800, 600)) # FULLSCREEN
    pygame.display.set_caption('Piano')

    # Fill background
    background = Background([0,0])
    screen.fill((255, 255, 255))
    screen.blit(background.image, background.rect)

    # Blocks
    blocks = list(map(gen_blocks, enumerate(session[trial]['notes'])))

    for block in blocks:
        screen.blit(block.image, block.rect)

    # The red line
    redline = RedLine(380, 460, 1)
    screen.blit(redline.image, redline.rect)

    # Blit everything to the screen
    pygame.display.flip()

    move = False

    # Event loop
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == 27:
                return
            elif event.type == KEYDOWN and event.unicode in sound_keys:
                pass
            elif event.type == QUIT:
                return

        screen.fill((255, 255, 255))
        screen.blit(background.image, background.rect)

        for block in blocks:
            screen.blit(block.image, block.rect)

        if move:
            redline.move()
        screen.blit(redline.image, redline.rect)

        pygame.display.flip()

        move = not move


if __name__ == '__main__':
    with open('media/sessions/session_1.json', 'r') as session_file:
        session = json.load(session_file)
        main(session)
