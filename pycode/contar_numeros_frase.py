# -*- coding: utf-8 -*-

"""
Date: 20/08/2015
author: peyoromn

"""


def contar_numeros(frase):
	#numeros = 0
	temp = ""
	lista_numeros = []
	for subcadena in frase.split():
		if subcadena.isdigit():
			lista_numeros.append(subcadena)
			#numeros += 1
		else:
			for c in subcadena:
				if c.isdigit():
					temp += c
			if temp != "":
				lista_numeros.append(temp)
				#numeros += 1
				temp = ""

	return lista_numeros



def main():
	print 
	frase = raw_input("Escriba una frase: ")
	numeros = contar_numeros(frase)
	print 
	print "Su frase tiene {} numeros: ".format(len(numeros))
	for n in numeros:
		print n, 



if __name__ == '__main__':
		main()
