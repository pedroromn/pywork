#!/usr/bin/env python
# -*- coding: utf-8 -*-


print "\nCREACIÓN DE UNA MATRIZ EN PYTHON"

numero_filas = int(raw_input("\tNumero de filas: "))
numero_columnas = int(raw_input("\tNumero de columnas: "))

# Se crea una matriz con tan solo una línea de código
matriz = [[0] * numero_columnas for i in range(numero_filas)]

print

for i in range(numero_filas):
    print "\t"
    for j in range(numero_columnas):
        print "[" + str(matriz[i][j]) + "]",
    print

print "\n"
