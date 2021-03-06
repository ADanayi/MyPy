from MyPy.__timer import Sampler
import psutil

class CPU_monitor(Sampler):
    
    def __init__(self, sampling_time, saving_time, saving_folder_path, default_file_name='data', default_file_ext='pdf'):
        Sampler.__init__(self, sampling_time, saving_time, saving_folder_path, default_file_name, default_file_ext)

    def sample(self):
        return psutil.cpu_percent()

class RAM_monitor(Sampler):

    def __init__(self, sampling_time, saving_time, saving_folder_path, default_file_name='data', default_file_ext='pdf'):
        Sampler.__init__(self, sampling_time, saving_time, saving_folder_path, default_file_name, default_file_ext)

    def sample(self):
        return psutil.virtual_memory()._asdict()['used']

class BW_monitor(Sampler):

    def __init__(self, sampling_time, saving_time, saving_folder_path, default_file_name='data', default_file_ext='pdf'):
        Sampler.__init__(self, sampling_time, saving_time, saving_folder_path, default_file_name, default_file_ext)
        self.__tx = psutil.net_io_counters().bytes_sent
        self.__rx = psutil.net_io_counters().bytes_recv

    def sample(self):
        tx = self.__tx
        rx = self.__rx
        val_bytes = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv - tx - rx
        self.__tx = psutil.net_io_counters().bytes_sent
        self.__rx = psutil.net_io_counters().bytes_recv
        return val_bytes / 1024
