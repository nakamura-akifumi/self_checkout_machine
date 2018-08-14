import yaml
import os


def init():
    global app
    global msg

    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config', 'settings.yaml')
    with open(config_file) as stream:
        app = yaml.load(stream)

    message_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config', 'messages.yaml')
    with open(message_file) as stream:
        raw = yaml.load(stream)
        msg = raw['main']

