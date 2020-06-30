# -*- coding: utf-8 -*-

"""
Date: 20/08/2015
author: peyoromn

"""

import random

digitos = ('1', '2', '3', '4', '5', '6', '7', '8', '9')

codigo = ''

for i in range(4):
	candidato = random.choice(digitos)
	while candidato in codigo:
		candidato = random.choice(digitos)
	codigo += candidato

print "Bienvenido al Mastermind!"
print "Tienes que adivinar un numero de 4 cifras distintas"

propuesta = raw_input("¿Que codigo propones?: ")

intentos = 1

while propuesta != codigo:
	intentos += 1
	aciertos = 0
	coincidencias = 0

	for i in range(4):
		if propuesta[i] == codigo[i]:
			aciertos += 1
		elif propuesta[i] in codigo:
			coincidencias += 1

	print "Tu propuesta (", propuesta,") tiene", aciertos, \
		"aciertos y ", coincidencias, "coincidencias."
        propuesta = raw_input("¿Cual otro codigo propones?: ")

print "Felicitaciones! adivinaste el codigo en ", intentos, "intentos"