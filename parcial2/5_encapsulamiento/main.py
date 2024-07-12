
from coches import *
"""
print("Objeto 1")
coche1=Coches("Blanco","VW","2022",220,150,5)
coche1.getInfo()


print("Objeto 2")
coche2=Coches("Azul","Nissan","2020",180,150,6)
coche2.getInfo()
"""

print(coche1.publico_atributo)

#Nota: para utilizar un atributo privado se tendria que hacer dentro de un metodo que fuera publico


#print(coche1.__getPrivadoAtributo) esto no es posible

print(coche1.getPrivadoAtributo)

#Nota 2: Para usar un metodo privado es necesario hacerlo dentro de un metodo publico

def getMetodoPublico(self):
    self.__getMetodoPrivado()