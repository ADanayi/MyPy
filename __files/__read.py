import traceback

def goodlines(file, func=None):
    try:
        if func is None:
            return [l.split('\n')[0] for l in file.readlines()]
        else:
            return [func(l.split('\n')[0]) for l in file.readlines()]
    except:
        traceback.print_exc()
        return None

def read_goodlines(file_path, func=None):
    try:
        with open(file_path, 'r') as file:
            ret = goodlines(file, func)
        return ret
    except:
        traceback.print_exc()
        return None
