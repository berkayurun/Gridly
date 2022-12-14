import signal
import shutil

def get_image_name(lastfmObject):
    name = lastfmObject.name.replace('/', '_')
    return name + '.jpg'

def handler(signum, frame):
    shutil.rmtree('./cache')
    print("losl")
    exit(1)

def register_signal_handler():
    signal.signal(signal.SIGINT, handler)