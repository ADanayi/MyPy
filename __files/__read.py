def goodlines(file):
    return [l.split('\n')[0] for l in file.readlines()]
