# IPython log file

lenguajes = ["c", "c++", "python", "R", "matlab", "java", "c#"]
lenguajes.append("go")
lenguajes
otros_lenguajes = ["ruby", "javascript", "php", "scala"]
lenguajes.extend(otros_lenguajes)
lenguajes
lenguajes.insert(6, "prolog")
lenguajes
lenguajes.pop()
lenguajes
lenguajes.pop(5)
lenguajes.remove("php")
lenguajes
lenguajes.reverse()
lenguajes
lenguajes.sort()
lenguajes
lenguajes.sort(reverse=True)
lenguajes
lenguajes.count("python")
lenguajes.count("python")
lenguajes.index("python")
max(lenguajes)
len(lenguajes)
cadena = "cadena"
uni_cadena = u"cadena"
cadena
uni_cadena
get_ipython().magic(u'pinfo cadena.encode')
c = " "
c.isspace()
c = " cd"
c.isspace()
c = "cd cd" 
c.isspace()
def mod_lista(lista):
    lista.append("xxxx")
    
mod_lista(lenguajes)
lenguajes
def mod_lista(lista):
    if lista is not None:
        lista.append("fdfd")
        
mod_lista(lenguajes)
lenguajes
mod_lista()
mod_lista([])
[]
a = []
mod_lista(a)
a
get_ipython().magic(u'save practica_listas.py')
get_ipython().magic(u'logstart practica_listas.py')
get_ipython().magic(u'ls ')
get_ipython().magic(u'edit practica_listas.py')
exit()
