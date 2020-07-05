#! -*- coding: utf-8 -*-
# aproximación de la raíz cuadrada de un número

def main():
    """Aproximación de la raíz cuadrada 
    de un número"""
    
    # Número del cual queremos conocer su raíz cuadrada
    objetivo = int(input("Escoge un entero: "))
    
    # Margen de error en la respuesta |respuesta^2 - objetivo| = epsilon 
    epsilon = 0.01 # qué tan cerca queremos llegar de la respuesta
    paso = epsilon**2
    respuesta = 0.0
    contador_iteraciones = 1
    contador_de_respuesta_negativa = 0
    
    while abs(respuesta**2 - objetivo) >= epsilon: #and respuesta <= objetivo:
            print(f"contador = {contador_iteraciones} - epsilon = {abs(respuesta**2 - objetivo)} - respuesta = {respuesta}")
            if respuesta < 0:
                contador_de_respuesta_negativa += 1
            respuesta += paso
            contador_iteraciones += 1
    
    print(f"Respuestas negativas: {contador_de_respuesta_negativa}")
    
    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f"No se encontró la raíz cuadrada de {objetivo}")
    else:
        print(f"La raíz cuadrada de {objetivo} es {respuesta}")
            


if __name__ == "__main__":
    main()