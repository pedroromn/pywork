# IPython log file

"""

DICCIONARIOS

"""
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel
tel['jack']
del tel['sape']
tel
tel['irv'] = 4127
tel
tel.keys()
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{x: x**2 for x in (2, 4, 6)}
for i, v in enumerate(['tic', 'tac', 'toe'])
for i, v in enumerate(['tic', 'tac', 'toe']):
    print i, v
    
for i in reversed(xrange(1,10,2)):
    print i
    
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.iteritems():
    print k, v
    
knights.iteritems()
print knights.iteritems()
string1, string2, string3 = '', 'Trondheim', 'Hamer Dance'
string1
string2
string3
string1 or string2
string2 or string3
string2 and string3
diccionario = {'color': "violeta", 'talle': "XS", 'precio': 174.25}
remera = diccionario.copy()
remera
remera['reservado'] = "SI"
remera
diccionario
remera.clear()
remera
remera = diccionario.copy()
musculosa = remera
musculosa
remera.clear()
musculosa
remera
secuencia = ["color", "talle", "marca"]
diccionario1 = dict.fromkeys(secuencia)
diccionario1
diccionario2 = dict.fromkeys(secuencia, 'valor x defecto')
diccionario2
a = "fdfd"
import string
get_ipython().magic(u'pinfo2 string.atoi')
l = ['c', 'a', 's', 'a']
str(l)
ord('a')
ord('b')
'a' < 'b'
diccionario1.update(diccionario2)
diccionario1
remera['color']
remera = diccionario1.copy()
remera
remera['color']
remera.get('color')
remera.get('color', 'talle')
remera.has_key('color')
remera.keys()
remera.values()
len(remera)
remera.get('job', None)
remera
for k in remera.iterkeys():
    print k
    
remera.pop()
remera.pop('color')
remera
remera.popitem()
remera.viewkeys()
b = remera.viewkeys()
b
diccionario1.items()
diccionario1
diccionario1.get('t', None)
f = diccionario1.get('t', None)
f
diccionario1.get('t')
diccionario1.get('color')
diccionario1.get('color')
get_ipython().magic(u'logstart diccionarios.py')
exit()
