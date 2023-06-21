import mysql.connector
from mysql.connector import Error

class DAO:
    def __init__(self):
        try:
            conexion = mysql.connector.connect(user='root', password='', 
                                               host='localhost', port='3306',
                                               database='trabajadores'
                                               )
            print(conexion)
            print("Conexion exitosa")
        except Error as ex:
            print("Error de conexión: {0} ".format(ex))
    