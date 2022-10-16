import numpy as np
import sys
import time
#from numpy import arange

print(np.arange(10))
print('\n')

km = np.array([1000, 2300, 4987, 1500])
type(km)

km.dtype

km = np.loadtxt(fname = '../Python_Data_Science_LINGUAGEM_E_NUMPY/Python_Data_Science/Numpy/data/carros-km.txt', dtype = int)
print(km)
print('\n')

dados = [ 
    ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva'],
    ['Central multimídia', 'Teto panorâmico', 'Freios ABS', '4 X 4', 'Painel digital', 'Piloto automático', 'Bancos de couro', 'Câmera de estacionamento'],
    ['Piloto automático', 'Controle de estabilidade', 'Sensor crepuscular', 'Freios ABS', 'Câmbio automático', 'Bancos de couro', 'Central multimídia', 'Vidros elétricos']
]

Acessorios = np.array(dados)
print(Acessorios)

print(km.shape)
print(Acessorios.shape)
# O shape exibe a dimensao da matriz

print('\n')

np_array = np.arange(1000000)
py_list = list(range(1000000))
#%time for _ in range(100): np_array *= 2 Teste no Jupiter
#%time for _ in range(100): py_list = [x * 2 for x in py_list] Teste no Jupiter

print('\n')

km = np.array([44410., 5712., 37123., 0., 25757.])
anos = np.array([2003, 1991, 1990, 2019, 2006])

idade = 2022 - anos

print('\n')

km_media = km/idade
print(km_media)

dados = np.array([km, anos])
print(dados)

dados[0]
km_media = dados[0] / (2019 - dados[1])
print(km_media)

#Ex.: IMC = peso / altura²

peso = np.array([106.0, 68.3,75.0])
altura = np.array([1.9, 1.58, 1.75])
IMC = peso / altura ** 2
print(IMC)
print('\n')


#Fatiamento com passo
print(dados[1,2])
contador = np.arange(10)
print(contador[1:4])
print(contador[1:8:2])
print(contador[::2])
print(contador[1::2])
print(dados)

print(dados[:,1:4][0]/(2022 - dados[:, 1:4][1]))

print(contador[contador > 5])

print(dados[:, dados[1] > 2000])

dados = np.array(
    [
        ['Roberto', 'casado', 'masculino'],
        ['Sheila', 'solteira', 'feminino'],
        ['Bruno', 'solteiro', 'masculino'],
        ['Rita', 'casada', 'feminino']
    ]
)

print(dados[0::2, :2]) #0: - Seleciona todas as linhas
                #:2 - Seleciona a linhas de index 0 e 2
                #:2 - Seleciona as colunhas de index 0 ate 2 (porem a 2 não é exibida)
print('\n')

dados = np.array([[44410.,  5712., 37123.,     0., 25757.], [ 2003.,  1991.,  1990.,  2019.,  2006.]])
print(dados)
print(dados.ndim)
print(dados.size)
print(dados.T) #Transforma linhas em colunas igual transpose()
print(dados.tolist())
print('\n')

contador = np.arange(10)
print(contador)
print(contador.reshape(5,2))
print(contador.reshape((5,2), order='C'))
print(contador.reshape((5,2), order='F'))

print('\n')

km = [44410, 5712, 37123, 0, 25757]
anos = [2003, 1991, 1990, 2019, 2006]
info_carros = km + anos
print(info_carros , '\n')

print(np.array(info_carros).reshape((5,2), order = 'F'), '\n')

dados_new = dados.copy()
print(dados_new,'\n')

dados_new.resize((3,5), refcheck=False)
print(dados_new, '\n')

dados_new[2] = dados_new[0]/(2022-dados_new[1])
print(dados_new)



    
    