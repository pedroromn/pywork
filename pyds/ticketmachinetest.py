<<<<<<< HEAD
# -*- coding:utf-8 -*-

from __future__ import print_function
from ticketmachine import MaquinaBoleto


def main():
    sep = "**********"
    print(5 * sep)
    print("Máquina de Boletos Simple")
    print("Compre su boleto")
    sep = "**********"
    print(5 * sep)
    ticket_machine = MaquinaBoleto(1000)
    cantidad = float(input("Introduzca su dinero: "))
    ticket_machine.insertar_dinero(cantidad)
    sep = "**********"
    print(5 * sep)
    print("Saldo Inicial: " + str(ticket_machine.get_saldo()))
    sep = "**********"
    print(5 * sep)
    ticket_machine.imprimir_boleto()
    print("Saldo Final: " + str(ticket_machine.get_saldo()))


if __name__ == '__main__':
    main()
=======
# -*- coding:utf-8 -*-

from __future__ import print_function
from ticketmachine import MaquinaBoleto


def main():
    sep = "**********"
    print(5 * sep)
    print("Máquina de Boletos Simple")
    print("Compre su boleto")
    sep = "**********"
    print(5 * sep)
    ticket_machine = MaquinaBoleto(1000)
    cantidad = float(raw_input("Introduzca su dinero: "))
    ticket_machine.insertar_dinero(cantidad)
    sep = "**********"
    print(5 * sep)
    print("Saldo Inicial: " + str(ticket_machine.get_saldo()))
    sep = "**********"
    print(5 * sep)
    ticket_machine.imprimir_boleto()
    print("Saldo Final: " + str(ticket_machine.get_saldo()))


if __name__ == '__main__':
    main()
>>>>>>> 44aa1ae7f0d12a3db94752192cb82dcca87e5306
