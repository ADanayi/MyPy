import os
import threading
import time

class Handler:
    def __init__(self, cbf, interval_s):
        self.__cbf = cbf
        self.__interval_s = interval_s
        self.__tic = time.time()
    
    def toc(self, toc=None):
        if toc is None:
            toc = time.time()

        if self.__interval_s <= toc - self.__tic:
            self.__tic = toc
            cbf = self.__cbf
            th = threading.Thread(target=cbf, daemon=True)
            th.start()

class Timer:
    def __init__(self, resolution_s = 1):
        self.__H = []
        self.__state = 'init'
        self.__resolution = resolution_s
        self.__L = threading.Lock()

    @property
    def state(self):
        return self.__state

    def add_handler(self, cbf, interval_s):
        self.__L.acquire()
        self.__H.append(Handler(cbf, interval_s))
        self.__L.release()

    def start(self):
        self.__th = threading.Thread(target=self.__action, daemon=True)
        self.__th.start()
        self.__state = 'started'
        
    def __action(self):
        while True:
            #print('.')
            time.sleep(self.__resolution)
            toc = time.time()
            self.__toc(toc)

    def __toc(self, toc):
        self.__L.acquire()
        for h in self.__H:
            try:
                h.toc(toc)
            except:
                self.__H.remove(h)
                #print('Timer Class: Error in one of handlers. Handler removed from list.')
        self.__L.release()