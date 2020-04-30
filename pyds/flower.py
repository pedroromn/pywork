# -*- coding: utf8 -*-


class Flower(object):
    """ clase Flower """
    def __init__(self, name, petals, price):
        self._name = name
        self._petals = petals
        self._price = price

    def set_price(self, new_price):
        """ configura el precio """
        self._price = new_price

    def set_name(self, new_name):
        """ configura el nombre """
        self._name = new_name

    def set_petals(self, new_petals):
        """ configura numero de petalos """
        self._petals = new_petals

    def get_name(self):
        """ retorna nombre """
        return self._name

    def get_petals(self):
        """ retorna numero de petalos """
        return self._petals

    def get_price(self):
        """ retorna precio """
        return self._price