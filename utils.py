import signal
import shutil
import os


def get_image_name(lastfmObject):
    name = lastfmObject.name.replace('/', '_')
    return name + '.jpg'


def handler(signum, frame):
    shutil.rmtree('./cache')
    exit(1)


def register_signal_handler():
    signal.signal(signal.SIGINT, handler)


def get_api_key():
    if os.path.exists('./config/config.txt'):
        with open('./config/config.txt', 'r') as f:
            API_KEY = f.readline()
        return API_KEY
