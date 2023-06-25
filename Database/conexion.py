import mysql.connector
from mysql.connector import Error
from Clases.Trabajador import Trabajador

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
                query = "SELECT id FROM sexo WHERE nombre = '{0}'"
                cursor.execute(query.format(trabajador.sexo))
                resultado = cursor.fetchone()
                id_sexo = resultado[0]
                
                # INSERTAR TRABAJADOR
                query = "INSERT INTO trabajador (rut, rut_dv, nombre, apellido, sexo, direccion) VALUES ({0},'{1}','{2}','{3}',{4},'{5}')"
                cursor.execute(query.format(trabajador.rut, trabajador.rut_dv, trabajador.nombre, trabajador.apellido, id_sexo, trabajador.direccion))

                # INSERTAR TELEFONOS
                query = "INSERT INTO telefono (numero, trabajador_rut) VALUES('{0}',{1})"
                print(trabajador.telefonos)
                for telefono in trabajador.telefonos:
                    cursor.execute(query.format(telefono, trabajador.rut))
                    
                # OBTENER ID CARGO, ID DEPARTAMENTO Y FORMATEO FECHA
                query = "SELECT id FROM cargo WHERE nombre = '{0}'"
                cursor.execute(query.format(trabajador.cargo))
                resultado = cursor.fetchone()
                id_cargo = resultado[0]
                
                query = "SELECT id FROM areadepartamento WHERE nombre = '{0}'"
                cursor.execute(query.format(trabajador.departamento))
                resultado = cursor.fetchone()
                id_departamento = resultado[0]   
                
                fecha = str(trabajador.fecha_aaaa) + "-" + str(trabajador.fecha_mm) + "-" + str(trabajador.fecha_dd)
                
                # INSERTAR DATOSLABORALES
                query = "INSERT INTO datoslaborales (cargo_id, area_departamento, fecha_ingreso, trabajador_rut) VALUES({0},{1},'{2}',{3})"
                cursor.execute(query.format(id_cargo, id_departamento, fecha, trabajador.rut))
                
                # COMMIT
                self.conexion.commit()
                
            except Error as ex:
                print("Error de conexión: {0} ".format(ex))
                self.conexion.rollback
    
    def ObtenerTrabajadores(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor(buffered=True)
                query = """
                SELECT t.rut, t.rut_dv, t.nombre, t.apellido, sexo.nombre as 'sexo', 
                car.nombre as 'cargo', ad.nombre as 'area_departamento'
                FROM trabajador AS t
                LEFT JOIN datoslaborales AS dl ON t.rut = dl.trabajador_rut
                LEFT JOIN areadepartamento AS ad ON dl.area_departamento = ad.id
                LEFT JOIN cargo AS car ON dl.cargo_id = car.id
                LEFT JOIN sexo ON t.sexo = sexo.id
                """
                cursor.execute(query)

                # Obtener los resultados de la consulta
                resultados = cursor.fetchall()

                # Crear una lista para almacenar los objetos de trabajador
                lista_trabajadores = []

                # Recorrer los resultados y crear los objetos de trabajador
                for fila in resultados:
                    rut, rut_dv, nombre, apellido, sexo, cargo, area_departamento = fila
                    
                    trabajador = Trabajador(
                        rut=rut,
                        rut_dv=rut_dv,
                        nombre=nombre,
                        apellido=apellido,
                        sexo=sexo,
                        direccion="",
                        telefonos=[],
                        datoslabID=0,
                        cargo=cargo,
                        departamento=area_departamento,
                        fecha_dd=1,
                        fecha_mm=1,
                        fecha_aaaa=1
                    )
                    lista_trabajadores.append(trabajador)

                cursor.close()
                return lista_trabajadores
            except Error as ex:
                print("Error de conexión: {0} ".format(ex))
    
    def ObtenerTrabajador(self, rut):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor(buffered=True)
                query = """
                SELECT t.rut, t.rut_dv, t.nombre, t.apellido, sexo.nombre as 'sexo', 
                t.direccion, dl.id as id_datoslaborales, car.nombre as 'cargo', 
                ad.nombre as 'area_departamento', dl.fecha_ingreso
                FROM trabajador AS t
                LEFT JOIN datoslaborales AS dl ON t.rut = dl.trabajador_rut
                LEFT JOIN areadepartamento AS ad ON dl.area_departamento = ad.id
                LEFT JOIN cargo AS car ON dl.cargo_id = car.id
                LEFT JOIN sexo ON t.sexo = sexo.id
                WHERE t.rut = {0}
                """
                cursor.execute(query.format(rut))
                resultado = cursor.fetchone()
                
                trabajador = None
                
                if resultado:
                    # Obtener los valores de los campos del resultado
                    rut, rut_dv, nombre, apellido, sexo, direccion, id_datoslaborales, cargo, area_departamento, fecha_ingreso = resultado

                    # Obtener telefonos
                    listaTelefonos = []
                    query2 = "SELECT numero from telefono WHERE trabajador_rut = {0}"
                    cursor.execute(query2.format(rut))
                    telefonos = cursor.fetchall()
                    
                    for telefono in telefonos:
                        numero = telefono[0]
                        listaTelefonos.append(numero)
                    
                    # Crear el objeto Trabajador con los valores obtenidos
                    trabajador = Trabajador(
                        rut=rut,
                        rut_dv=rut_dv,
                        nombre=nombre,
                        apellido=apellido,
                        sexo=sexo,
                        direccion=direccion,
                        telefonos=[],
                        datoslabID=id_datoslaborales,
                        cargo=cargo,
                        departamento=area_departamento,
                        fecha_dd=fecha_ingreso.day,
                        fecha_mm=fecha_ingreso.month,
                        fecha_aaaa=fecha_ingreso.year
                    )
                cursor.close()
                return trabajador
            except Error as ex:
                print("Error de conexión: {0} ".format(ex))
                
    def RegistrarCargaFamiliar(self, familiar, trabajador_rut):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor(buffered=True)
                # OBTENER EL ID DEL SEXO
                query = "SELECT id FROM sexo WHERE nombre = '{0}'"
                cursor.execute(query.format(familiar.sexo))
                resultado = cursor.fetchone()
                id_sexo = resultado[0]
                
                # OBTENER ID DEL PARENTESCO 
                query = "SELECT id FROM parentesco WHERE nombre = '{0}'"
                cursor.execute(query.format(familiar.parentesco))
                resultado = cursor.fetchone()
                id_parentesco = resultado[0]
                
                # REGISTRAR FAMILIAR
                query = """
                INSERT INTO cargafamiliar(rut, rut_dv, nombre, apellido, sexo, parentesco_id, trabajador_rut)
                VALUES({0},'{1}','{2}','{3}',{4},{5},{6})
                """
                cursor.execute(query.format(familiar.rut, familiar.rut_dv, familiar.nombre,
                                            familiar.apellido, id_sexo, id_parentesco, trabajador_rut))
                self.conexion.commit()
            except Error as ex:
                print("Error de conexión: {0} ".format(ex))
                
    def RegistrarContactoEmergencia(self, contacto, trabajador_rut):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor(buffered=True)
                
                # OBTENER ID DEL PARENTESCO 
                query = "SELECT id FROM parentesco WHERE nombre = '{0}'"
                cursor.execute(query.format(contacto.relacion))
                resultado = cursor.fetchone()
                id_parentesco = resultado[0]
                
                # REGISTRAR CONTACTO
                query = """
                INSERT INTO contactosemergencia(nombre, apellido, relacion, telefono, trabajador_rut)
                VALUES('{0}','{1}',{2},'{3}',{4})
                """
                cursor.execute(query.format(contacto.nombre, contacto.apellido, id_parentesco, contacto.telefono, trabajador_rut))
                self.conexion.commit()
                
            except Error as ex:
                print("Error de conexión: {0} ".format(ex))