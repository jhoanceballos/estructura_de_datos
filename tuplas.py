#las tuplas  no se pueden modificar despues de creadas
# las tuplas son immutables no se pueden modificar una vez creadas
"""las listas se crean con [], las tuplas se crean con ()"""
tupla = (1, 2, 3, 4, 5)
print(tupla)
#operaciones de las tuplas
print(len(tupla))# longitud de la tupla
print(tupla[0])# primer elemento de la tupla
print(tupla[-1])# ultimo elemento de la tupla
#buscar un elemento
print(tupla.index(3))# devuelve el indice del elemento 3
# otra forma usando index
print(tupla.index(3))# devuelve el indice del elemento 3