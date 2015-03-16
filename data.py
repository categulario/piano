import pygame
import pygame.mixer
import time

pygame.mixer.init()

notes  = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

tile_positions = {
    (note, column):(460+(column)*80, 500-(80*note_index))
    for note_index, note in enumerate(notes)
    for column in range(4)
}

sound_keys = '3456789ertyuiodfghjklcvbnm,.'

sound_map = {
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

sounds = {
    (note, scale): pygame.mixer.Sound('media/sound/%s_%d.wav'%(note, scale))
    for note in notes
    for scale in range(1, 5)
}

if __name__ == '__main__':
    sounds['A', 2].play()
    time.sleep(3)
