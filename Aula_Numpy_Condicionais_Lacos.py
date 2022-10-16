Acessorios = ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva']
print(Acessorios)

for item in Acessorios:
    print(item)
    
print('\n')
    
list(range(10))

for i in range(10):
    print(i ** 2)

print('\n')
    
quadrado = []
for i in range(10):
    quadrado.append(i ** 2)
print(quadrado)

print('\n')

#List Comprehensions
print([i ** 2 for i in range(10)])

print('\n')

#Loops aninhados
dados = [ 
    ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva'],
    ['Central multimídia', 'Teto panorâmico', 'Freios ABS', '4 X 4', 'Painel digital', 'Piloto automático', 'Bancos de couro', 'Câmera de estacionamento'],
    ['Piloto automático', 'Controle de estabilidade', 'Sensor crepuscular', 'Freios ABS', 'Câmbio automático', 'Bancos de couro', 'Central multimídia', 'Vidros elétricos']
]
print(dados)
print('\n')

for lista in dados:
    print(lista)

print('\n')

for lista in dados:
    for item in lista:
      print(item) 

print('\n') 
      
Acessorios = []
for lista in dados:
    for item in lista:
      Acessorios.append(item)
print(Acessorios)

print('\n') 

list(set(Acessorios))

print('\n') 

[item for lista in dados for item in lista] #list comprehesion com itens duplicados
list(set([item for lista in dados for item in lista])) #list comprehesion removendo itens duplicados

print('\n') 

# 1º item da lista - Nome do veículo
# 2º item da lista - Ano de fabricação
# 3º item da lista - Veículo é zero km?

dados = [
    ['Jetta Variant', 2003, False],
    ['Passat', 1991, False],
    ['Crossfox', 1990, False],
    ['DS5', 2019, True],
    ['Aston Martin DB4', 2006, False],
    ['Palio Weekend', 2012, False],
    ['A5', 2019, True],
    ['Série 3 Cabrio', 2009, False],
    ['Dodge Jorney', 2019, False],
    ['Carens', 2011, False]
]
print(dados)
print('\n')

zero_km_Y = []
for lista in dados:
    if (lista[-1] == True):
        zero_km_Y.append(lista)

print(zero_km_Y)

zero_km_N = []
for lista in dados:
    if (lista[-1] == False):
        zero_km_N.append(lista)

print(zero_km_N)

print('\n')

[lista for lista in dados if lista[-1] == True]
[lista for lista in dados if lista[-1] == False]

print('\n')

zero_km_Y, zero_km_N = [] , []
for lista in dados:
    if (lista[-1] == True):
        zero_km_Y.append(lista)
    else:
        zero_km_N.append(lista)

print('\n')

A, B, C = [], [], []
for lista in dados:
    if(lista[1] <= 2000):
        A.append(lista)
    elif(lista[1] > 2000 and lista[1] <= 2010):
        B.append(lista)
    else:
        C.append(lista)
    
        

    