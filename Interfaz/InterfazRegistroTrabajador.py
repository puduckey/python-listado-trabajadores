import tkinter as tk
from tkinter import ttk

class RegistroTrabajador(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Registro de Trabajador")
        self.geometry("500x500")

        # Sección de Datos Personales
        self.frame_datos_personales = ttk.LabelFrame(self, text="Datos Personales", padding=10)
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

        # posicionamiento de los componentes en la ventana
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
        self.frame_datos_laborales = ttk.LabelFrame(self, text="Datos Laborales", padding=10)
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
        self.entry_fecha_ingreso = tk.Entry(self.frame_datos_laborales)
        
        self.label_area.grid(row=0, column=0, sticky=tk.E)
        self.combo_area.grid(row=0, column=1, padx=5)
        self.label_cargo.grid(row=1, column=0, sticky=tk.E)
        self.combo_cargo.grid(row=1, column=1, padx=5)
        self.label_fecha_ingreso.grid(row=2, column=0, sticky=tk.E)
        self.entry_fecha_ingreso.grid(row=2, column=1)

        # boton de registro y cancelar
        self.button_registrar = tk.Button(self, text="Registrar", command=self.registrar_trabajador)
        self.button_registrar.pack()

        self.combo_sexo.current(0)  # seleccionar el primer valor por defecto
        self.combo_area.bind("<<ComboboxSelected>>", self.actualizar_cargos) # actualiza seleccion

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
