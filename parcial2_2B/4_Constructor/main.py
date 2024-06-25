
from coches import *
#Crear un objetos o instanciar la clase

#Mostrar los valores inicales del objeto o instancia de la clase
# print(f"Marca: {coche1.marca} {coche1.color}, numeros de plazas: {coche1.plazas} \nModelo: {coche1.modelo} con una velocidad de {coche1.velocidad} Km/h y un potencia de {coche1.caballaje} hp")
print("Objeto 1")
coche1=Coches("Blanco","VW","2022",220,150,5)
coche1.getInfo()

#Utilizar los metodos set para cambiar o modificar los valores de los atributos aun cuando tengan un valor o no ... aunque los valores solo cambiaran para el objeto o instancia en cuestion en el momento que otro objeto se crea si se tienen valores iniciales se crea con los valores de los atributos de clase 

#actualizar todas las propiedades de objeto

print("Objeto 2")
coche2=Coches("Azul","Nissan","2020",180,150,6)
coche2.getInfo()

#Aunque con los atributos se puede mostrar un valor se recomienda que sea a traves de los getters
# print(f"Marca: {coche1.getMarca()} {coche1.getColor()}, numeros de plazas: {coche1.getPlazas()} \nModelo: {coche1.getModelo()} con una velo…