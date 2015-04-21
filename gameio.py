from datetime import datetime
from itertools import count
from settings import settings
from classes import InfoBackground
import json
import os

def csv_result(essay):
    """Given the essay evaluation matrix return the string to be written to
    output file"""
    def to_line(val):
        return ','.join(map(str, val))+'\n'
    return map(to_line, essay)

def get_out_name(sess_name):
    """Compute the name for the output file given the input file name"""
    base = '.'.join(sess_name.split('.')[:-1])
    return '%s_output_%s.csv'%(base, datetime.now())


class PianoSession:
    session      = {}
    player       = ''
    all_sessions = {}

    sess_file_name = 'sessions.json'

    def __init__(self):
        if not os.path.isfile(self.sess_file_name):
            with open(self.sess_file_name, 'w') as sess_file:
                json.dump({
                    'players': {}
                }, sess_file, indent=4)

    def __enter__(self):
        self.read_session()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.write_session()

    def read_session(self):
        with open(self.sess_file_name, 'r') as sess_file:
            all_sessions = json.load(sess_file)
        players      = all_sessions['players'].keys()

        print ('Bienvenido al juego, elige un jugador de la lista o crea uno nuevo')
        print ('escribiendo un nuevo nombre')
        print ('')
        print ('Jugadores disponibles:')
        print (', '.join(players) if players else '<Ninguno>')
        print ()

        player = input ('Entrar jugador: ')

        self.player = player

        if player in players:
            self.session = all_sessions['players'][player]
        else:
            self.session = {
                'group': self.read_group(),
                'level': 0,
            }

        self.all_sessions = all_sessions

    def read_group(self):
        group_keys = list(settings.GROUPS.keys())
        num_groups = len(group_keys)
        group      = ''
        i          = 0

        while not group:
            if i%5==0:
                print ('Elegir grupo para el nuevo usuario')
                print ('Grupos disponibles: ')
                print ('')
                print ('\n'.join(
                    map(
                        lambda index, name: '%d: %s'%(index, name),
                        count(),
                        group_keys,
                    )
                ))
                print ('')
            try:
                num_group = int(input('Número del grupo elegido: '))

                if num_group < 0 or num_group >= num_groups:
                    raise ValueError()

                group = group_keys[num_group]
            except ValueError:
                print ('Número inválido')

            i += 1

        return group

    def write_session(self):
        self.all_sessions['players'][self.player] = self.session

        with open(self.sess_file_name, 'w') as sess_file:
            json.dump(self.all_sessions, sess_file, indent=4)

    def get_infoscreens(self):
        groups = settings.GROUPS
        levels = settings.LEVELS

        images = levels[groups[self.session['group']][self.session['level']]]['screens']

        return list(map(lambda x:InfoBackground(x), images))

    def __str__(self):
        return '<Sesión de %s>'%self.player

if __name__ == '__main__':
    with PianoSession() as ps:
        print ()
        print ('Dentro de la sesión')
        print ()
