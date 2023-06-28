import sys
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Interfaz.registroTrabajador import RegistroTrabajador
from Interfaz.perfil import PerfilUsuario
from Database.conexion import DAO

class InterfazListadoTrabajadores(tk.Tk):
    def __init__(self, usuario):
        super().__init__()
        
        self.usuario = usuario
        
        if usuario.identificacion != "Trabajador":
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
            
            # Botón para refrescar lista de trabajadores
            self.boton_refrescar = tk.Button(self, text="Refrescar lista", command=self.refrescar_lista_trabajadores)
            self.boton_refrescar.pack(side=tk.LEFT, padx=10, pady=10)
            
            if usuario.identificacion == "Administrador" or usuario.identificacion == "Jefe RRHH":
                # Botón para filtrar lista de trabajadores
                self.boton_filtrar = tk.Button(self, text="Filtrar lista", command=self.ventana_filtrar)
                self.boton_filtrar.pack(side=tk.LEFT, padx=10, pady=10)

        # Botón para ver el perfil del trabajador
        self.boton_perfil = tk.Button(self, text="Ver mi perfil", command=self.ver_perfil)
        self.boton_perfil.pack(side=tk.LEFT, padx=10, pady=10)
    
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
        db = DAO()
        trabajador = db.ObtenerTrabajadorPorUsername(self.usuario.username)
        familiares = db.ObtenerCargasFamiliares(trabajador.rut)
        contactos = db.ObtenerContactosEmergencia(trabajador.rut)
        
        perfil_usuario = PerfilUsuario(self.usuario, trabajador, familiares, contactos)
        perfil_usuario.mainloop()

    def refrescar_lista_trabajadores(self):
        self.tabla.delete(*self.tabla.get_children())
        self.obtener_lista_trabajadores()
    
    def ventana_filtrar(self):
        ventana_filtros = tk.Toplevel(self)
        ventana_filtros.title("Filtrar lista")
        ventana_filtros.geometry("250x250")
        ventana_filtros.transient(self)
        ventana_filtros.grab_set()

        # Variables de control para los menús desplegables
        sexo_var = tk.StringVar()
        cargo_var = tk.StringVar()
        area_var = tk.StringVar()

        def confirmar_filtro():
            # Obtener los valores seleccionados de los menús desplegables
            sexo = sexo_var.get()
            cargo = cargo_var.get()
            area = area_var.get()

            # Cerrar la ventana emergente
            ventana_filtros.destroy()

            # Llamar a la función para filtrar la lista de trabajadores
            self.filtrar_lista_trabajadores(sexo, cargo, area)


        label_sexo = tk.Label(ventana_filtros, text="Sexo:")
        label_cargo = tk.Label(ventana_filtros, text="Cargo:")
        label_area = tk.Label(ventana_filtros, text="Área:")
        # Crear menús desplegables
        sexo_menu = ttk.Combobox(ventana_filtros, textvariable=sexo_var, values=["Masculino", "Femenino"], width=20)
        cargo_menu = ttk.Combobox(ventana_filtros, textvariable=cargo_var, values=[
            "Gerente de Operaciones",
            "Supervisor de Distribución",
            "Supervisor de Entrega",
            "Personal de Clasificación y Distribución",
            "Personal de Entrega",
            "Gerente de Atención al Cliente",
            "Representante de Servicio al Cliente",
            "Especialista en Seguimiento de Envíos",
            "Coordinador de Reclamaciones",
            "Gerente de Ventas y Marketing",
            "Ejecutivo de Ventas",
            "Especialista en Marketing Digital",
            "Coordinador de Alianzas Comerciales",
            "Gerente de Recursos Humanos",
            "Contador",
            "Analista Financiero",
            "Especialista en Cuentas por Pagar",
            "Especialista en Cuentas por Cobrar",
            "Gerente Financiero",
            "Especialista en Reclutamiento y Selección",
            "Especialista en Capacitación y Desarrollo",
            "Coordinador de Nómina y Beneficios",
            "Especialista en Relaciones Laborales",
            "Gerente de Tecnología de la Información",
            "Administrador de Sistemas",
            "Desarrollador de Software",
            "Especialista en Seguridad Informática",
            "Técnico de Soporte Técnico",
            "Gerente de Logística y Almacén",
            "Coordinador de Inventarios",
            "Planificador de Rutas",
            "Especialista en Cadena de Suministro",
            "Almacenista"
        ], width=40)
        area_menu = ttk.Combobox(ventana_filtros, textvariable=area_var, values=[
            "Departamento de Operaciones",
            "Departamento de Servicio al Cliente",
            "Departamento de Ventas y Marketing",
            "Departamento de Recursos Humanos",
            "Departamento Financiero y Contable",
            "Departamento de Tecnología de la Información",
            "Departamento de Calidad y Control de Procesos"
        ], width=40)
        # Crear botón "Aceptar"
        boton_aceptar = tk.Button(ventana_filtros, text="Aceptar", command=confirmar_filtro)

        # Posicionar los elementos en la ventana
        label_sexo.pack()
        sexo_menu.pack()
        label_cargo.pack()
        cargo_menu.pack()
        label_area.pack()
        area_menu.pack()
        boton_aceptar.pack()
    
    def filtrar_lista_trabajadores(self, sexo, cargo, area):
        self.tabla.delete(*self.tabla.get_children())
        
        if sexo == '':
            sexo = None        
        if cargo == '':
            cargo = None        
        if area == '':
            area = None
        
        db = DAO()
        lista = db.ObtenerTrabajadoresFiltrados(sexo, cargo, area)
        for trabajador in lista:
            self.agregar_trabajador(str(trabajador.rut) + "-" + trabajador.rut_dv, trabajador.nombre + " " + trabajador.apellido, trabajador.sexo, trabajador.departamento, trabajador.cargo)
    
    def cerrar_sesion(self):
        messagebox.showinfo("Cerrar Sesión", "Sesión cerrada correctamente")
        self.destroy()
        sys.exit()

if __name__ == "__main__":
    app = InterfazListadoTrabajadores()
    app.mainloop()