#! -*- coding: utf-8 -*-
# Algoritmo de búsqueda binaria para encontrar raíz cuadrada de un entero


def main():
    """Algoritmo de búsqueda binaria para encontrar 
    raíz cuadrada de un entero"""
    
    objetivo = int(input("Escoge un numero: "))
    epsilon = 0.00001 # precisión en la respuesta
    
    # definimos el espacion de búsqueda inicial
    # subconjunto de númneros reales
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2
    
    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
            
        respuesta = (alto + bajo) / 2
        
    print(f"La raíz cuadrada de {objetivo} es {respuesta}")
    
    
if __name__ == "__main__":
    main()