import pygame
from pygame.locals import *
from classes import Background, Block, RedLine, scales, get_icon
from data import tile_positions, sound_keys, sounds, key_map
from gameio import csv_result, get_out_name, PianoSession
from settings import settings
from itertools import islice
import os
import sys

# Bitmask values for evaluation
EVAL_NOTE  = 2
EVAL_SCALE = 4
EVAL_TIME  = 8

def nex_blocks(session):
    """Get next four blocks from session and map them to a list of Block objects
    """
    def gen_blocks(note_tuple):
        # index, note
        return Block(tile_positions[note_tuple[1][0], note_tuple[0]], note_tuple[1][0], note_tuple[1][1])
    return list(map(gen_blocks, enumerate(islice(session, 4))))

def eval_key(block, evaluated, note, scale):
    """Compute the evaluation of a click"""
    res = 0
    if note == block.note:
        res |= EVAL_NOTE
    if scale == block.scale:
        res |= EVAL_SCALE
    if not evaluated:
        res |= EVAL_TIME
    return res

def gen_essay(blocks):
    """Given a list of block objects return the evaluation matrix for this essay
    """
    return [
        (block.note, block.scale)
        for block in blocks
    ]

def display_info(session, screen, clock):
    # Info screen variables
    infoscreens  = session.get_infoscreens()
    num_infos    = len(infoscreens)
    current_info = 0

    # Info screen
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
                if current_info == num_infos:
                    break
            elif event.type == QUIT:
                # Handles window close button
                return
        else:
            screen.blit(infoscreens[current_info].image, infoscreens[current_info].rect)

            pygame.display.flip()
            continue
        break

def main(session):
    """Main entry point of this game, keeps the game loop"""
    # Initialize screen
    pygame.init()
    # the game screen, pass FULLSCREEN to fullscreen
    screen = pygame.display.set_mode((800, 600))
    # Game icon
    pygame.display.set_icon(get_icon())
    # Game title
    pygame.display.set_caption('Piano')

    # Fill background
    background = Background()

    # Blit everything to the screen
    clock = pygame.time.Clock()

    # Display info screens
    display_info(session, screen, clock)

    # Blocks
    blocks = nex_blocks(session)
    # The red line
    redline = RedLine(380, 460, 2)
    # First scale (corresponding to first block)
    scale = scales[blocks[0].scale]

    # Gane loop variables
    move         = True # controls redline motion speed
    column       = -1 # stores current column given by the clock
    progress     = float('-inf') # register progress of redline
    evaluated    = False # A flag that indicates if this column has been evaluated
    evaluation   = [] # Essay evaluation matrix
    essay        = gen_essay(blocks)
    criteria     = session.get_criteria()

    # Event loop
    while True:
        # tick to 60 fps
        clock.tick(60)
        # Handle events
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == 27:
                # ESC key, exit game
                return
            elif event.type == KEYDOWN and event.unicode in sound_keys and column>-1:
                clicked_note, clicked_scale = key_map[event.unicode]
                # print (eval_key(blocks[column], evaluated, clicked_note, clicked_scale))
            elif event.type == QUIT:
                # Handles window close button
                return

        # Move the redline
        if move:
            new_progress = redline.move()
            if progress != new_progress: # progress has changed
                # Essay finished, report to session
                if new_progress < progress:
                    session.results += csv_result(evaluation)
                    blocks     = nex_blocks(session)
                    essay      = gen_essay(blocks)
                    evaluation = []

                    if not blocks:
                        break
                progress = new_progress

            if criteria & EVAL_TIME:
                new_column = redline.get_column()

        # Change the column and the scale
        if new_column != column and new_column > -1:
            evaluated = False
            column = new_column
            scale = scales[blocks[column].scale]

        # Paint background
        screen.fill((255, 255, 255))
        screen.blit(background.image, background.rect)

        # Paint blocks
        if criteria & EVAL_NOTE:
            for block in blocks:
                screen.blit(block.image, block.rect)

        # Paint the redline
        if criteria & EVAL_TIME:
            screen.blit(redline.image, redline.rect)
        # Paint the scale
        if criteria & EVAL_SCALE:
            screen.blit(scale.image, scale.rect)

        # Send everything to screen
        pygame.display.flip()

        # Alternate readline motion
        move = not move


if __name__ == '__main__':
    with PianoSession() as piano_session:
        main(piano_session)
