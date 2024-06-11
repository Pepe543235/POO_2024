
paises=["Mexico","USA","Brasil","Japon"]
numeros=[23,43,65,33,24,100,24]
texto=["Hola",True,23,3.1416]

#Ordenar una lista

print(paises)
paises.sort()
print(paises)

print(numeros)
numeros.sort()
print(numeros)
"""
no es posible:
print(texto)
texto.sort()
print(texto)
"""

#añadir elementos
print(texto)
texto.insert(len(texto),"True")
print(texto)
texto.insert(len(texto),True)#inserta un elemento en un indice especifico
print(texto)
texto.append(False)#inserta un valor al final de la lista
print(texto)

#eliminar elementos
print(numeros)
numeros.remove(23)
print(numeros)
numeros.pop(0)
print(numeros)

#Dar la vuelta a una lista

print(numeros)
numeros.reverse()
print(numeros)

#Buscar un dato dentro de una lista
respuesta="Brasil" in paises
print(respuesta)

#Cuantas veces aparece un valor dentro de una lista

print(numeros)
numeros.append(24)
cuantos=numeros.count(24)
print("El numero 23 se encontro {cuantos}")

#Unir listas

print(paises)
paises.extend(numeros)
print(paises)

