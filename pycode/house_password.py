# -*- coding: utf-8 -*-

"""
Stephan y Sophia no se preocupan por la seguridad y usan contraseñas sencillas para todo. 
Ayuda a a Nikola a desarrollar un módulo para verificar la seguridad de la contraseña o password. 
La contraseña será considerada suficientemente fuerte si el largo es mayor o igual a 10 caracteres, 
tiene por lo menos un dígito, así como una letra en mayúscula y una letra en minúscula. 
La contraseña contiene solo letras latinas o dígitos ASCII.

Entrada: La contraseña como una cadena o string (Unicode para python 2.7).

Salida: Si la contraseña es segura o no representada mediante un booleano o cualquier 
otro tipo de dato que pueda ser convertido y procesado como un booleano. En los resultados 
finales podrás ver los resultados convertidos.

"""

# largo >= 10
# tiene por lo menos un dígito
# letra en mayúscula
# letra en minúscula
# letras latinas o dígitos ASCII

# Se recibirán cadenas unicode


import re

def checkio(password):

    has_digit = False
    has_upper = False
    has_lower = False

    if re.match("[a-zA-Z0-9]+", password) and 10 <= len(password) <= 64:
        for c in password:
            if c.isdigit():
                has_digit = True
                continue
            if c.isupper():
                has_upper = True
                continue
            if c.islower():
                has_lower = True
                continue

            if has_digit and has_lower and has_upper:
                break

        if  has_digit and has_lower and has_upper:
            return True
        else:
            return False
    else:
        return False



def main():
   print checkio(u'bAse730onE4'), checkio(u'asasasasasasasaas'), checkio(u'QWERTYqwerty');
   print checkio(u'123456123456'), checkio(u'QwErTy911poqqqq')


if __name__ == '__main__':
    main()