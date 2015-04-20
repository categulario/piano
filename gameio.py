from datetime import datetime
from itertools import count
from conf.levels import GROUPS
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

    sessions_file_name  = 'sessions.json'
    sessions_file_read  = None
    sessions_file_write = None

    def __init__(self):
        self.sessions_file_write = open(self.sessions_file_name, 'w')
        self.sessions_file_read  = open(self.sessions_file_name, 'r')

        if not os.path.isfile(self.sessions_file_name):
            json.dump({
                'players': {}
            }, self.sessions_file_write, indent=4)
            self.sessions_file_write.flush()

    def __enter__(self):
        self.read_session()

    def __exit__(self, exc_type, exc_value, traceback):
        self.write_session()

    def read_session(self):
        all_sessions = json.load(self.sessions_file_read)
        players      = all_sessions['players'].keys()

        print ('Bienvenido al juego, elige un jugador de la lista o crea uno nuevo')
        print ('escribiendo un nuevo nombre')
        print ('')
        print ('Jugadores disponibles:')
        print (', '.join(players) if players else 'Ninguno')
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
        group_keys = list(GROUPS.keys())
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
        json.dump(self.all_sessions, self.sessions_file_write, indent=4)

if __name__ == '__main__':
    with PianoSession() as ps:
        print ()
        print ('Dentro de la sesión')
        print ()
