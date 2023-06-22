import mysql.connector
from mysql.connector import Error

class DAO:
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(user='root', password='', 
                                               host='localhost', port='3306',
                                               database='trabajadores'
                                               )
            print(self.conexion)
            print("Conexion exitosa")
        except Error as ex:
            print("Error de conexión: {0} ".format(ex))
    
    def RegistrarTrabajador(self, trabajador):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor(buffered=True)
                # OBTENER EL ID DEL SEXO
                query = "SELECT id FROM sexo WHERE nombre = {0}"
                cursor.execute(query.format(trabajador.sexo))
                resultado = cursor.fetchone()
                id_sexo = resultado[0]
                
                # INSERTAR TRABAJADOR
                query = "INSERT INTO trabajador (rut, rut_dv, nombre, apellido, sexo, direccion) VALUES ({0},{1},{2},{3},{4},{5})"
                cursor.execute(query.format(trabajador.rut, trabajador.rut_dv, trabajador.nombre, trabajador.apellido, id_sexo, trabajador.direccion))

                # INSERTAR TELEFONOS
                query = "INSERT INTO telefono (numero, trabajador_rut) VALUES({0},{1})"
                for telefono in trabajador.telefonos:
                    cursor.execute(query.format(telefono, trabajador.rut))
                    
                # OBTENER ID CARGO, ID DEPARTAMENTO Y FORMATEO FECHA
                query = "SELECT id FROM cargo WHERE nombre = {0}"
                cursor.execute(query.format(trabajador.cargo))
                resultado = cursor.fetchone()
                id_cargo = resultado[0]
                
                query = "SELECT id FROM areadepartamento WHERE nombre = {0}"
                cursor.execute(query.format(trabajador.departamento))
                resultado = cursor.fetchone()
                id_departamento = resultado[0]   
                
                fecha = str(trabajador.fecha_aaaa) + "-" + str(trabajador.fecha_mm) + "-" + str(trabajador.fecha_dd)
                
                # INSERTAR DATOSLABORALES
                query = "INSERT INTO datoslaborales (cargo_id, area_departamento, fecha_ingreso, trabajador_rut) VALUES({0},{1},{2},{3})"
                cursor.execute(query.format(id_cargo, id_departamento, fecha, trabajador.rut))
                
                # COMMIT
                self.conexion.commit()
                
            except Error as ex:
                print("Error de conexión: {0} ".format(ex))
                self.conexion.rollback