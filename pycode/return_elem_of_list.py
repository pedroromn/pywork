# -*- coding: utf-8 -*-

"""You have a list L and an index i,and you want to get
L[i] when i is a valid index into L; otherwise,you want
to get a default value v. If L were a dictionary,you’d use
L.get(i, v), but lists don’t have a get method
"""


def list_get(l, i, v=None):
    assert isinstance(l, list)
    if l is not None:
        if -len(l) <= i < len(l):
            return l[i]
        else:
            return v


def main():
    l = ([1, 2], ['red', 'blue', 'green'], 'datos',
         {1: 'dato1', 2: 'dato2', 3: 'dato3'})
    try:
        temp = list_get(l, -4)
        print temp
        # print L[5]
    except IndexError:
        print "indice de la lista fuera de rango"

if __name__ == '__main__':
    main()
