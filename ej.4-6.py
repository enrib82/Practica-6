# -*- coding: cp1252 -*-
"""Enrique Ibáñez Orero - 1º DAW - Practica 6 - Ejercicio 4 - Pràctica 6.
Escribe un programa que permita crear una lista de palabras
 y que, a continuación, pida una
palabra y elimine esa palabra de la lista. """


num=int(raw_input("Dime el numero de palabras: "))
cont=1
if num<1:
    print("No puede ser")
else:
    li=[]
    for i in xrange(1,num+1):
        li.append(raw_input("Palabra %d: " %cont))
        cont += 1
print li

eliminar=raw_input("Palabra a eliminar: ")

while eliminar in li:
     li.remove(eliminar)

print li
