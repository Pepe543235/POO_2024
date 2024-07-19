import mysql.connector

try:
#conectar con la BD en MYSQL

  conexion=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bd_notasW'
)
except Exception as e:
 print(f"tipo de excepcion:{type(e)._name_}")
 print("ocurrio un error con la conexion al server")


     