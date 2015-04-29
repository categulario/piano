import pygame
import pygame.mixer
import time

pygame.mixer.init()

# Available notes
notes  = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

# Compute positions in the screen given the note and the column of the block
tile_positions = {
    (note, column):(460+(column)*80, 500-(80*note_index))
    for note_index, note in enumerate(notes)
    for column in range(4)
}

# Valid keys for this game
sound_keys = [
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    'e',
    'r',
    't',
    'y',
    'u',
    'i',
    'o',
    'd',
    'f',
    'g',
    'h',
    'j',
    'k',
    'l',
    'c',
    'v',
    'b',
    'n',
    'm',
    ',',
    '.',
]

# Map keys to their corresponding note and scale
key_map = {
    '3' : ('C', 1),
    '4' : ('D', 1),
    '5' : ('E', 1),
    '6' : ('F', 1),
    '7' : ('G', 1),
    '8' : ('A', 1),
    '9' : ('B', 1),
    'e' : ('C', 2),
    'r' : ('D', 2),
    't' : ('E', 2),
    'y' : ('F', 2),
    'u' : ('G', 2),
    'i' : ('A', 2),
    'o' : ('B', 2),
    'd' : ('C', 3),
    'f' : ('D', 3),
    'g' : ('E', 3),
    'h' : ('F', 3),
    'j' : ('G', 3),
    'k' : ('A', 3),
    'l' : ('B', 3),
    'c' : ('C', 4),
    'v' : ('D', 4),
    'b' : ('E', 4),
    'n' : ('F', 4),
    'm' : ('G', 4),
    ',' : ('A', 4),
    '.' : ('B', 4),
}

# Map (note, scale) to its respective sound
sounds = {
    (note, scale): pygame.mixer.Sound('media/sound/%s_%d.wav'%(note, scale))
    for note in notes
    for scale in range(1, 5)
}

# test soud play
if __name__ == '__main__':
    sounds['A', 2].play()
    time.sleep(3)
