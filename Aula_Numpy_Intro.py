import numpy as np
import sys
sys.path.append('../')

#https://numpy.org/doc/1.16/reference/generated/numpy.loadtxt.html


km = np.loadtxt('../Python_Data_Science_LINGUAGEM_E_NUMPY/Python_Data_Science/Numpy/data/carros-km.txt')
anos = np.loadtxt('../Python_Data_Science_LINGUAGEM_E_NUMPY/Python_Data_Science/Numpy/data/carros-anos.txt', dtype = int)
km_media = km / (2019- anos)

print(type(km_media))