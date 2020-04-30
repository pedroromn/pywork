# -*- coding: utf-8 -*-

cantidad = int(raw_input("Cantidad: "))

valores = [500, 200, 100, 50, 20, 10, 5, 2, 1]
dinero = []

if cantidad != 0:
	for i in range(len(valores)):
		dinero.append(cantidad / valores[i])
		if dinero[i] == 0:
			continue
		else:
			cantidad = cantidad % valores[i]
	print dinero
else:
	print "0€"
