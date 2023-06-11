from numpy import getfromtxt
from numpy import savetxt


def read_csv_file(file_name):
    read_data = getfromtxt(file_name, delimiter=',')
    return read_data


def save_csv_file(file_name, data_array):
    savetxt(file_name, data_array, delimiter=',')