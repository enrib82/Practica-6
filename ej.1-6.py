# -*- coding: cp1252 -*-
"""Enrique Ibáñez Orero - 1º DAW - Practica 5 - Ejercicio 1 - Pràctica 6. Escribe un programa que permita crear una lista de palabras. Para ello, el programa tiene que
pedir un número y luego solicitar ese número de palabras para crear la lista. Por último, el
programa tiene que escribir la lista.
"""

contador=1
num=int(raw_input("Dime cuantas palabras tiene la lista: "))
li=[]
if num < 1:
    print("No puede ser")
else:
    for i in xrange(1,num+1):
        li.append(raw_input("Palabra %d: " %contador))
        contador += 1
print "La lista creada es:", li
