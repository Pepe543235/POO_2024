"""2.- 
Escribir un programa  que añada valores a una lista mientras que su longitud 
 sea menor a 120, y luego mostrar la lista: Usar un while y for"""

lista=[]
i=0

while len(lista)<120:
    i+=1
    lista.append(i)

print(lista)

lista2=[]
for i in range(1,121):
    lista2.append(i)

print("\n",lista2)