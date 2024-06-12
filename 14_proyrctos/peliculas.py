import os
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

    elif operacion=="3" or operacion=="Actualizar" or operacion=="aztualizar":
                    antigua = input("¿Qué película deseas actualizar? ")
                    nueva = input("¿Cuál es el nuevo nombre de la película? ")
                    try:
                        indice = peliculas.index(antigua)

                        peliculas[indice] = nueva
                        print(f"La película '{antigua}' se ha actualizado a '{nueva}'")
                    except ValueError:
                        print(f"La película '{antigua}' no se encuentra en la lista")
    
    elif operacion=="4" or operacion=="Consultar" or operacion=="consultar":
                    if peliculas:
                        print(f"\n Las películas disponibles son: {', '.join(peliculas)}")
                    else:
                        print("\t No hay películas en la lista")

    elif operacion=="5" or operacion=="buscar" or operacion=="Buscar":
                    busca = input("¿Qué película deseas buscar? ")
                    try:
                        i = peliculas.index(busca)
                        print(f"La película '{busca}' está en la posición {i + 1}.")
                    except ValueError:
                        print(f"La película '{busca}' no se encuentra en la lista.")

    elif operacion=="5" or operacion=="buscar" or operacion=="Buscar":
                    busca = input("¿Qué película deseas buscar? ")
                    try:
                        i = peliculas.index(busca)
                        print(f"La película '{busca}' está en la posición {i + 1}.")
                    except ValueError:
                        print(f"La película '{busca}' no se encuentra en la lista.")

    elif operacion=="6" or operacion=="Vaciar" or operacion=="vaciar":
                    peliculas.clear()
                    print("Las peliculas fueron vaciadas correctamente...")
    else:
        print("\t ..---Operación no válida---..")


peliculas=[]
os.system("cls")
op=True
while op:
    print(f"\n .-.-.-CINEPOLIS-.-.-. \n 1.- Agregar \n 2.- Remover \n 3.- Actualizar \n 4.- Consultar peliculas \n 5.- Buscar \n 6.- Vaciar \n 7.- Salir")
    op=input("\t Elija una opcion para realizar a la pelicula: ")
    
    if op!="7":
        opc(op, peliculas)
    else:
      op=False
      print("\n \t ....----Gracias por utilizar el sistema----....")