# -*- coding: cp1252 -*-
"""Enrique Ibáñez Orero - 1º DAW - Practica 6 - Ejercicio 2 - Pràctica 6.
Escribe un programa que permita crear una lista de palabras y que, a continuación, pida una
palabra y diga cuántas veces aparece esa palabra en la lista. """

cont=1
num=int(raw_input("Numero de palabras: "))
if num<1:
    print("No puede ser")
else:
    li=[]
    for i in range(1,num+1):
        li.append(raw_input("Palabra %d: " %cont))
        cont += 1
print li

buscar=raw_input("Palabra a buscar: ")
print "La he encontrado %d veces" %li.count(buscar)
