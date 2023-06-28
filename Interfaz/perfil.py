import tkinter as tk
from tkinter import messagebox
from Database.conexion import DAO
from Clases.Trabajador import Trabajador
from Clases.CargaFamiliar import CargaFamiliar
from Clases.ContactoEmergencia import ContactoEmergencia
from Interfaz.registroTrabajador import RegistroTrabajador

class PerfilUsuario(tk.Tk):
    def __init__(self, usuario, trabajador, cargas_familiares, contactos_emergencia):
        super().__init__()
        
        self.usuario = usuario
        self.trabajador = trabajador
        self.cargas_familiares = cargas_familiares
        self.contactos_emergencia = contactos_emergencia
         
        self.title("Perfil de Usuario")
        
        # Sección de cuenta
        seccion_cuenta = tk.LabelFrame(self, text="Cuenta de usuario", width=200)
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
        seccion_datos_personales = tk.LabelFrame(self, text="Datos personales")
        seccion_datos_personales.pack(padx=20, pady=10)
        
        tk.Label(seccion_datos_personales, text="RUT:").grid(row=0, column=0, sticky=tk.W)
        tk.Label(seccion_datos_personales, text="Nombre:").grid(row=1, column=0, sticky=tk.W)
        tk.Label(seccion_datos_personales, text="Apellido:").grid(row=2, column=0, sticky=tk.W)
        tk.Label(seccion_datos_personales, text="Sexo:").grid(row=3, column=0, sticky=tk.W)
        tk.Label(seccion_datos_personales, text="Dirección:").grid(row=4, column=0, sticky=tk.W)
        tk.Label(seccion_datos_personales, text="Teléfonos:").grid(row=5, column=0, sticky=tk.W)

        entry_rut = tk.Entry(seccion_datos_personales, width=60)
        entry_rut.insert(0, str(trabajador.rut) + "-" + trabajador.rut_dv)
        entry_rut.configure(state="readonly")
        entry_rut.grid(row=0, column=1)

        entry_nombre = tk.Entry(seccion_datos_personales, width=60)
        entry_nombre.insert(0, trabajador.nombre)
        entry_nombre.configure(state="readonly")
        entry_nombre.grid(row=1, column=1)

        entry_apellido = tk.Entry(seccion_datos_personales, width=60)
        entry_apellido.insert(0, trabajador.apellido)
        entry_apellido.configure(state="readonly")
        entry_apellido.grid(row=2, column=1)

        entry_sexo = tk.Entry(seccion_datos_personales, width=60)
        entry_sexo.insert(0, trabajador.sexo)
        entry_sexo.configure(state="readonly")
        entry_sexo.grid(row=3, column=1)

        entry_direccion = tk.Entry(seccion_datos_personales, width=60)
        entry_direccion.insert(0, trabajador.direccion)
        entry_direccion.configure(state="readonly")
        entry_direccion.grid(row=4, column=1)

        entry_telefonos = tk.Entry(seccion_datos_personales, width=60)
        entry_telefonos.insert(0, ", ".join(trabajador.telefonos))
        entry_telefonos.configure(state="readonly")
        entry_telefonos.grid(row=5, column=1)

        # Sección de datos laborales
        seccion_datos_laborales = tk.LabelFrame(self, text="Datos laborales")
        seccion_datos_laborales.pack(padx=20, pady=10)

        tk.Label(seccion_datos_laborales, text="Departamento:").grid(row=0, column=0, sticky=tk.W)
        tk.Label(seccion_datos_laborales, text="Cargo:").grid(row=1, column=0, sticky=tk.W)
        tk.Label(seccion_datos_laborales, text="Fecha de ingreso:").grid(row=2, column=0, sticky=tk.W)

        entry_departamento = tk.Entry(seccion_datos_laborales, width=60)
        entry_departamento.insert(0, trabajador.departamento)
        entry_departamento.configure(state="readonly")
        entry_departamento.grid(row=0, column=1)

        entry_cargo = tk.Entry(seccion_datos_laborales, width=60)
        entry_cargo.insert(0, trabajador.cargo)
        entry_cargo.configure(state="readonly")
        entry_cargo.grid(row=1, column=1)

        entry_fecha_ingreso = tk.Entry(seccion_datos_laborales, width=60)
        entry_fecha_ingreso.insert(0, str(trabajador.fecha_dd) + "/" + str(trabajador.fecha_mm) + "/" + str(trabajador.fecha_aaaa))
        entry_fecha_ingreso.configure(state="readonly")
        entry_fecha_ingreso.grid(row=2, column=1)

        # Sección de cargas familiares
        seccion_cargas_familiares = tk.LabelFrame(self, text="Cargas familiares")
        seccion_cargas_familiares.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Aquí debes agregar la lógica para mostrar el listado de cargas familiares
        for i, carga in enumerate(cargas_familiares):
            tk.Label(seccion_cargas_familiares, text="Carga {}: ".format(i+1)).grid(row=i, column=0, sticky=tk.W)
            tk.Label(seccion_cargas_familiares, text="RUT: {}".format(str(carga.rut) + "-" + carga.rut_dv)).grid(row=i, column=1, sticky=tk.W)
            tk.Label(seccion_cargas_familiares, text="Nombre completo: {}".format(carga.nombre + " " + carga.apellido)).grid(row=i, column=2, sticky=tk.W)
            tk.Label(seccion_cargas_familiares, text="Sexo: {}".format(carga.sexo)).grid(row=i, column=3, sticky=tk.W)
            tk.Label(seccion_cargas_familiares, text="Parentesco: {}".format(carga.parentesco)).grid(row=i, column=4, sticky=tk.W)

        # Sección de contactos de emergencia
        seccion_contactos_emergencia = tk.LabelFrame(self, text="Contactos de emergencia")
        seccion_contactos_emergencia.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Aquí debes agregar la lógica para mostrar el listado de contactos de emergencia
        for i, contacto in enumerate(contactos_emergencia):
            tk.Label(seccion_contactos_emergencia, text="Contacto {}: ".format(i+1)).grid(row=i, column=0, sticky=tk.W)
            tk.Label(seccion_contactos_emergencia, text="Nombre completo: {}".format(contacto.nombre + " " + contacto.apellido)).grid(row=i, column=1, sticky=tk.W)
            tk.Label(seccion_contactos_emergencia, text="Relación: {}".format(contacto.relacion)).grid(row=i, column=2, sticky=tk.W)
            tk.Label(seccion_contactos_emergencia, text="Teléfono: {}".format(contacto.telefono)).grid(row=i, column=3, sticky=tk.W)

        # Botones
        btn_actualizar = tk.Button(self, text="Actualizar información", command=self.actualizar_informacion)
        btn_actualizar.pack(pady=10)

        btn_cambiar_contrasenia = tk.Button(self, text="Cambiar contraseña", command=self.mostrar_ventana_cambio_contrasenia)
        btn_cambiar_contrasenia.pack(pady=10)
    
    def actualizar_informacion(self):
        registro_trabajador = RegistroTrabajador()
        registro_trabajador.mostrar_datos_trabajador(self.trabajador, self.cargas_familiares, self.contactos_emergencia)
        self.destroy()
        registro_trabajador.actualizacion_desde_perfil()
        registro_trabajador.mainloop()
        
    def mostrar_ventana_cambio_contrasenia(self):
        # Crear la ventana emergente
        ventana_cambio_contrasenia = tk.Toplevel(self)
        ventana_cambio_contrasenia.title("Cambio de Contraseña")
        ventana_cambio_contrasenia.geometry("400x300")

        # Función para guardar la nueva contraseña
        def guardar_contrasenia():
            contrasenia_actual = entry_contrasenia_actual.get()
            nueva_contrasenia = entry_nueva_contrasenia.get()
            confirmar_contrasenia = entry_confirmar_contrasenia.get()

            # Verificar que los campos no estén vacíos y que la nueva contraseña y la confirmación coincidan
            if contrasenia_actual and nueva_contrasenia and confirmar_contrasenia:
                if nueva_contrasenia == confirmar_contrasenia:
                    db = DAO()
                    if db.CambiarContrasenia(self.usuario.username, contrasenia_actual, nueva_contrasenia) == False:
                        messagebox.showinfo("Cambio de Contraseña", "¡La contraseña actual es incorrecta!", parent=self)
                    else:
                        messagebox.showinfo("Cambio de Contraseña", "¡Contraseña cambiada exitosamente!", parent=self)
                        ventana_cambio_contrasenia.destroy()
                else:
                    messagebox.showerror("Error", "La nueva contraseña y la confirmación no coinciden.", parent=self)
            else:
                messagebox.showerror("Error", "Por favor, completa todos los campos.", parent=self)

        # Etiquetas y campos de entrada en la ventana
        tk.Label(ventana_cambio_contrasenia, text="Contraseña Actual:").pack()
        entry_contrasenia_actual = tk.Entry(ventana_cambio_contrasenia, show="*")
        entry_contrasenia_actual.pack()

        tk.Label(ventana_cambio_contrasenia, text="Nueva Contraseña:").pack()
        entry_nueva_contrasenia = tk.Entry(ventana_cambio_contrasenia, show="*")
        entry_nueva_contrasenia.pack()

        tk.Label(ventana_cambio_contrasenia, text="Confirmar Contraseña:").pack()
        entry_confirmar_contrasenia = tk.Entry(ventana_cambio_contrasenia, show="*")
        entry_confirmar_contrasenia.pack()

        # Botón para guardar la contraseña
        btn_guardar = tk.Button(ventana_cambio_contrasenia, text="Guardar", command=guardar_contrasenia)
        btn_guardar.pack()
    
if __name__ == "__main__":
    app = PerfilUsuario()
    app.mainloop()