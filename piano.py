import pygame
from pygame.locals import *
from classes import Background, Block, RedLine, scales, get_icon, infoscreens
from data import tile_positions, sound_keys, sounds, sound_map
from gameio import csv_result, get_out_name, PianoSession
from settings import settings
from itertools import islice
import os
import sys

# Bitmask values for evaluation
EVAL_CLICK = settings.get('EVAL_CLICK')
EVAL_NOTE  = settings.get('EVAL_NOTE')
EVAL_SCALE = settings.get('EVAL_SCALE')
EVAL_TIME  = settings.get('EVAL_TIME')

def nex_blocks(session):
    """Get next four blocks from session and map them to a list of Block objects
    """
    def gen_blocks(note_tuple):
        # index, note
        return Block(tile_positions[note_tuple[1][0], note_tuple[0]], note_tuple[1][0], note_tuple[1][1])
    return list(map(gen_blocks, enumerate(islice(session, 4))))

def eval_key(block, note, scale):
    """Compute the evaluation of a click"""
    res = EVAL_CLICK | EVAL_TIME
    if note == block.note:
        res |= EVAL_NOTE
    if scale == block.scale:
        res |= EVAL_SCALE
    return res

def gen_essay(blocks):
    """Given a list of block objects return the evaluation matrix for this essay
    """
    return [
        [block.note, block.scale, 0]
        for block in blocks
    ]

def main(session, out_file, test):
    """Main entry point of this game, keeps the game loop"""
    # Initialize screen
    pygame.init()
    # the game screen, pass FULLSCREEN to fullscreen
    screen = pygame.display.set_mode((800, 600), FULLSCREEN)
    # Game icon
    pygame.display.set_icon(get_icon())
    # Game title
    pygame.display.set_caption('Piano')

    # Fill background
    background = Background()

    # Blocks
    blocks = nex_blocks(session)

    # The red line
    redline = RedLine(380, 460, 2)

    # First scale (corresponding to first block)
    scale = scales[blocks[0].scale]

    # Blit everything to the screen
    clock = pygame.time.Clock()

    move     = False # controls redline motion speed
    position = 0 # stores current column
    essay    = gen_essay(blocks) # Essay evaluation matrix
    current_info = 0

    while True:
        # tick to 60 fps
        clock.tick(60)
        # Handle events
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == 27:
                # ESC key, exit game
                return
            elif event.type == KEYDOWN:
                # Valid key, validate input and update essay evaluation matrix
                current_info += 1
                if current_info == 8:
                    break
            elif event.type == QUIT:
                # Handles window close button
                return
        else:
            screen.blit(infoscreens[current_info].image, infoscreens[current_info].rect)

            pygame.display.flip()
            continue
        break

    # Event loop
    while True:
        # tick to 60 fps
        clock.tick(60)
        # Handle events
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == 27:
                # ESC key, exit game
                return
            elif event.type == KEYDOWN and event.unicode in sound_keys:
                # Valid key, validate input and update essay evaluation matrix
                if not (essay[position][2] & EVAL_CLICK):
                    essay[position][2] = eval_key(blocks[position], *sound_map[event.unicode])
                    # Every required condition was stisfied, play sound
                    if (essay[position][2] & test) == test:
                        sounds[sound_map[event.unicode]].play()
            elif event.type == QUIT:
                # Handles window close button
                return

        # Paint background
        screen.fill((255, 255, 255))
        screen.blit(background.image, background.rect)

        # Paint blocks
        if test & EVAL_NOTE:
            for block in blocks:
                screen.blit(block.image, block.rect)

        # Move the redline
        if move:
            position = redline.move()
            if position == 4:
                # Finished essay
                out_file.writelines(csv_result(essay))
                blocks = nex_blocks(session)
                essay  = gen_essay(blocks)
                if not blocks:
                    break
            elif position > -1:
                # get next scale
                scale = scales[blocks[position].scale]

        # Paint the redline
        if test & EVAL_TIME:
            screen.blit(redline.image, redline.rect)
        # Paint the scale
        if test & EVAL_SCALE:
            screen.blit(scale.image, scale.rect)

        # Send everything to screen
        pygame.display.flip()

        # Alternate readline motion
        move = not move


if __name__ == '__main__':
    session = PianoSession()
    # names of files for read and write
    sess_dir  = settings.get('SESSION_DIR')
    out_dir   = settings.get('OUTPUT_DIR')
    read_file = settings.get('READ_FILE')

    sess_name = os.path.join(sess_dir, read_file)

    output_adapter = settings.get('OUTPUT_ADAPTER')
    if (output_adapter == 'file'):
        output_handler  = open(os.path.join(out_dir, get_out_name(read_file)), 'w')
    else:
        output_handler  = sys.stdout

    # this is a context manager, once completed files are closed
    with open(sess_name, 'r') as session_file:
        # a generator that splits content of each line in session_file
        sess_gen = (line.strip().split(',') for line in session_file)

        # call the main funciton with the session, output file and test values
        main(sess_gen, output_handler, settings.get('EVALUATION_CRITERIA'))

    if output_handler is not sys.stdout:
        output_handler.close()
