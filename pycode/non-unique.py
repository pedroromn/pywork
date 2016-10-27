# -*- coding: utf-8 -*-

"""
Se te dará una lista no vacía de enteros (X). Para esta misión, 
deberás retornar una lista que consista únicamente de elementos 
no únicos. Para hacerlo, necesitarás remover todos los ementos 
que sean únicos (elementos que aparezcan una sola vez en la lista dada).
Al resolver esta misión, no cambies el orden de la lista. Ejemplo: 
[1, 2, 3, 1, 3] 1 y 3 no son elementos 
únicos y el resultado será [1, 3, 1, 3].

"""

# data -> lista

def checkio(data):
    lista = []
    for item in data:
        if data.count(item) != 1:
            lista.append(item)
    
    return lista


def main():
    print checkio([1, 2, 3, 1, 3])
    print
    print checkio([1, 2, 3, 4, 5])
    print
    print checkio([5, 5, 5, 5, 5])
    print
    print checkio([10, 9, 10, 10, 9, 8])  


if __name__ == '__main__':
    main()    