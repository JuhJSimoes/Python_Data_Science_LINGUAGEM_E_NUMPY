import numpy as np
import sys

anos = np.loadtxt(fname = "../Python_Data_Science_LINGUAGEM_E_NUMPY/Python_Data_Science/Numpy/data/carros-anos.txt", dtype = int)
km = np.loadtxt(fname = "../Python_Data_Science_LINGUAGEM_E_NUMPY/Python_Data_Science/Numpy/data/carros-km.txt")
valor = np.loadtxt(fname = "../Python_Data_Science_LINGUAGEM_E_NUMPY/Python_Data_Science/Numpy/data/carros-valor.txt")

dataset = np.column_stack((anos, km, valor))
print(dataset.shape, '\n')

print(np.mean(dataset, axis=1), '\n')

print(np.mean(dataset[:,2]), '\n')

print(np.std(dataset[:,2]), '\n')

print(np.std(dataset[:,2]), '\n')

print(dataset.sum(axis=0), '\n')

print((dataset[:,1].sum()), '\n')

print(np.sum(dataset, axis=0), '\n')

print(np.sum(dataset[:,2]), '\n')

