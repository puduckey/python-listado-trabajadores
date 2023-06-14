import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Interfaz.InterfazRegistroTrabajador import RegistroTrabajador

class InterfazListadoTrabajadores(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Listado de Trabajadores")
        self.geometry("800x600")

        # Tabla
        self.tabla = ttk.Treeview(self)
        self.tabla["columns"] = ("rut", "nombre", "sexo", "cargo")

        # Columnas
        self.tabla.column("#0", width=0, stretch=tk.NO)  # Columna oculta
        self.tabla.column("rut", anchor=tk.W, width=100)
        self.tabla.column("nombre", anchor=tk.W, width=200)
        self.tabla.column("sexo", anchor=tk.W, width=100)
        self.tabla.column("cargo", anchor=tk.W, width=200)

        # Encabezados de columna
        self.tabla.heading("rut", text="RUT")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("sexo", text="Sexo")
        self.tabla.heading("cargo", text="Cargo")

        self.label = tk.Label(self, text="Listado de trabajadores")
        self.label.pack()

        # Lectura de datos
        # Datos de ejemplo
        self.agregar_trabajador("12345678-9", "Juan Pérez", "Masculino", "Gerente")
        self.agregar_trabajador("98765432-1", "María Gómez", "Femenino", "Asistente")

        # Agregar tabla a la interfaz
        self.tabla.pack(expand=True, fill=tk.BOTH)

        # Botón para registrar nuevos trabajadores
        self.boton_registrar = tk.Button(self, text="Registrar Trabajador", command=self.registrar_trabajador)
        self.boton_registrar.pack(side=tk.LEFT, padx=10, pady=10)

        # Botón para cerrar sesión y volver al inicio de sesión
        self.boton_cerrar_sesion = tk.Button(self, text="Cerrar Sesión", command=self.cerrar_sesion)
        self.boton_cerrar_sesion.pack(side=tk.RIGHT, padx=10, pady=10)

    def agregar_trabajador(self, rut, nombre, sexo, cargo):
        self.tabla.insert("", tk.END, text="", values=(rut, nombre, sexo, cargo))

    def registrar_trabajador(self):
        # messagebox.showinfo("Registro de Trabajador", "Funcionalidad de registro de trabajador")
        registro_trabajador = RegistroTrabajador()
        registro_trabajador.mainloop()

    def cerrar_sesion(self):
        messagebox.showinfo("Cerrar Sesión", "Sesión cerrada correctamente")
        self.destroy()

if __name__ == "__main__":
    app = InterfazListadoTrabajadores()
    app.mainloop()