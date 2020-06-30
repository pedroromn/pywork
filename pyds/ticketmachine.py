<<<<<<< HEAD
# -*- coding: utf-8 -*-

from __future__ import print_function


class MaquinaBoleto(object):
    """Modela una máquina expendedora de boletos(tickets) simplificada"""

    def __init__(self, precio_boleto):
        self._precio = precio_boleto
        self._saldo = 0
        self._total = 0

    def get_precio(self):
        """Retorna el precio de un boleto en esta máquina"""
        return self._precio

    def get_saldo(self):
        return self._saldo

    def insertar_dinero(self, cantidad):
        while cantidad <= 0:
            cantidad = float(input("Introduzca dinero: "))
        self._saldo += cantidad

    def imprimir_boleto(self):
        """Simula la impresión de un boleto"""
        if self._saldo >= self._precio:
            self.__formato_impresion_boleto()
            # Actualiza el total recolectado
            self._total += self._precio
            # Actualiza el saldo despues de vender un boleto
            self._saldo -= self._precio
        else:
            print("Debe ingresar como mínimo: " + str(self._precio - self._saldo) + "cvos adicionales")

    def retornar_vueltas(self):
        vueltas = self._saldo
        self._saldo = 0
        return vueltas

    def __formato_impresion_boleto(self):
        print("******************************")
        print("*        Línea Blue           ")
        print("*        Boleto               ")
        print("*        " + str(self._precio) + " cvos.")
        print("******************************\n")
=======
# -*- coding: utf-8 -*-

from __future__ import print_function


class MaquinaBoleto(object):
    """Modela una máquina expendedora de boletos(tickets) simplificada"""

    def __init__(self, precio_boleto):
        self._precio = precio_boleto
        self._saldo = 0
        self._total = 0

    def get_precio(self):
        """Retorna el precio de un boleto en esta máquina"""
        return self._precio

    def get_saldo(self):
        return self._saldo

    def insertar_dinero(self, cantidad):
        while cantidad <= 0:
            cantidad = float(raw_input("Introduzca dinero: "))
        self._saldo += cantidad

    def imprimir_boleto(self):
        """Simula la impresión de un boleto"""
        if self._saldo >= self._precio:
            self.__formato_impresion_boleto()
            # Actualiza el total recolectado
            self._total += self._precio
            # Actualiza el saldo despues de vender un boleto
            self._saldo -= self._precio
        else:
            print("Debe ingresar como mínimo: " + str(self._precio - self._saldo) + "cvos adicionales")

    def retornar_vueltas(self):
        vueltas = self._saldo
        self._saldo = 0
        return vueltas

    def __formato_impresion_boleto(self):
        print("******************************")
        print("*        Línea Blue           ")
        print("*        Boleto               ")
        print("*        " + str(self._precio) + " cvos.")
        print("******************************\n")
>>>>>>> 44aa1ae7f0d12a3db94752192cb82dcca87e5306
