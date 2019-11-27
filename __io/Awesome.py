import xlsxwriter
import numpy as np

class Writer_SimpleTable:
    def __init__(self, opath, Keys):
        self.workbook = xlsxwriter.Workbook(opath)
        self.worksheets = {}

        self.Keys = Keys
        for key in self.Keys:
            self.worksheets[key] = self.workbook.add_worksheet(key)

        self.ptr_row = {}
        self.ptr_col = {}
        self.n_row = 0
        self.n_col = 0

    def flag_new_row(self, label):
        label = str(label)
        if label in self.ptr_row.keys():
            return
        self.n_row += 1
        self.ptr_row[label] = self.n_row
        self.__append_cell_at(self.n_row, 0, label)

    def flag_new_col(self, label):
        label = str(label)
        if label in self.ptr_col.keys():
            return
        self.n_col += 1
        self.ptr_col[label] = self.n_col
        self.__append_cell_at(0, self.n_col, label)

    def __append_cell_at(self, r, c, label):
        for key in self.worksheets.keys():
            self.worksheets[key].write(r, c, label)

    def append(self, row_label, col_label, feedDict):
        r = self.ptr_row[str(row_label)]
        c = self.ptr_col[str(col_label)]
        for key in self.worksheets.keys():
            self.worksheets[key].write(r, c, feedDict[key])
            
    def finish(self):
        self.workbook.close()

import pickle

def saveToFile(opath, dictionary):
    with open(opath, 'wb') as handle:
        pickle.dump(dictionary, handle, protocol=pickle.HIGHEST_PROTOCOL)

def loadFromFile(opath):
    with open(opath, 'rb') as handle:
        b = pickle.load(handle)
        return b
