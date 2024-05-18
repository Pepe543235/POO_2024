#El ciclo while es una estructura de control que itera o repite la ejecucion de una serie de instrucciones
#tantas veces como la condicion se cumpla 'True'
#Sintaxis
#while condicion
#   bloque de instruccion

#Ejemplo 1 crear un programa que imprima 5 veces @
contador=1
while contador<=5:
    print("@")
    contador+=1

#Ejemplo 2 Crear un programa que imprima los numeros del 1 al 5 los sume y al final imprima la suna
contador=1
suma=0
while contador<=5:
    print(contador)
    suma+=contador
    contador+=1
print(f"La suma es: {suma}")

#Ejemplo 3 Crear un programa que solicite un numero entero y a continuacion imprima la tabla de multiplicar correspondiente
numero=int(input("Ingresa un numero"))
multi=0
i=1
while i<=10:
    multi=i*numero
    print(f"{numero} x {i} = {multi}")
    i+=1