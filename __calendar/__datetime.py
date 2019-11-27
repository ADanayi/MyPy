import datetime

def today():
    return datetime.datetime.now()

def tomorrow():
    n = datetime.datetime.now()
    d = n.date()
    t = n.time()
    d2 = datetime.date.fromordinal(d.toordinal() + 1)
    return datetime.datetime(d2.year, d2.month, d2.day, t.hour, t.minute, t.second, t.microsecond)

def has_passed(t0, t):
    tic = t0
    toc = t
    if toc.toordinal() > tic.toordinal():
        return True
    return toc.timestamp() > tic.timestamp()