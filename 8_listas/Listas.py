import os
"""
list-(Array)
son colecciones o conjunto de datos/valores bajo un msimo nombre, para acceder a los valores se
hace con un indice numerico

Nota: sus valores si son modificables

La lista es una coleccion ordenada y modificable, permite miembros diplicados


#Ejemplo_ Crear una lista con datos numericos e imprimir el contenido

lista=[23,34]
print(lista)

#recorre la lista con for
for i in lista:
    print(i)

#recorrer la lista con while
i=0
while i <= len(lista)-1:
    print(lista[i])
    i+=1

#Ejemplo 2: Crea una lista de 4 palabras, solicitar una palabra y buscar la coincidencia en la lista, indicar si la encontro 
#o no y en que posicion

palabras=["hola","2924","bye","UTD"]

palabra_buscar=input("Ingresa la palabra a buscar: ")

p=0
for i in palabras:
    p+=1
    if palabra_buscar =="hola":
        print(f"La palabra {i} esta ubicada en la posición {palabras.index(i)}")
        break
    elif palabra_buscar =="2024":
        print(f"La palabra {i} esta ubicada en la posición {palabras.index(i)}")
        break
    elif palabra_buscar =="bye":
        print(f"La palabra {i} esta ubicada en la posición {palabras.index(i)}")
        break
    elif palabra_buscar =="UTD":
        print(f"La palabra {i} esta ubicada en la posición {palabras.index(i)}")
        break
    else: 
        print("La palabra no existe")
        break

#Ejemplo 3, añadir y eliminar elementos en una lista
os.system("cls")
numeros=[23,34]
print(numeros)

#agregar ellemento
numeros.append(100)
print(numeros)
numeros.insert(3,100)
print(numeros)

#eliminar elemento
numeros.remove(100)#indicar el elemento a borrar
print(numeros)
numeros.pop(2)#indicar la posicion del elemento a borrar
print(numeros)

#ejemplo 4
agenda=[
   ["Carlos",6182334567],
   ["Karin",6182334568],
   ["Leon",6182334569],
   ["Pedro",6182334569],
]

print(agenda)

for i in agenda:
   print(f"{agenda.index(i)+1}.- {i}")

"""
#Ejemplo 5 Crear un programa que permita gestionar, administrar peliculas, colocar un menu de opciones para
#agregar, remover, consultar peliculas.
#Notas
#1.-Utilizar funciones y mandar llamar desde otro archivo
#2.-Utilizar listas para almacenar los nombres de peliculas

def opc(operacion, peliculas):
     
    if operacion=="1" or operacion=="Agregar" or operacion=="agregar":
            op2="Si"
            while op2=="Si" or op2=="si":
                    agrega=input("¿Qué pelicula agregaras? ")
                    peliculas.append(agrega)
                    print("\t Su pelicula se agrego correctamente")
                    op2=input("\t ¿Desea agregar otra pelicula? (Si/No) ")
          
    elif operacion=="2" or operacion=="Remover" or operacion=="remover":
                op2="Si"
                while op2=="Si" or op2=="si":
                    if peliculas:
                        print(f"Las películas disponibles son: {', '.join(peliculas)}")
                        quitar = input("¿Qué película deseas remover? ")
                        try:
                            peliculas.remove(quitar)
                            print("\t La película se removió correctamente")
                        except ValueError:
                            print("\t -----La película no está en la lista-----")
                    else:
                        print("\t No hay películas para remover")
                    op2 = input("\t ¿Desea remover otra película? (Si/No) ")

    elif operacion=="3" or operacion=="Consultar" or operacion=="consultar":
                    if peliculas:
                        print(f"\n Las películas disponibles son: {', '.join(peliculas)}")
                    else:
                        print("\t No hay películas en la lista")
    else:
        print("\t ..---Operación no válida---..")


peliculas=[]
os.system("cls")
op=True
while op:
    print(f"\n .-.-.-CINEPOLIS-.-.-. \n 1.- Agregar \n 2.- Remover \n 3.- Consultar peliculas \n 4.- Salir")
    op=input("\t Elija una opcion para realizar a la pelicula: ")
    
    if op!="4":
        opc(op, peliculas)
    else:
      op=False
      print("\n \t ....----Gracias por utilizar el sistema----....")