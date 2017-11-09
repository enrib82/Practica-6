# -*- coding: cp1252 -*-
"""Enrique Ibáñez Orero - 1º DAW - Practica 6 - Ejercicio 5 - Pràctica 6.
Escribe un programa que permita crear dos listas de palabras y que,
 a continuación, elimine de la
primera lista los nombres de la segunda lista. """

contador=1
num=int(raw_input("Dime cuantas palabras tiene la lista: "))


if num < 1:
    print("No puede ser")
else:
    li=[]
    for i in range(1,num+1):
        li.append(raw_input("Palabra %d: " %contador))
        contador += 1
print "La lista creada es:", li

num2=int(raw_input("Dime cuantas palabras quieres eliminar de la lista: "))

if num2 < 1:
    print("No puede ser")
else:
        eliminar=[]
        for i in range(1,num2+1):
            li.remove(raw_input("Dime las palabra que quieres eliminar: " ))

        print "La lista de palabras a eliminar es:" ,eliminar

        for i in eliminar:
            for j in range(len(li)-1, -1, -1):
                if li[j] == i:
                    del(li[j])
        print "La lista es ahora:", li
