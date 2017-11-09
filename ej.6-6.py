# -*- coding: cp1252 -*-
"""Enrique Ibáñez Orero - 1º DAW - Practica 6 - Ejercicio 6 - Pràctica 6.
Escribe un programa que permita crear una lista de palabras y que, a continuación, cree una
segunda lista igual a la primera, pero al revés (no se trata de escribir la lista al revés, sino de crear
una lista distinta). """


cont=1
num=int(raw_input("Numero de palabras: "))
lista=[]
for i in xrange(1,num+1):
    lista.append(raw_input("Palabra %d: " %cont))
    cont += 1
print "Orden correcto: " ,lista
lista2=lista
lista2.reverse()
print "Orden inverso: " ,lista2
