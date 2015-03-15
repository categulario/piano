import pygame
import pygame.mixer
import time

pygame.mixer.init()

notes  = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

tile_positions = {
    (column, note):(460+(column)*80, 500-(80*note_index))
    for note_index, note in enumerate(notes)
    for column in range(4)
}

sound_keys = '3456789ertyuiodfghjklcvbnm,.'

sound_map = {
    '3' : ('C', 4),
    '4' : ('D', 4),
    '5' : ('E', 4),
    '6' : ('F', 4),
    '7' : ('G', 4),
    '8' : ('A', 4),
    '9' : ('B', 4),
    'e' : ('C', 3),
    'r' : ('D', 3),
    't' : ('E', 3),
    'y' : ('F', 3),
    'u' : ('G', 3),
    'i' : ('A', 3),
    'o' : ('B', 3),
    'd' : ('C', 2),
    'f' : ('D', 2),
    'g' : ('E', 2),
    'h' : ('F', 2),
    'j' : ('G', 2),
    'k' : ('A', 2),
    'l' : ('B', 2),
    'c' : ('C', 1),
    'v' : ('D', 1),
    'b' : ('E', 1),
    'n' : ('F', 1),
    'm' : ('G', 1),
    ',' : ('A', 1),
    '.' : ('B', 1),
}

sounds = {
    (note, scale): pygame.mixer.Sound('media/sound/%s_%d.wav'%(note, scale))
    for note in notes
    for scale in range(1, 5)
}

if __name__ == '__main__':
    sounds['A', 2].play()
    time.sleep(3)
