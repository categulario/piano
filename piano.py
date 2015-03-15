import pygame
from pygame.locals import *
from classes import Background, Block, RedLine
import json

notes  = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

tile_positions = {
    (column, note):(460+(column)*80, 500-(80*note_index))
    for note_index, note in enumerate(notes)
    for column in range(4)
}

def gen_blocks(note_tuple):
    print (note_tuple)
    return Block(tile_positions[note_tuple])

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

    sound = pygame.mixer.Sound('media/sound/5.wav')

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
