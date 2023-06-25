import sys
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Interfaz.registroTrabajador import RegistroTrabajador
from Database.conexion import DAO

class InterfazListadoTrabajadores(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Listado de Trabajadores")
        self.geometry("800x600")

        # Tabla
        self.tabla = ttk.Treeview(self)
        self.tabla["columns"] = ("rut", "nombre", "sexo","area", "cargo")

        # Columnas
        self.tabla.column("#0", width=0, stretch=tk.NO)  # Columna oculta
        self.tabla.column("rut", anchor=tk.W, width=100)
        self.tabla.column("nombre", anchor=tk.W, width=200)
        self.tabla.column("sexo", anchor=tk.W, width=100)
        self.tabla.column("area", anchor=tk.W, width=200)
        self.tabla.column("cargo", anchor=tk.W, width=200)

        # Encabezados de columna
        self.tabla.heading("rut", text="RUT")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("sexo", text="Sexo")
        self.tabla.heading("area", text="Area/Departamento")
        self.tabla.heading("cargo", text="Cargo")

        self.label = tk.Label(self, text="Listado de trabajadores")
        self.label.pack()

        # Lectura de datos
        # Datos de ejemplo
        self.obtener_lista_trabajadores()

        # Agregar tabla a la interfaz
        self.tabla.pack(expand=True, fill=tk.BOTH)

        # Botón para registrar nuevos trabajadores
        self.boton_registrar = tk.Button(self, text="Registrar Trabajador", command=self.registrar_trabajador)
        self.boton_registrar.pack(side=tk.LEFT, padx=10, pady=10)

        # Botón para modificar trabajador seleccionado
        self.boton_modificar = tk.Button(self, text="Modificar seleccionado", command=self.modificar_trabajador)
        self.boton_modificar.pack(side=tk.LEFT, padx=10, pady=10)

        # Botón para ver el perfil del trabajador
        self.boton_perfil = tk.Button(self, text="Ver mi perfil", command=self.ver_perfil)
        self.boton_perfil.pack(side=tk.LEFT, padx=10, pady=10)

        # Botón para refrescar lista de trabajadores
        self.boton_refrescar = tk.Button(self, text="Refrescar lista", command=self.refrescar_lista_trabajadores)
        self.boton_refrescar.pack(side=tk.LEFT, padx=10, pady=10)

        # Botón para cerrar sesión y volver al inicio de sesión
        self.boton_cerrar_sesion = tk.Button(self, text="Cerrar Sesión", command=self.cerrar_sesion)
        self.boton_cerrar_sesion.pack(side=tk.RIGHT, padx=10, pady=10)


    def obtener_lista_trabajadores(self):
        db = DAO()
        lista = db.ObtenerTrabajadores()
        
        for trabajador in lista:
            self.agregar_trabajador(str(trabajador.rut) + "-" + trabajador.rut_dv, trabajador.nombre + " " + trabajador.apellido, trabajador.sexo, trabajador.departamento, trabajador.cargo)
    
    def agregar_trabajador(self, rut, nombre, sexo, areadepartamento,  cargo):
        self.tabla.insert("", tk.END, text="", values=(rut, nombre, sexo, areadepartamento, cargo))

    def registrar_trabajador(self):
        registro_trabajador = RegistroTrabajador()
        registro_trabajador.mainloop()

    def modificar_trabajador(self):
        seleccionado = self.tabla.selection()
        if seleccionado:
            valores = self.tabla.item(seleccionado)["values"]
            rut = valores[0].replace("-", "")[:-1]
            db = DAO()
            trabajador = db.ObtenerTrabajador(rut)
            listaFamiliares = db.ObtenerCargasFamiliares(rut)
            listaContactos = db.ObtenerContactosEmergencia(rut)
            
            registro_trabajador = RegistroTrabajador()
            registro_trabajador.mostrar_datos_trabajador(trabajador, listaFamiliares, listaContactos)
            registro_trabajador.mainloop()
        else:
            messagebox.showwarning("Seleccionar Trabajador", "Por favor, seleccione un trabajador de la lista.")

    def ver_perfil(self):
        messagebox.showinfo("Ver mi perfil", "Funcionalidad para ver el perfil del usuario")

    def refrescar_lista_trabajadores(self):
        self.tabla.delete(*self.tabla.get_children())
        self.obtener_lista_trabajadores()
    
    def cerrar_sesion(self):
        messagebox.showinfo("Cerrar Sesión", "Sesión cerrada correctamente")
        self.destroy()
        sys.exit()

if __name__ == "__main__":
    app = InterfazListadoTrabajadores()
    app.mainloop()