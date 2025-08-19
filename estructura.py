#listas creaciion
lista= [1, 2, 3, 4, 5,6, 7, 8, 9, 10] # lista de numeros
print(lista) #imprimir lista
#listas acceso
print(lista[6])  # acesso al elemento en la posicion 6
#lista vacia
lista_vacia = [] # lista vacia
# lista vacia voy a imgresar elementos
lista_vacia.append(1) # un elemento tipo entero
print(lista_vacia) #imprimir lista
# un elemento tipo texto
lista_vacia.append("hola") # un elemento tipo texto
print(lista_vacia) #imprimir lista
# insertar un boleano en  la enmedio de 0 y 1
lista_vacia.insert(1, True) # insrtar un elemento en la lista vacia
print(lista_vacia) #imprimir lista
#mostar el ultimo elemento de dato de la lista
print(lista_vacia[-1]) # acceder al ultimo elemento de la lista
# listas longitud
print(len(lista_vacia)) # longitud de la lista
# listas eliminar
lista_vacia.remove(1) # eliminar el elemento 1 de la lista
# para que es pop() elimina el ultimo elemento de la lista
lista_vacia.pop() # eliminar el ultimo elemento de la 
print(lista_vacia) #imprimir lista
#moficar un elemento de la lista
lista_vacia[0] = "modificado" # modificar el primer elemento de la lista
print(lista_vacia) #imprimir lista despues de modificar

# estender una lista
lista_vacia.extend([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) # extender la lista
print(lista_vacia) #imprimir lista despues de extender
#lista de listas
lista_de_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # lista de listas
print(lista_de_listas) #imprimir lista de listas
# acceder a un elemento de una lista de listas
print(lista_de_listas[1][2]) # acceder al elemento 6 de la lista
#llenar lista con valores aleatorios
import random
lista_aleatoria = []
for i in range(10):
    lista_aleatoria = [random.randint(1, 100) for i in range(10)]
print(lista_aleatoria) #imprimir lista de valores 
# usando numpy para valores aleatorios en una lista
import numpy as np
lista_numpy = np.random.randint(1, 100, size=10).tolist()  # generar una lista de 10 numeros aleatorios
print(lista_numpy)  # imprimir lista de valores aleatorios con numpy
# operaciones de la lista
lista_numpy.sort()  # ordenar la lista
print(lista_numpy)  # imprimir lista ordenada
# invertir la lista
lista_numpy.reverse()  # invertir la lista
print(lista_numpy)  # imprimir lista invertida
# buscar un elemento en la lista
print(30 in lista_numpy)  # buscar el elemento 30 en la lista)
# buscar en lista vacia
print (2 in lista_vacia)  # buscar el elemento 2 en la lista vacia
# buscar pero con index
print(lista_vacia.index(3)) # buscar el elemento 3 en la lista vacia
# contar el numero de veces que aparece un elemento en la lista
print(lista_numpy.count(50)) # contar el numero de veces que aparece el elemento 30 en la lista
# copiar una lista
lista_copiada = lista_numpy.copy()  # copiar la lista
print(lista_copiada)  # imprimir lista copiada
# sumar dos listas
lista_copia = lista_numpy[:] # copiar la lista numpy
print(lista_copia)  # imprimir lista copiada
# limpiar una lista
lista_numpy.clear()  # limpiar la lista
print(lista_numpy)  # imprimir lista limpia
# concatenar listas 
lista_concatenada = lista_vacia + lista_copiada # concatenar las listas
print(lista_concatenada)  # imprimir lista concatenada
# sacar el mayor valor de una lista
print(max(lista_copiada))  # sacar el mayor 
#tamaño de la lista copiada
print(len(lista_copiada))  # imprimir el tamaño de la lista copiada