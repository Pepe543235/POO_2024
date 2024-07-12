from conexionBD import *
try:
   micursor=conexion.cursor()
   nombre=input("¿Cual es el nombre? ")
   direccion=input("¿Cual es tu direccion? ")
   tel=input("¿Cual es tu numero de telefono? ")

   sql="insert into clientes (id,nombre,direccion,tel) values (null,%s,%s,%s)"
   valores=(nombre,direccion,tel)

   micursor.execute(sql,valores)
#sirve para finalizar la ejecución de SQL
   conexion.commit()
except:
  print(f"Hubo un error al subir los datos")
else:
   print(f"Registro insertado exitosamente")