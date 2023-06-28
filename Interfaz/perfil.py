import tkinter as tk
import re
import datetime
from tkinter import ttk
from tkinter import messagebox
from Clases.Trabajador import Trabajador
from Clases.CargaFamiliar import CargaFamiliar
from Clases.ContactoEmergencia import ContactoEmergencia
from Database.conexion import DAO

class PerfilUsuario(tk.Tk):
    def __init__(self, usuario, trabajador, cargas_familiares, contactos_emergencia):
        super().__init__()

        # Crear ventana principal
        ventana = tk.Tk()
        ventana.title("Perfil de Usuario")

        # Sección de cuenta
        seccion_cuenta = tk.LabelFrame(ventana, text="Cuenta de usuario")
        seccion_cuenta.pack(padx=10, pady=10)

        tk.Label(seccion_cuenta, text="Nombre de usuario:").grid(row=0, column=0, sticky=tk.W)
        tk.Label(seccion_cuenta, text="Identificación:").grid(row=1, column=0, sticky=tk.W)

        entry_username = tk.Entry(seccion_cuenta)
        entry_username.insert(0, usuario.username)
        entry_username.configure(state="readonly")
        entry_username.grid(row=0, column=1)

        entry_identificacion = tk.Entry(seccion_cuenta)
        entry_identificacion.insert(0, usuario.identificacion)
        entry_identificacion.configure(state="readonly")
        entry_identificacion.grid(row=1, column=1)

        # Sección de datos personales
        seccion_datos_personales = tk.LabelFrame(ventana, text="Datos personales")
        seccion_datos_personales.pack(padx=20, pady=10)

        tk.Label(seccion_datos_personales, text="RUT:").grid(row=0, column=0, sticky=tk.W)
        tk.Label(seccion_datos_personales, text="Nombre:").grid(row=1, column=0, sticky=tk.W)
        tk.Label(seccion_datos_personales, text="Apellido:").grid(row=2, column=0, sticky=tk.W)
        tk.Label(seccion_datos_personales, text="Sexo:").grid(row=3, column=0, sticky=tk.W)
        tk.Label(seccion_datos_personales, text="Dirección:").grid(row=4, column=0, sticky=tk.W)
        tk.Label(seccion_datos_personales, text="Teléfonos:").grid(row=5, column=0, sticky=tk.W)

        entry_rut = tk.Entry(seccion_datos_personales)
        entry_rut.insert(0, str(trabajador.rut) + "-" + trabajador.rut_dv)
        entry_rut.configure(state="readonly")
        entry_rut.grid(row=0, column=1)

        entry_nombre = tk.Entry(seccion_datos_personales)
        entry_nombre.insert(0, trabajador.nombre)
        entry_nombre.configure(state="readonly")
        entry_nombre.grid(row=1, column=1)

        entry_apellido = tk.Entry(seccion_datos_personales)
        entry_apellido.insert(0, trabajador.apellido)
        entry_apellido.configure(state="readonly")
        entry_apellido.grid(row=2, column=1)

        entry_sexo = tk.Entry(seccion_datos_personales)
        entry_sexo.insert(0, trabajador.sexo)
        entry_sexo.configure(state="readonly")
        entry_sexo.grid(row=3, column=1)

        entry_direccion = tk.Entry(seccion_datos_personales)
        entry_direccion.insert(0, trabajador.direccion)
        entry_direccion.configure(state="readonly")
        entry_direccion.grid(row=4, column=1)

        entry_telefonos = tk.Entry(seccion_datos_personales)
        entry_telefonos.insert(0, ", ".join(trabajador.telefonos))
        entry_telefonos.configure(state="readonly")
        entry_telefonos.grid(row=5, column=1)

        # Sección de datos laborales
        seccion_datos_laborales = tk.LabelFrame(ventana, text="Datos laborales")
        seccion_datos_laborales.pack(padx=20, pady=10)

        tk.Label(seccion_datos_laborales, text="Departamento:").grid(row=0, column=0, sticky=tk.W)
        tk.Label(seccion_datos_laborales, text="Cargo:").grid(row=1, column=0, sticky=tk.W)
        tk.Label(seccion_datos_laborales, text="Fecha de ingreso:").grid(row=2, column=0, sticky=tk.W)

        entry_departamento = tk.Entry(seccion_datos_laborales)
        entry_departamento.insert(0, trabajador.departamento)
        entry_departamento.configure(state="readonly")
        entry_departamento.grid(row=0, column=1)

        entry_cargo = tk.Entry(seccion_datos_laborales)
        entry_cargo.insert(0, trabajador.cargo)
        entry_cargo.configure(state="readonly")
        entry_cargo.grid(row=1, column=1)

        entry_fecha_ingreso = tk.Entry(seccion_datos_laborales)
        entry_fecha_ingreso.insert(0, str(trabajador.fecha_dd) + "/" + str(trabajador.fecha_mm) + "/" + str(trabajador.fecha_aaaa))
        entry_fecha_ingreso.configure(state="readonly")
        entry_fecha_ingreso.grid(row=2, column=1)

        # Sección de cargas familiares
        seccion_cargas_familiares = tk.LabelFrame(ventana, text="Cargas familiares")
        seccion_cargas_familiares.pack(padx=10, pady=10)

        # Aquí debes agregar la lógica para mostrar el listado de cargas familiares
        for i, carga in enumerate(cargas_familiares):
            tk.Label(seccion_cargas_familiares, text="Carga {}: ".format(i+1)).grid(row=i, column=0, sticky=tk.W)
            tk.Label(seccion_cargas_familiares, text="RUT: {}".format(carga.rut)).grid(row=i, column=1, sticky=tk.W)
            tk.Label(seccion_cargas_familiares, text="Nombre completo: {}".format(carga.nombre + " " + carga.apellido)).grid(row=i, column=2, sticky=tk.W)
            tk.Label(seccion_cargas_familiares, text="Sexo: {}".format(carga.sexo)).grid(row=i, column=3, sticky=tk.W)
            tk.Label(seccion_cargas_familiares, text="Parentesco: {}".format(carga.parentesco)).grid(row=i, column=4, sticky=tk.W)

        # Sección de contactos de emergencia
        seccion_contactos_emergencia = tk.LabelFrame(ventana, text="Contactos de emergencia")
        seccion_contactos_emergencia.pack(padx=10, pady=10)

        # Aquí debes agregar la lógica para mostrar el listado de contactos de emergencia
        for i, contacto in enumerate(contactos_emergencia):
            tk.Label(seccion_contactos_emergencia, text="Contacto {}: ".format(i+1)).grid(row=i, column=0, sticky=tk.W)
            tk.Label(seccion_contactos_emergencia, text="Nombre completo: {}".format(contacto.nombre + " " + contacto.apellido)).grid(row=i, column=1, sticky=tk.W)
            tk.Label(seccion_contactos_emergencia, text="Relación: {}".format(contacto.relacion)).grid(row=i, column=2, sticky=tk.W)
            tk.Label(seccion_contactos_emergencia, text="Teléfono: {}".format(contacto.telefono)).grid(row=i, column=3, sticky=tk.W)

        # Botones
        btn_actualizar = tk.Button(ventana, text="Actualizar información", command=self.actualizar_informacion)
        btn_actualizar.pack(pady=10)

        btn_cambiar_contrasenia = tk.Button(ventana, text="Cambiar contraseña", command=self.cambiar_contrasenia)
        btn_cambiar_contrasenia.pack(pady=10)
    
    def actualizar_informacion(self):
        print("actualizar_informacion")

    def cambiar_contrasenia(self):
        print("cambiar_contrasenia")
            
if __name__ == "__main__":
    app = PerfilUsuario()
    app.mainloop()
