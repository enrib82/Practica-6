# -*- coding: cp1252 -*-
"""Enrique Ibáñez Orero - 1º DAW - Practica 6 - Ejercicio 3 - Pràctica 6.
Escribe un programa que permita crear una lista de palabras y que, a continuación, pida dos
palabras y sustituya la primera por la segunda en la lista. """



num=int(raw_input("Numero de palabras: "))
cont=1
if num<1:
    print("No puede ser")
else:
    li=[]
    for cadena in xrange(1,num+1):
        li.append(raw_input("Palabra %d: " %cont))
        cont += 1
print li
buscar=raw_input('buscar la palabra... ')

subs=raw_input('sustituir por la palabra... ')
cont=0
for cadena in li:
     if cadena==buscar:
         li[cont]=subs
     cont += 1

print li
