## Requisitos previos:
- Sistema operativo: Windows, macOS o Linux.
- Python 3.4 instalado en tu sistema.
- Acceso a una base de datos MySQL, ya sea local o remota.
## Pasos de instalación:
1. Descarga el código fuente del programa y guárdalo en una ubicación conveniente en tu sistema.
1. Instala las dependencias
   1. Abre una terminal en la ubicación del código fuente y ejecuta la siguiente línea de comando para instalar las dependencias necesarias:
```
pip install -r dependencias.txt
```
3. Crea e importa la base de datos
   1. Establece la conexión con el servidor en tu software de administración de base de datos de preferencia.
   1. Asegúrate de que el servidor de MySQL esté en funcionamiento y que tengas los permisos necesarios para crear una base de datos y tablas.
   1. Asegúrate de seleccionar la base de datos adecuada en el administrador de base de datos antes de ejecutar las consultas.
   1. Localiza el archivo database.sql proporcionado con el programa.
   1. Abre el archivo en un editor de texto, copia y pega el contenido en el editor de consultas de tu administrador de base de datos.
   1. Ejecuta las consultas SQL para crear las tablas e insertar los datos necesarios en la base de datos. Esto se puede hacer seleccionando todo el contenido del editor de consultas y haciendo clic en el botón "Ejecutar" o "Ejecutar consulta" en el administrador de base de datos.
   1. Verifica que las consultas se hayan ejecutado correctamente y que las tablas y los datos se hayan creado en la base de datos.
4. Configura la base de datos:
   1. Abre el archivo de configuración (config.py) con un editor de texto.
   1. Modifica los detalles de la conexión a la base de datos: host, puerto, nombre de usuario, contraseña y nombre de la base de datos.
   1. Guarda los cambios del archivo de configuración.
4. Ejecuta el programa:
   1. En la terminal o línea de comandos, navega hasta la ubicación del código.
   1. Ejecuta el siguiente comando para iniciar el programa:
    ```
    python main.py
    ```
6. Utiliza el programa
   - Una vez ejecutes el programa debería ver una ventana de inicio de sesión.
   - Consulta el manual de usuario para conocer todas las funcionalidades del sistema.
