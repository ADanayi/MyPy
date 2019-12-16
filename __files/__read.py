def goodlines(file):
    return [l.split('\n')[0] for l in file.readlines()]

def read_goodlines(file_path):
    try:
        with open(file_path, 'r') as file:
            ret = goodlines(file)
        return ret
    except:
        return None