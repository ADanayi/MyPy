import os
from . import Timer
import MyPy.__files as files
from threading import Lock
import time
from matplotlib import pyplot as plt
from MyPy.__calendar import today

class Sampler:

    def __init__(self, sampling_time, saving_time, saving_folder_path, default_file_name='data', default_file_ext='pdf'):
        self.__sampling_time = sampling_time
        self.__saving_time = saving_time
        self.__saving_folder_path = saving_folder_path
        self.__timer = Timer(resolution_s = min(saving_time, sampling_time))
        self.__default_file_name = default_file_name
        self.__default_file_ext = default_file_ext

        self.__lock = Lock()
        self.__S = []
        self.__tic = time.time()
        self.__Ts = self.timestamp()

        self.__timer.add_handler(self.__sample, self.__sampling_time)
        self.__timer.add_handler(self.__save, self.__saving_time)
        self.__timer.start()

    @property
    def saving_folder_path(self):
        return self.__saving_folder_path

    @property
    def sampling_time(self):
        return self.__sampling_time

    @property
    def saving_time(self):
        return self.__saving_time

    def sample(self):
        return None

    def save(self, S, Tf, Ts):
        path = files.assure_path(self.__saving_folder_path)
        path = os.path.join(path, '{}_{}.{}'.format(self.__default_file_name, 
            str(today()).replace('.', '_'), self.__default_file_ext))
        plt.figure()
        plt.plot(S)
        plt.title('{}-{}@{}s'.format(int(Ts), int(Tf), self.__sampling_time))
        plt.savefig(path)

    def timestamp(self):
        return time.time() - self.__tic

    def __sample(self):
        sample = self.sample()
        self.__lock.acquire()
        self.__S.append(sample)
        self.__lock.release()

    def __save(self):
        self.__lock.acquire()
        Tf = self.timestamp()
        S = self.__S.copy()
        self.__S = []
        Ts = self.__Ts
        self.save(S, Tf, Ts)
        self.__Ts = Tf
        self.__lock.release()

import numpy as np

class ErgodicSampler(Sampler):

    def __init__(self, sampling_time, saving_time, saving_folder_path, default_file_name='data', default_file_ext='pdf'):
        Sampler.__init__(self, sampling_time, saving_time, saving_folder_path, default_file_name, default_file_ext)
        self.__L = []
        self.__last_u = 0

    def new_ensemble(self, value):
        self.__L.append(value)

    def sample(self):
        if len(self.__L) > 0:
            self.__last_u = np.mean(self.__L)
        self.__L.clear()
        return self.__last_u
