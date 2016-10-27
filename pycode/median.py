# -*- coding: utf-8 -*-

"""
La mediana representa el valor en la posición central de un conjunto de datos ordenados. 
En una lista con un número impar de elementos la mediana se encuentra en la posición central. 
Si la lista tiene un número par de elementos, no existe un valor central que divida la lista 
en dos partes iguales por lo que la mediana equivale a la media de los dos valores centrales. 
En esta misión, recibirás una lista no vacía de números naturales (X). Con ella deberás de separar 
la parte superior e inferior para encontrar la mediana.

Entrada: Lista de enteros.

Salida: La mediana en formato entero/flotante.

"""


def checkio(data):
    data.sort()

    mediana = 0

    if len(data) % 2 != 0:
        mediana = data[len(data) / 2]
    else:
        mediana = (data[len(data) / 2 - 1] + data[len(data) / 2]) / 2.0

    return mediana


def main():
    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    #assert checkio(range(1000000)) == 499999.5, "Long."


if __name__ == '__main__':
    main()
