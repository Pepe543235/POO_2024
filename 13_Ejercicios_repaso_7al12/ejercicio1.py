"""
Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 

 a.- Recorrer la lista y mostrarla
 b.- hacer una funcion que recorra la lista de numeros y devuelva un string
 c.- ordenarla y mostrarla
 d.- mostrar su longitud
 e.- buscar algun elemento que el usuario pida por teclado
 """
#a
celular=["Iphone","Samsung","Huawei","Oppo"]


for i in celular:
   print(f"{celular.index(i)+1}.- {i}")

#b
def dev_str(lista):
    for i in numeros:
        print(str(numeros.index(i)))

    return ', '.join(map(str, lista))
numeros = [1, 2, 3, 4, 5]
resultado = dev_str(numeros)
print(resultado)

#c
celular.sort()
print(celular)

#d
print(celular.len)

#e
palabra_buscar=input("Ingresa la palabra a buscar: ")

p=0
for i in celular:
    p+=1
    if palabra_buscar =="Iphone":
        print(f"La palabra {i} esta ubicada en la posición {celular.index(i)}")
        break
    elif palabra_buscar =="Samsung":
        print(f"La palabra {i} esta ubicada en la posición {celular.index(i)}")
        break
    elif palabra_buscar =="Huawei":
        print(f"La palabra {i} esta ubicada en la posición {celular.index(i)}")
        break
    elif palabra_buscar =="Oppo":
        print(f"La palabra {i} esta ubicada en la posición {celular.index(i)}")
        break
    else: 
        print("La palabra no existe")
        break