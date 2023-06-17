import tkinter as tk
from tkinter import messagebox
from Interfaz.listadoTrabajadores import InterfazListadoTrabajadores

class Login(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("El Correo de Yury")
        self.geometry("400x300")

        self.label_usuario = tk.Label(self, text="Usuario:")
        self.entry_usuario = tk.Entry(self)
        self.label_password = tk.Label(self, text="Contraseña:")
        self.entry_password = tk.Entry(self, show="*")
        self.button_login = tk.Button(self, text="Iniciar sesión", command=self.login)

        self.label_usuario.pack()
        self.entry_usuario.pack()
        self.label_password.pack()
        self.entry_password.pack()
        self.button_login.pack()

    def login(self):
        usuario = self.entry_usuario.get()
        password = self.entry_password.get()

        # Aquí iría la lógica de autenticación y verificación de usuarios
        if usuario == "admin" and password == "123":
            messagebox.showinfo("Inicio de sesión", "¡Inicio de sesión exitoso!")
            # Aquí podrías abrir una nueva ventana o realizar otras acciones según el perfil del usuario
            self.destroy()  # Cierra la ventana de inicio de sesión
            listado_trabajadores = InterfazListadoTrabajadores()
            listado_trabajadores.mainloop()
        else:
            messagebox.showerror("Inicio de sesión", "¡Usuario o contraseña incorrectos!")

if __name__ == "__main__":
    app = Login()
    app.mainloop()