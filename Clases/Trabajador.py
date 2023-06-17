#rut nombre sexo cargo
class Trabajador:
    def __init__(self, id, rut, rut_dv, nombre, apellido, sexo, direccion, telefono, 
                 datoslabID, cargo, departamento, fecha_dd, fecha_mm, fecha_aaaa):
        self.id = id
        self.rut = rut
        self.rut_dv = rut_dv
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.direccion = direccion
        self.telefono = telefono
        self.datoslabID = datoslabID
        self.cargo = cargo
        self.departamento = departamento
        self.fecha_dd = fecha_dd
        self.fecha_mm = fecha_mm
        self.fecha_aaaa = fecha_aaaa