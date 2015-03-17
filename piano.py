import pygame
from pygame.locals import *
from classes import Background, Block, RedLine, scales
from data import tile_positions, sound_keys, sounds, sound_map
from itertools import islice
import json

def nex_blocks(session):
    def gen_blocks(note_tuple):
        # index, note
        return Block(tile_positions[note_tuple[1][0], note_tuple[0]], note_tuple[1][0], note_tuple[1][1])
    return list(map(gen_blocks, enumerate(islice(session, 4))))

def eval_key(key, block):
    res = 1
    note  = sound_map[key][0]
    scale = sound_map[key][1]
    if note == block.note:
        res += 2
    if scale == block.scale:
        res += 4
    return res

def csv_result(essay):
    def to_line(val):
        return str(val)+'\n'
    return map(to_line, essay)

def main(session, out_file, test):
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
    screen.blit(block.image, block.rect)

    # The red line
    redline = RedLine(380, 460, 2)
    screen.blit(redline.image, redline.rect)

    scale = scales[blocks[0].scale]

    # Blit everything to the screen
    pygame.display.flip()
    clock = pygame.time.Clock()

    move     = False # controls redline motion speed
    position = 0 # stores redline column (zero-indexed)
    essay    = [0]*4 # keeps record of the essay

    # Event loop
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == 27:
                return
            elif event.type == KEYDOWN and event.unicode in sound_keys:
                if not (essay[position] & 1):
                    essay[position] = eval_key(event.unicode, blocks[position])
                    if (essay[position] & test) == test:
                        sounds[sound_map[event.unicode]].play()
            elif event.type == QUIT:
                return

        screen.fill((255, 255, 255))
        screen.blit(background.image, background.rect)


        for block in blocks:
            screen.blit(block.image, block.rect)

        if move:
            position = redline.move()
            if position == 4:
                out_file.writelines(csv_result(essay))
                essay = [0]*4
                blocks = nex_blocks(session)
                if not blocks:
                    break
            elif position > -1:
                scale = scales[blocks[position].scale]

        screen.blit(redline.image, redline.rect)
        screen.blit(scale.image, scale.rect)

        pygame.display.flip()

        move = not move


if __name__ == '__main__':
    with open('media/sessions/session_1.csv', 'r') as session_file:
        with open('media/sessions/output_1.csv', 'w') as out_file:
            gen = (line.strip().split(',') for line in session_file)
            collected_data = main(gen, out_file, 6)
