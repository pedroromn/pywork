# -*- coding:utf-8 -*-


class VisorNumero(object):
    """Representa un visor digital de números que puede mostrar
    valores desde cero hasta un determinado límite."""
    def __init__(self, limite):
        self._limite = limite
        self._valor = 0

    def get_valor(self):
        return self._valor

    def set_valor(self, nuevo_valor):
        if nuevo_valor >= 0 and nuevo_valor < self._limite:
            self._valor = nuevo_valor

    def get_valor_visor(self):
        if self._valor < 10:
            return "0" + str(self._valor)
        else:
            return str(self._valor)

    def incrementar(self):
        self._valor = (self._valor + 1) % self._limite


class VisorReloj(object):
    """Implementa un visor para un reloj digital de estilo europeo
    de 24 horas. El reloj muestra horas y minutos"""
    def __init__(self):
        self._horas = VisorNumero(24)
        self._minutos = VisorNumero(60)
        self._cadvisor = ""
        self.actualizar_visor()

    def __init__(self, hora, minuto):
        self._horas = VisorNumero(24)
        self._minutos = VisorNumero(60)
        self.poner_en_hora(hora, minuto)

    def tic_tac(self):
        self._minutos.incrementar()
        if self._minutos.get_valor() == 0:
            self._horas.incrementar()
        self.actualizar_visor()

    def poner_en_hora(self, hora, minuto):
        self._horas.set_valor(hora)
        self._minutos.set_valor(minuto)
        self.actualizar_visor()

    def get_hora(self):
        return self._cadvisor

    def actualizar_visor(self):
        self._cadvisor = str(self._horas.get_valor_visor()) + ":" + \
                         str(self._minutos.get_valor_visor())
