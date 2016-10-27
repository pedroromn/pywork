# -*- coding: utf-8 -*-

"""
Date: 20/08/2015
author: peyoromn

"""

"""
Diseña un programa que lea una cadena y un número entero k y nos diga cuántas
palabras tienen una longitud de k caracteres
"""


def words_long_k(frase, k):
	if frase != "" and k > 0:
		palabras = 0
		for palabra in frase.split():
			if len(palabra) == k:
				palabras += 1
		return palabras
	else:
		return -1


def main():
	print
	frase = raw_input("\tEscriba una frase: ")
	k = int(raw_input("\tDigite un entero positivo (1-9): "))

	res = words_long_k(frase, k)

	print

	if res:
		print "\tEl numero de palabras de la frase que son de longitud {} son {}".format(k, res)
	else:
		print "\tLos datos ingresados no son correctos"
	print

if __name__ == '__main__':
		main()	
