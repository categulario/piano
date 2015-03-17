import pygame
from pygame.locals import *
from classes import Background, Block, RedLine, Scale
from data import tile_positions, sound_keys, sounds, sound_map
from itertools import islice
import json

def gen_blocks(note_tuple):
    # index, note
    return Block(tile_positions[note_tuple[1][0], note_tuple[0]])

def nex_blocks(session):
    return list(map(gen_blocks, enumerate(islice(session, 4))))

def next_scale(session):
    return int(list(islice(session, 1))[0][1])

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
    blocks = nex_blocks(session)
    
    for block in blocks:
        screen.blit(block.image, block.rect)

    # Scales
    scale = Scale(next_scale(session))
    screen.blit(scale.image, scale.rect)

    # The red line
    redline = RedLine(380, 460, 2)
    screen.blit(redline.image, redline.rect)

    # Blit everything to the screen
    pygame.display.flip()
    clock = pygame.time.Clock()

    move = False
    position = 0
    lastPos = 0
    chageScale = False

    # Event loop
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == 27:
                return
            elif event.type == KEYDOWN and event.unicode in sound_keys:
                sounds[sound_map[event.unicode]].play()
            elif event.type == QUIT:
                return

        screen.fill((255, 255, 255))
        screen.blit(background.image, background.rect)


        for block in blocks:
            screen.blit(block.image, block.rect)
        
        screen.blit(scale.image, scale.rect)

        if move:
            position = redline.move()
            if position == 4:
                blocks = nex_blocks(session)

            if chageScale:
                print(position)
                scale = Scale(next_scale(session))

            if position>lastPos:
                chageScale = True
                lastPos = position
            else :
                chageScale = False

        screen.blit(redline.image, redline.rect)

        pygame.display.flip()

        move = not move


if __name__ == '__main__':
    with open('media/sessions/session_1.csv', 'r') as session_file:
        gen = (line.strip().split(',') for line in session_file)
        main(gen)
