#Nota: cuando se imprime en pantalla una cadena de caracteres
#se trabaja por default con "cadenas", es decir python no 
#puede concatenar otra cosa que no sea un String (str)

texto="Soy una cadena de caracteres"
numero=23

#Concatenar cadena str con str

print("soy otra cadena "+texto)

#Concatenar str con int

numero_str=str(numero)
print("EL numero: "+numero_str)
print("EL numero: "+str(numero))

#Concatenar un entrero con un string
n1=int('23')
n2=33

suma=n1+n2

print("La suma es: "+str(suma))
print(f"La suma es: {suma}")

#Concatenar float y int con str

n1=23.99
n2=33.0

suma=float(n1+n2)

print(f"La suma es: {suma}")