"""
Existe una estructura de condicion llamada "if"
la cual evalua una condicion para encontrar el valor "True" o se cumple
la condicion se ejecuta la linea o lineas codigo

Tenemos 3 tipos de if

1.- If simple
2.- If compuesto}
3.- If anidado
4.- If y else if 
"""

#Ejemplo 1 if simple
color=""
if color=="rojo" :
    print("Soy el color rojo")

#Ejemplo de if compuesto

if color=="rojo" :
    print("Soy el color rojo")
else:
    print("No soy rojo")

#Ejemplo de if anidado

if color=="rojo" :
    print("Soy el color rojo")
    if color!="rojo":
        print("Soy otro color")
else:
    print("No soy rojo")
    if color!="rojo":
        print("Soy otro color")

#Ejemplo de if con elif

color="rojo"
if color=="rojo" :
    print("Soy el color rojo")
elif color=="negro":
    print("Soy el color negro")
elif color=="verde":
    print("Soy el color verde")
else:
    print("No soy rojo, verde o negro")