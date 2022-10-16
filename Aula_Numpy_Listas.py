#Se um item pertence ou não a uma lista
Acessorios = ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva']
print(Acessorios)
print('Rodas de liga' in Acessorios)
print('Rodas de liga' not in Acessorios)

print('\n')



#Concatenando listas

A = ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro']
B = ['Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 
'Sensor de chuva']

print(A)
print(B)

print(A + B)

print(len(Acessorios))

print('\n')



#Seleções em listas

print(Acessorios[0])
print(Acessorios[-1]) #-1 acessa o ultimo item da lista, -2 o penultimo e assim sucessivamente

Carro_1 = ['Jetta Variant', 'Motor 4.0 Turbo', 2003, 44410.0, False, ['Rodas de liga', 'Travas elétricas', 'Piloto automático'], 88078.64]
Carro_2 = ['Passat', 'Motor Diesel', 1991, 5712.0, False, ['Central multimídia', 'Teto panorâmico', 'Freios ABS'], 106161.94]
Carros = [Carro_1, Carro_2]
print(Carros[0][0])
print(Carros[0][-2])
print(Carros[0][-2][1] + '\n')

#Slice
print(Acessorios[2:6])
print(Acessorios[2:])
print(Acessorios[:5])

print('\n')

#Metodos de Listas
Acessorios.sort()
print(Acessorios)
Acessorios.append('4 X 4')
print(Acessorios)

Acessorios.pop()
print(Acessorios)
Acessorios.pop(3)
print(Acessorios)

Acessorios_2 = Acessorios.copy() #ou Acessorios_2 = Acessorios[:]
Acessorios_2.append('4 X 4')
print(Acessorios)
print(Acessorios_2)

