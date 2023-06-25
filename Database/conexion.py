import mysql.connector
from mysql.connector import Error
from Clases.Trabajador import Trabajador
from Clases.CargaFamiliar import CargaFamiliar
from Clases.ContactoEmergencia import ContactoEmergencia

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
                query = """INSERT INTO trabajador (rut, rut_dv, nombre, apellido, sexo, direccion) VALUES ({0},'{1}','{2}','{3}',{4},'{5}')
                ON DUPLICATE KEY UPDATE rut_dv = '{1}', nombre = '{2}', apellido = '{3}', sexo = {4}, direccion = '{5}'
                """
                cursor.execute(query.format(trabajador.rut, trabajador.rut_dv, trabajador.nombre, trabajador.apellido, id_sexo, trabajador.direccion))

                # INSERTAR TELEFONOS
                print(trabajador.telefonos)
                for telefono in trabajador.telefonos:
                    # verificar si el telefono existe
                    resultado = None
                    query = "SELECT id FROM telefono where numero = '{0}' AND trabajador_rut = {1}"
                    cursor.execute(query.format(telefono, trabajador.rut))
                    resultado = cursor.fetchone()
                    if not resultado:
                        query = "INSERT INTO telefono (numero, trabajador_rut) VALUES('{0}',{1})"
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
                query = """INSERT INTO datoslaborales (trabajador_rut, cargo_id, area_departamento, fecha_ingreso) VALUES({0},{1},{2},'{3}')
                ON DUPLICATE KEY UPDATE cargo_id = {1}, area_departamento = {2}, fecha_ingreso = '{3}'"""
                cursor.execute(query.format(trabajador.rut, id_cargo, id_departamento, fecha))
                
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
                t.direccion, car.nombre as 'cargo', 
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
                    rut, rut_dv, nombre, apellido, sexo, direccion, cargo, area_departamento, fecha_ingreso = resultado

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
                        telefonos=listaTelefonos,
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
                
                # COMPROBAR SI EL FAMILIAR EXISTE
                resultado = None
                query = "SELECT id FROM cargafamiliar WHERE id = '{0}'"
                cursor.execute(query.format(familiar.id))
                resultado = cursor.fetchone()
                
                if resultado:
                    # ACTUALIZAR FAMILIAR
                    query = """
                    UPDATE cargafamiliar SET rut_dv = '{1}', nombre = '{2}', apellido = '{3}', sexo = {4}, parentesco_id = {5}, trabajador_rut = {6}
                    WHERE id = {7}
                    """
                    cursor.execute(query.format(familiar.rut, familiar.rut_dv, familiar.nombre,
                                            familiar.apellido, id_sexo, id_parentesco, trabajador_rut, familiar.id))
                else:
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
    
    def BorrarCargaFamiliar(self, familiar_id):
        if self.conexion.is_connected():    
            try:
                cursor = self.conexion.cursor(buffered=True)
                query = """DELETE FROM cargafamiliar WHERE id = {0}"""
                cursor.execute(query.format(familiar_id))
                self.conexion.commit()
                
            except Error as ex:
                print("Error de conexión: {0} ".format(ex))

    def ObtenerCargasFamiliares(self, trabajador_rut):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor(buffered=True)
                query = """SELECT cargafamiliar.id, cargafamiliar.rut, cargafamiliar.rut_dv, 
                cargafamiliar.nombre, cargafamiliar.apellido, sexo.nombre as 'sexo', 
                parentesco.nombre as 'parentesco'
                FROM cargafamiliar
                LEFT JOIN sexo ON cargafamiliar.sexo = sexo.id
                LEFT JOIN parentesco ON cargafamiliar.parentesco_id = parentesco.id
                WHERE trabajador_rut = {0}
                """
                cursor.execute(query.format(trabajador_rut))
                resultados = cursor.fetchall()
                
                listaFamiliares = []
                
                for resultado in resultados:
                    familiar = CargaFamiliar(int(resultado[0]), int(resultado[1]), resultado[2], resultado[3],
                                             resultado[4], resultado[5], resultado[6])
                    listaFamiliares.append(familiar)
                    
                for familiar in listaFamiliares:
                    print("ID:", str(familiar.id))
                    print("RUT:", str(familiar.rut))
                    print("DV:", familiar.rut_dv)
                    print("Nombre:", familiar.nombre)
                    print("Apellido:", familiar.apellido)
                    print("Sexo:", familiar.sexo)
                    print("Parentesco:", familiar.parentesco)
                    print("----------------------")


                return listaFamiliares
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
                
                # COMPROBAR SI EL CONTACTO YA EXISTE
                query = "SELECT id FROM contactosemergencia WHERE id = '{0}'"
                cursor.execute(query.format(contacto.id))
                resultado = cursor.fetchone()
                
                if resultado:
                    # ACTUALIZAR CONTACTO
                    query = """
                    UPDATE contactosemergencia SET nombre = '{0}', apellido = '{1}', relacion = {2}, telefono = '{3}', trabajador_rut = {4}
                    """
                    cursor.execute(query.format(contacto.nombre, contacto.apellido, id_parentesco, contacto.telefono, trabajador_rut))
                else:
                    # REGISTRAR CONTACTO
                    query = """
                    INSERT INTO contactosemergencia(nombre, apellido, relacion, telefono, trabajador_rut)
                    VALUES('{0}','{1}',{2},'{3}',{4})
                    """
                    cursor.execute(query.format(contacto.nombre, contacto.apellido, id_parentesco, contacto.telefono, trabajador_rut))
                self.conexion.commit()
                
            except Error as ex:
                print("Error de conexión: {0} ".format(ex))
    
    def BorrarContactoEmergencia(self, contacto_id):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor(buffered=True)
                query = """DELETE FROM contactosemergencia WHERE id = {0}"""
                cursor.execute(query.format(contacto_id))
                self.conexion.commit()
                
            except Error as ex:
                print("Error de conexión: {0} ".format(ex))
    
    def ObtenerContactosEmergencia(self, trabajador_rut):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor(buffered=True)
                query = """SELECT ce.id, ce.nombre, ce.apellido, parentesco.nombre as 'relacion', ce.telefono
                FROM contactosemergencia AS ce
                LEFT JOIN parentesco ON ce.relacion = parentesco.id
                WHERE trabajador_rut = {0}
                """
                cursor.execute(query.format(trabajador_rut))
                resultados = cursor.fetchall()
                
                listaContactos = []
                
                for resultado in resultados:
                    contactos = ContactoEmergencia(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4])
                    listaContactos.append(contactos)
                return listaContactos
            except Error as ex:
                print("Error de conexión: {0} ".format(ex))
                
    def BorrarTelefono(self, numero, trabajador_rut):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor(buffered=True)
                query = "DELETE FROM telefono WHERE numero = {0} AND trabajador_rut = {1}"
                cursor.execute(query.format(numero, trabajador_rut))
                self.conexion.commit()
            except Error as ex:
                print("Error de conexión: {0} ".format(ex))