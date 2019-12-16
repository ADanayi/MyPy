import os

def assure_path(*args):
    path = ''
    for arg in args:
        path = os.path.join(path, arg)
    if not os.path.exists(path):
        os.makedirs(path)
    return path
