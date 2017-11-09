# -*- coding: cp1252 -*-
"""Enrique Ibáñez Orero - 1º DAW - Practica 6 - Ejercicio 10 - Pràctica 6.
Escribe un programa que pida un número y a continuación escriba la lista de todos los divisores
del número (incluidos el uno y él mismo)."""


num=int(raw_input("Dime un numero para sacar sus divisores: "))
dividendo=0
if num<1:
    print("No puede ser")
else:
    li=[]
    for i in range(1,num+1):
        if num%i==0:
            dividendo+=1
            li.append(i)

print  num, "tiene" ,len(li), "caracteres" ,li
