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
    return list(map(to_line, essay))

def get_out_name(sess_name):
    """Compute the name for the output file given the input file name"""
    base = '.'.join(sess_name.split('.')[:-1])
    return '%s_output_%s.csv'%(base, datetime.now())


class PianoSession:
    session      = {}
    player       = ''
    all_sessions = {}
    results      = []

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
        self.write_results()
        self.write_session()

    def read_session(self):
        with open(self.sess_file_name, 'r') as sess_file:
            all_sessions = json.load(sess_file)
        players      = sorted(all_sessions['players'].keys())

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

        print ()
        print ('Jugando el jugador %s, que pertenece al grupo %s en el nivel %d'%(self.player, self.session['group'], self.session['level']))
        print ()

        self.all_sessions = all_sessions

    def read_group(self):
        group_keys = sorted(settings.GROUPS.keys())
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
        self.session['level'] += 1
        self.all_sessions['players'][self.player] = self.session

        with open(self.sess_file_name, 'w') as sess_file:
            json.dump(self.all_sessions, sess_file, indent=4)

    def write_results(self):
        out_dir  = os.path.join('media/data', self.player)
        out_file_name = os.path.join(out_dir, '%s_%s.csv'%(
            self.session['group'],
            self.get_level_name(),
        ))

        if not os.path.isdir(out_dir):
            os.mkdir(out_dir)

        with open(out_file_name, 'w') as out_file:
            out_file.writelines(self.results)
            print ('Datos guardados en %s'%out_file_name)

    def get_level_name(self):
        groups = settings.GROUPS

        current_group = self.session['group']
        current_level = self.session['level']

        if current_level < len(groups[current_group]):
            return groups[current_group][current_level]
        else:
            print ('No hay más niveles para este usuario en este grupo')
            exit(0)

    def get_level(self):
        groups = settings.GROUPS
        levels = settings.LEVELS

        current_level = self.session['level']
        current_group = self.session['group']

        if current_level < len(groups[current_group]):
            return levels[self.get_level_name()]
        else:
            print ('No hay más niveles para este usuario en este grupo')
            exit(0)

    def get_infoscreens(self):
        images = self.get_level()['screens']

        return list(map(lambda x:InfoBackground(x), images))

    def get_criteria(self):
        return self.get_level()['criteria']

    def __iter__(self):
        file_name = self.get_level()['file']

        return (
            line.strip().split(',')
            for line in open(os.path.join('media/sessions', file_name), 'r')
        )

    def __str__(self):
        return '<Sesión de %s>'%self.player

if __name__ == '__main__':
    with PianoSession() as ps:
        print ()
        print ('Dentro de la sesión')
        print ()
