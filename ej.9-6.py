# -*- coding: cp1252 -*-
"""Enrique Ibáñez Orero - 1º DAW - Practica 6 - Ejercicio 9 - Pràctica 6.
Escribe un programa que permita crear una lista de palabras y que,
 a continuación, cree una segunda lista con las palabras de la
 primera, pero sin palabras repetidas (el orden de las palabras
en la segunda lista no es importante). """

cont=1
num=int(raw_input("Numero de palabras: "))
li=[]
for i in range(1,num+1):
    li.append(raw_input("Palabra %d: " %cont))
    cont += 1
print "Tu lista: ",li
li2=[]
for i in li:
    if not i in li2:
        li2.append(i)
li=li2
print "Lista sin repetciones: ",li
