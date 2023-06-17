import tkinter as tk
from tkinter import ttk
from Clases.Trabajador import Trabajador
from Clases.CargaFamiliar import CargaFamiliar
from Clases.ContactoEmergencia import ContactoEmergencia

class RegistroTrabajador(tk.Tk):
    
    def __init__(self):
        super().__init__()
        
        self.listaCargasFamiliares = []
        self.listaContactos = []

        self.title("Registro de Trabajador")
        self.geometry("600x500")

        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas = tk.Canvas(self, yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar.config(command=self.canvas.yview)

        self.container = ttk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.container, anchor=tk.NW)

        # Sección de Datos Personales
        self.frame_datos_personales = ttk.LabelFrame(self.container, text="Datos Personales", padding=10)
        self.frame_datos_personales.pack(pady=10)
        
        self.label_rut = tk.Label(self.frame_datos_personales, text="RUT:")
        self.entry_rut = tk.Entry(self.frame_datos_personales, width=20)
        self.label_dv = tk.Label(self.frame_datos_personales, text="-")
        self.entry_dv = tk.Entry(self.frame_datos_personales, width=5)
        self.label_nombre = tk.Label(self.frame_datos_personales, text="Nombre:")
        self.entry_nombre = tk.Entry(self.frame_datos_personales)
        self.label_apellido = tk.Label(self.frame_datos_personales, text="Apellido:")
        self.entry_apellido = tk.Entry(self.frame_datos_personales)
        self.label_sexo = tk.Label(self.frame_datos_personales, text="Sexo:")
        self.combo_sexo = ttk.Combobox(self.frame_datos_personales, values=["Masculino", "Femenino"], state="readonly")

        self.label_rut.grid(row=0, column=0, sticky=tk.E)
        self.entry_rut.grid(row=0, column=1, padx=5)
        self.label_dv.grid(row=0, column=2, sticky=tk.W)
        self.entry_dv.grid(row=0, column=3, padx=5)
        self.label_nombre.grid(row=1, column=0, sticky=tk.E)
        self.entry_nombre.grid(row=1, column=1)
        self.label_apellido.grid(row=2, column=0, sticky=tk.E)
        self.entry_apellido.grid(row=2, column=1)
        self.label_sexo.grid(row=3, column=0, sticky=tk.E)
        self.combo_sexo.grid(row=3, column=1)

        # seccion de Datos Laborales
        self.frame_datos_laborales = ttk.LabelFrame(self.container, text="Datos Laborales", padding=10)
        self.frame_datos_laborales.pack(pady=10)
        
        self.label_area = tk.Label(self.frame_datos_laborales, text="Área/Departamento:")
        self.combo_area = ttk.Combobox(self.frame_datos_laborales, values=[
            "Departamento de Operaciones",
            "Departamento de Servicio al Cliente",
            "Departamento de Ventas y Marketing",
            "Departamento de Recursos Humanos",
            "Departamento Financiero y Contable",
            "Departamento de Tecnología de la Información",
            "Departamento de Calidad y Control de Procesos"
        ], state="readonly", width=40)
        
        self.label_cargo = tk.Label(self.frame_datos_laborales, text="Cargo:")
        self.combo_cargo = ttk.Combobox(self.frame_datos_laborales, values=[], state="readonly", width=40)

        self.label_fecha_ingreso = tk.Label(self.frame_datos_laborales, text="Fecha de Ingreso:")

        # Menús desplegables para día, mes y año
        self.frame_fecha_ingreso = ttk.LabelFrame(self.frame_datos_laborales, text="Fecha de Ingreso", padding=10)
        self.frame_fecha_ingreso.grid(row=2, column=0, columnspan=2, sticky="w")
        
        self.label_dia = tk.Label(self.frame_fecha_ingreso, text="Día:")
        self.combo_dia = ttk.Combobox(self.frame_fecha_ingreso, values=list(range(1, 32)), state="readonly", width=3)
        self.label_dia.grid(row=0, column=0, padx=(0, 5))
        self.combo_dia.grid(row=0, column=1)
        
        self.label_mes = tk.Label(self.frame_fecha_ingreso, text="Mes:")
        self.combo_mes = ttk.Combobox(self.frame_fecha_ingreso, values=list(range(1, 13)), state="readonly", width=3)
        self.label_mes.grid(row=0, column=2, padx=(10, 5))
        self.combo_mes.grid(row=0, column=3)
        
        self.label_anio = tk.Label(self.frame_fecha_ingreso, text="Año:")
        self.combo_anio = ttk.Combobox(self.frame_fecha_ingreso, values=list(range(1950, 2151)), state="readonly", width=4)
        self.label_anio.grid(row=0, column=4, padx=(10, 5))
        self.combo_anio.grid(row=0, column=5)
        
        self.label_area.grid(row=0, column=0, sticky=tk.E, pady=5)
        self.combo_area.grid(row=0, column=1, pady=5)
        self.label_cargo.grid(row=1, column=0, sticky=tk.E, pady=5)
        self.combo_cargo.grid(row=1, column=1, pady=5)
        

        # Seccion Cargas Familiares
        self.frame_cargas_familiares = ttk.LabelFrame(self.container, text="Cargas Familiares", padding=10)
        self.frame_cargas_familiares.pack(pady=10)

        self.tree_cargas_familiares = ttk.Treeview(self.frame_cargas_familiares, show="headings")
        self.tree_cargas_familiares["columns"] = ("rut", "nombre", "sexo", "parentesco")

        self.tree_cargas_familiares.heading("rut", text="RUT")
        self.tree_cargas_familiares.heading("nombre", text="Nombre")
        self.tree_cargas_familiares.heading("sexo", text="Sexo")
        self.tree_cargas_familiares.heading("parentesco", text="Parentesco")

        self.tree_cargas_familiares.column("rut", width=100)
        self.tree_cargas_familiares.column("nombre", width=150)
        self.tree_cargas_familiares.column("sexo", width=100)
        self.tree_cargas_familiares.column("parentesco", width=150)

        self.tree_cargas_familiares.pack(pady=10)
        
        self.agregar_carga = tk.Button(self.frame_cargas_familiares, text="Agregar", command=self.agregar_carga_familiar)
        self.agregar_carga.pack(side=tk.RIGHT, padx=10, pady=10)
        
        # Seccion contactos
        self.frame_contactos_emergencia = ttk.LabelFrame(self.container, text="Contactos de Emergencia", padding=10)
        self.frame_contactos_emergencia.pack(pady=10)

        self.tree_contactos_emergencia = ttk.Treeview(self.frame_contactos_emergencia, show="headings")
        self.tree_contactos_emergencia["columns"] = ("nombre", "relacion", "telefono")

        self.tree_contactos_emergencia.heading("nombre", text="Nombre")
        self.tree_contactos_emergencia.heading("relacion", text="Relación")
        self.tree_contactos_emergencia.heading("telefono", text="Teléfono")

        self.tree_contactos_emergencia.column("nombre", width=150)
        self.tree_contactos_emergencia.column("relacion", width=150)
        self.tree_contactos_emergencia.column("telefono", width=100)

        self.tree_contactos_emergencia.pack(pady=10)

        self.agregar_carga = tk.Button(self.frame_contactos_emergencia, text="Agregar", command=self.agregar_contacto_emergencia)
        self.agregar_carga.pack(side=tk.RIGHT, padx=10, pady=10)
        
        self.container.bind("<Configure>", self.on_frame_configure)

        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)

        # boton de registro y cancelar
        self.button_registrar = tk.Button(self.container, text="Registrar", command=self.registrar_trabajador)
        self.button_registrar.pack()

        self.combo_sexo.current(0)  # seleccionar el primer valor por defecto
        self.combo_area.bind("<<ComboboxSelected>>", self.actualizar_cargos) # actualiza seleccion

        # datos de ejmplo
        # self.tree_cargas_familiares.insert("", "end", values=("123456789", "Juan Pérez", "Masculino", "Hijo"))
        # self.tree_contactos_emergencia.insert("", "end", values=("María López", "Amigo", "987654321"))

        self.actualizar_lista_cargas_familiares()

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def actualizar_cargos(self, event):
        area_seleccionada = self.combo_area.get()
        cargos = []

        if area_seleccionada == "Departamento de Operaciones":
            cargos = [
                "Gerente de Operaciones",
                "Supervisor de Distribución",
                "Supervisor de Entrega",
                "Personal de Clasificación y Distribución",
                "Personal de Entrega"
            ]
        elif area_seleccionada == "Departamento de Servicio al Cliente":
            cargos = [
                "Gerente de Atención al Cliente",
                "Representante de Servicio al Cliente",
                "Especialista en Seguimiento de Envíos",
                "Coordinador de Reclamaciones"
            ]
        elif area_seleccionada == "Departamento de Ventas y Marketing":
            cargos = [
                "Gerente de Ventas y Marketing",
                "Ejecutivo de Ventas",
                "Especialista en Marketing Digital",
                "Coordinador de Alianzas Comerciales"
            ]
        elif area_seleccionada == "Departamento de Recursos Humanos":
            cargos = [
                "Gerente de Recursos Humanos",
                "Contador",
                "Analista Financiero",
                "Especialista en Cuentas por Pagar",
                "Especialista en Cuentas por Cobrar"
            ]
        elif area_seleccionada == "Departamento Financiero y Contable":
            cargos = [
                "Gerente Financiero",
                "Especialista en Reclutamiento y Selección",
                "Especialista en Capacitación y Desarrollo",
                "Coordinador de Nómina y Beneficios",
                "Especialista en Relaciones Laborales"
            ]
        elif area_seleccionada == "Departamento de Tecnología de la Información":
            cargos = [
                "Gerente de Tecnología de la Información",
                "Administrador de Sistemas",
                "Desarrollador de Software",
                "Especialista en Seguridad Informática",
                "Técnico de Soporte Técnico"
            ]
        elif area_seleccionada == "Departamento de Calidad y Control de Procesos":
            cargos = [
                "Gerente de Logística y Almacén",
                "Coordinador de Inventarios",
                "Planificador de Rutas",
                "Especialista en Cadena de Suministro",
                "Almacenista"
            ]

        self.combo_cargo.config(values=cargos)
        self.combo_cargo.current(0)

    def agregar_carga_familiar(self):
        ventana_carga_familiar = tk.Toplevel(self)
        ventana_carga_familiar.title("Agregar Carga Familiar")

        # Etiqueta y entrada para el RUT
        label_rut = tk.Label(ventana_carga_familiar, text="RUT:")
        entry_rut = tk.Entry(ventana_carga_familiar, width=20)
        label_rut.grid(row=0, column=0, padx=5, pady=5)
        entry_rut.grid(row=0, column=1, padx=5, pady=5)

        # Etiqueta y entrada para el dígito verificador
        label_dv = tk.Label(ventana_carga_familiar, text="Dígito Verificador:")
        entry_dv = tk.Entry(ventana_carga_familiar, width=5)
        label_dv.grid(row=1, column=0, padx=5, pady=5)
        entry_dv.grid(row=1, column=1, padx=5, pady=5)

        # Etiqueta y entrada para el nombre
        label_nombre = tk.Label(ventana_carga_familiar, text="Nombre:")
        entry_nombre = tk.Entry(ventana_carga_familiar)
        label_nombre.grid(row=2, column=0, padx=5, pady=5)
        entry_nombre.grid(row=2, column=1, padx=5, pady=5)

        label_apellido = tk.Label(ventana_carga_familiar, text="Apellido:")
        entry_apellido = tk.Entry(ventana_carga_familiar)
        label_apellido.grid(row=3, column=0, padx=5, pady=5)
        entry_apellido.grid(row=3, column=1, padx=5, pady=5)
    
        # Menú desplegable para el sexo
        label_sexo = tk.Label(ventana_carga_familiar, text="Sexo:")
        combo_sexo = ttk.Combobox(ventana_carga_familiar, values=["Masculino", "Femenino"], state="readonly")
        label_sexo.grid(row=4, column=0, padx=5, pady=5)
        combo_sexo.grid(row=4, column=1, padx=5, pady=5)

        # Menú desplegable para el parentesco
        label_parentesco = tk.Label(ventana_carga_familiar, text="Parentesco:")
        parentescos = ["Hijo/a", "Cónyuge", "Padre", "Madre", "Hermano/a"]
        combo_parentesco = ttk.Combobox(ventana_carga_familiar, values=parentescos, state="readonly")
        label_parentesco.grid(row=5, column=0, padx=5, pady=5)
        combo_parentesco.grid(row=5, column=1, padx=5, pady=5)

        def guardar_carga_familiar():
            rut = entry_rut.get()
            dv = entry_dv.get()
            nombre = entry_nombre.get()
            apellido = entry_apellido.get()
            sexo = combo_sexo.get()
            parentesco = combo_parentesco.get()

            carga_familiar = CargaFamiliar(rut, dv, nombre, apellido, sexo, parentesco)
            ventana_carga_familiar.destroy()
            # Aquí puedes hacer algo con la carga familiar, como almacenarla en una lista o enviarla a una base de datos
            self.listaCargasFamiliares.append(carga_familiar)
            self.actualizar_lista_cargas_familiares()

        # Botón para guardar la carga familiar
        button_guardar = tk.Button(ventana_carga_familiar, text="Guardar", command=guardar_carga_familiar)
        button_guardar.grid(row=6, column=0, columnspan=2, padx=5, pady=10)

    def agregar_contacto_emergencia(self):
        print("agregar_contacto_emergencia")

    def actualizar_lista_cargas_familiares(self):
        self.tree_cargas_familiares.delete(*self.tree_cargas_familiares.get_children())
        for carga_familiar in self.listaCargasFamiliares:
            self.tree_cargas_familiares.insert("", "end", values=(carga_familiar.rut + "-" + carga_familiar.rut_dv, carga_familiar.nombre + " " + carga_familiar.apellido, carga_familiar.sexo, carga_familiar.parentesco))

    def registrar_trabajador(self):
        rut = self.entry_rut.get()
        dv = self.entry_dv.get()
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        sexo = self.combo_sexo.get()
        area = self.combo_area.get()
        cargo = self.combo_cargo.get()
        fecha_ingreso = self.entry_fecha_ingreso.get()

        # Validacion y registro a bd
        


        # exito
        mensaje = f"Trabajador registrado:\nRUT: {rut}-{dv}\nNombre: {nombre} {apellido}\nSexo: {sexo}\nÁrea/Departamento: {area}\nCargo: {cargo}\nFecha de Ingreso: {fecha_ingreso}"
        tk.messagebox.showinfo("Registro Exitoso", mensaje)
        self.destroy()

if __name__ == "__main__":
    app = RegistroTrabajador()
    app.mainloop()
