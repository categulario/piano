__all__ = ['settings']

import os

class SettingsLoader:
    def __init__(self):
        ENVIRONMENT     = os.environ.get('PIANO_ENVIRONMENT', 'play')
        SETTINGS_MODULE = os.environ.get('PIANO_SETTINGS_MODULE', 'conf')

        settings = __import__(SETTINGS_MODULE + '.settings').__getattribute__('settings').__dict__

        if os.path.isfile(SETTINGS_MODULE+'/settings_'+ENVIRONMENT+'.py'):
            overrided = __import__(SETTINGS_MODULE + '.settings_'+ENVIRONMENT).__getattribute__('settings_'+ENVIRONMENT).__dict__
        else:
            overrided = {}

        self.settings = dict()

        for key in settings.keys():
            self.settings[key] = overrided.get(key, settings[key])

    def __getitem__(self, key):
        return self.settings.get(key, None)

    def __getattr__(self, key):
        return self.settings.get(key, None)

    def get(self, key, default=None):
        return self.settings.get(key, default)

settings = SettingsLoader()
