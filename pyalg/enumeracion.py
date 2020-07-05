#! -*- coding: utf-8 -*-
# Obtner la raiz cuadrada de un número 

def main():
    """Obtener la raiz cuadrada de un número"""
    objetivo = int(input("Escoge un entero: "))
    respuesta = 0
    
    while respuesta**2 < objetivo:
        respuesta += 1
        
    if respuesta**2 == objetivo:
        print(f"La raiz cuadrada de {objetivo} es {respuesta}")
    else:
        print(f"{objetivo} no tiene una raiz cuadrada exacta")


if __name__ == "__main__":
    main()