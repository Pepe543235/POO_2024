"""3.- 

Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla con 
 palabras o frases hasta que el usuario asi lo crea conveniente, posteriormente imprimir 
 el contenido de la lista en mayusculas
"""

lista=[]
op=0
if len(lista) == 0:
    while op!="No" and op!="no":
        palabra=input("Escriba la palabra que quiera ")
        lista.append(palabra)
        op=input("¿Desea continuar? ")

print(lista.upper())
