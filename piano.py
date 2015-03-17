import pygame
from pygame.locals import *
from classes import Background, Block, RedLine, Scale
from data import tile_positions, sound_keys, sounds, sound_map
from itertools import islice
import json

def gen_blocks(note_tuple):
    # index, note
    return Block(tile_positions[note_tuple[1][0], note_tuple[0]])

def main(session):
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((800, 600)) # FULLSCREEN
    pygame.display.set_caption('Piano')

    # Fill background
    background = Background([0,0])
    screen.fill((255, 255, 255))
    screen.blit(background.image, background.rect)

    # Blocks
    blocks = list(map(gen_blocks, enumerate(islice(session, 4))))
    scale = Scale(3)
    screen.blit(scale.image, scale.rect)
    for block in blocks:
        screen.blit(block.image, block.rect)

    # The red line
    redline = RedLine(380, 460, 2)
    screen.blit(redline.image, redline.rect)

    # Blit everything to the screen
    pygame.display.flip()
    clock = pygame.time.Clock()

    move = False

    # Event loop
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == 27:
                return
            elif event.type == KEYDOWN and event.unicode in sound_keys:
                pass
            elif event.type == QUIT:
                return

        screen.fill((255, 255, 255))
        screen.blit(background.image, background.rect)

        screen.blit(scale.image, scale.rect)

        for block in blocks:
            screen.blit(block.image, block.rect)

        if move:
            redline.move()
        screen.blit(redline.image, redline.rect)

        pygame.display.flip()

        move = not move


if __name__ == '__main__':
    with open('media/sessions/session_1.csv', 'r') as session_file:
        gen = (line.strip().split(',') for line in session_file)
        main(gen)
