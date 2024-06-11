#Aqui se realiza lo que Angel haga en el video

# Definimos una función lambda para mezclar ingredientes
mezclar_ingredientes = lambda ing1, ing2: f'Mezclando {ing1} con {ing2}'

# Utilizamos la función lambda para mezclar ingredientes
resultado = mezclar_ingredientes("harina", "azúcar")

# Imprimimos el resultado
print(resultado)  # Esto imprimirá "Mezclando harina con azúcar"
# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usamos una función lambda para filtrar los números pares
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

# Imprimimos el resultado
print(numeros_pares)  # Esto imprimirá [2, 4, 6, 8, 10]

def solicitarDatos():
    if opcion=="5":
        print("Bye bye")
        return None
    global n1,n2,ope
    n1=int(input("Numero #1: "))
    n2=int(input("Numero #2: "))
    ope=input("Operacion: ").upper()
    print(getCalculadora(n1,n2,ope))


def getCalculadora(num1,num2,operacion):
    if operacion=="1" or operacion=="+" or operacion=="SUMA":
        resultado=f"{num1}+{num2}={int(num1)+int(num2)}"
    elif operacion=="2" or operacion=="-" or operacion=="RESTA":
        resultado=f"{num1}-{num2}={int(num1)-int(num2)}"  
    elif operacion=="3" or operacion=="*" or operacion=="MULTIPLICACION":
        resultado=f"{num1}*{num2}={int(num1)*int(num2)}"        
    elif operacion=="4" or operacion=="/" or operacion=="DIVISION":
        resultado=f"{num1}/{num2}={int(num1)/int(num2)}"      
    return resultado

print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.-Multiplicacion \n 4.- División \n 5.- SALIR ")
opcion=input("\t Elige una opción: ").upper()


solicitarDatos()

""""
    Los errores de excepciones en un lenguaje de programación no es otra cosa que los errores
    en tiempo de ejecución. Cuando se manejan errores mediantes las excepciones en realidad
    se dice que se evita que se presenten esos erorres en el programa en el tiempo de ejecución
"""
#Ejemplo: se representa un error cuando no es generada una variable
try:
    nombre = input("Dame el nombre completo de una persona: ")

    if len(nombre)>0:
        nombre_usuario="El nombre del usuario del sistema es: "+nombre

    print(nombre_usuario)    
except:
    print("Es necesario introducir un nombre de una persona")    

#Ejemplo: cuando se solicita un numero y se ingresa otra cosa
try: 
    numero = int(input("Ingresa un numero entero")) 

    if numero>0:
        print ("Es positivo")
    else:
        print ("Es negativo")
except ValueError:
    print("No es posible convertir una letra a un numero")

#Ejemplo 3: cuando se generan multiples excepciones
try:
    numero1=int(input("Ingresa un numero: "))
    print("El cuadrado del numero es: "+str(numero1+numero1))
except TypeError:
    print("Es necesario convertir el numero a entero")
except ValueError:
    print("No es posible convertir una letra a numero")
else:
    print("Todo se ejecuto correctamente")        
finally:
    print("Ya termino")