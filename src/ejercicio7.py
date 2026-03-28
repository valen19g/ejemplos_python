import random 
nombres = input('ingrese nombres separados por , ')
lista_nombres = []

for n in nombres.split(','):
    lista_nombres.append(n.strip())

mezclados = lista_nombres.copy()
random.shuffle(mezclados)
for i in range(len(lista_nombres)):
    if lista_nombres[i]!= mezclados[i]:
        print(f'{lista_nombres[i]} -> {mezclados[i]}')
       
    