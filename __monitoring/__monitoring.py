from MyPy.__timer import Sampler
import psutil

class CPU_monitor(Sampler):
    
    def __init__(self, sampling_time, saving_time, saving_folder_path, default_file_name='data', default_file_ext='pdf'):
        Sampler.__init__(self, sampling_time, saving_time, saving_folder_path, default_file_name, default_file_ext)

    def sample(self):
        psutil.cpu_percent()

class RAM_monitor(Sampler):

    def __init__(self, sampling_time, saving_time, saving_folder_path, default_file_name='data', default_file_ext='pdf'):
        Sampler.__init__(self, sampling_time, saving_time, saving_folder_path, default_file_name, default_file_ext)

    def sample(self):
        return psutil.virtual_memory()._asdict()['used']
