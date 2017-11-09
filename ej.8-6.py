# -*- coding: cp1252 -*-
"""Enrique Ibáñez Orero - 1º DAW - Practica 6 - Ejercicio 8 - Pràctica 6.
Escribe un programa que permita crear una lista de palabras y que, a continuación, ordene la lista
por orden alfabético. """


num=int(raw_input("Dime el numero de palabras: "))
cont=1
if num<1:
    print("No puede ser")
else:
    li=[]
    for i in xrange(1,num+1):
        li.append(raw_input("Palabra %d: " %cont))
        cont += 1
print "La lista es: " ,li

li.sort()
print "La lista ordenada es: " ,li
