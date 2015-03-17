import pygame
from pygame.locals import *
from classes import Background, Block, RedLine, scales
from data import tile_positions, sound_keys, sounds, sound_map
from itertools import islice

EVAL_CLICK = 1
EVAL_NOTE  = 2
EVAL_SCALE = 4
EVAL_TIME  = 8

def nex_blocks(session):
    def gen_blocks(note_tuple):
        # index, note
        return Block(tile_positions[note_tuple[1][0], note_tuple[0]], note_tuple[1][0], note_tuple[1][1])
    return list(map(gen_blocks, enumerate(islice(session, 4))))

def eval_key(block, note, scale):
    res = EVAL_CLICK
    if note == block.note:
        res |= EVAL_NOTE
    if scale == block.scale:
        res |= EVAL_SCALE
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

    # Blocks
    blocks = nex_blocks(session)

    # The red line
    redline = RedLine(380, 460, 2)

    scale = scales[blocks[0].scale]

    # Blit everything to the screen
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
                if not (essay[position] & EVAL_CLICK):
                    essay[position] = eval_key(blocks[position], *sound_map[event.unicode])
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
            collected_data = main(gen, out_file, EVAL_SCALE)
