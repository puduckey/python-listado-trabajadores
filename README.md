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
## Manual de usuario:
### Inicio de sesión
1. Ejecuta el archivo ejecutable del programa.
2. Se abrirá una ventana de inicio de sesión
3. Ingrese las credenciales de su cuenta de usuario
   - Credenciales por defecto de administrador:
      1. Nombre de usuario: admin
      1. Contraseña: admin
      1. Es recomendable que cambie la contraseña por defecto de esta cuenta.
4. Haz clic en el botón “Iniciar sesión” para acceder al sistema.
### Menú principal
1. Después de iniciar sesión correctamente, se mostrará el menú principal con las opciones y funcionalidades disponibles según su perfil de usuario.
2. Las opciones y funcionalidades del menú incluyen:
   1. Listado de trabajadores
   1. Registrar un trabajador
   1. Modificar trabajador
   1. Refrescar lista
   1. Filtrar listado
   1. Ver mi perfil
### Listado de trabajadores
- Se muestra una tabla resumen con la información de todos los trabajadores de la empresa
registrados.
- La tabla incluye los campos: RUT, Nombre, Sexo, Área/Departamento, Cargo.
### Registrar un trabajador
- Al selecciona esta opción se abrirá un formulario para ingresar los datos de un nuevo trabajador.
- Se deben completar todos los campos requeridos en el formulario, incluyendo: Datos personales, Datos laborales, Contactos de emergencia, Cargas familiares.
- Al registrar un nuevo trabajador el sistema le asignará una cuenta de usuario al trabajador (el nombre de usuario es generado por el sistema y se les asignará una contraseña temporal por defecto: abc123)
- Los privilegios de usuario de los trabajadores que se registren en el sistema dependerán del cargo que se les asigne:
  - A quien se le asigne el cargo de Administrador de sistemas obtendrá privilegios de Administrador.
  - A quien se le asigne el cargo de Gerente de Recursos Humanos obtendrá privilegios de Jefe RR.HH.
  - A quien se le asigne un cargo perteneciente al departamento de Recursos Humanos obtendrá privilegios de Personal RR.HH.
  - A quien se le asigne el cargo no mencionado anteriormente obtendrá privilegios de Trabajador.
### Modificar trabajador
- Al seleccionar esta opción se abrirá el formulario de registro correspondiente al trabajador que este seleccionado en el listado.
- Todos sus datos son modificables a excepción de su RUT.
- El trabajador puede ser eliminado de los registros mediante el botón que se encuentra al final de este apartado, tenga mucho cuidado ya que este cambio es irreversible.
  - Cada trabajador que sea eliminado se guardará en un historial de trabajadores en la base de datos, además se incluirá información adicional como la fecha en la que se efectuó la acción y el nombre del usuario responsable.
### Refrescar lista
- Al seleccionar esta opción se refrescará el listado de trabajadores, con tal de ver las actualizaciones que se vayan realizando en el sistema.
### Filtrar listado
- Esta opción solo está disponible para el jefe de Recursos Humanos.
- Permite filtrar y mostrar un listado de trabajadores según los siguientes criterios de filtrado: sexo, cargo y/o área/departamento.
### Ver perfil de usuario
- Todas las cuentas de usuario asociadas a un trabajador permitirán ver su perfil de usuario
- Al seleccionar esta opción se mostrará un resumen de la información registrada.
- En la parte inferior de la ventana se muestran dos botones que permiten las siguientes funciones:
  - Modificar la información personal, cargas familiares y contactos de emergencia (no se permite modificar el RUT ni los datos laborales)
  - Cambiar la contraseña de la cuenta de usuario.
### Privilegios de usuario
A continuación, se dará una breve descripción de los privilegios de cada perfil de usuario:
1. Administrador
La identificación “Administrador” tiene el acceso total al sistema con todas sus funcionalidades.
   - Listar trabajadores
   - Registrar trabajadores
   - Modificar trabajadores
   - Eliminar trabajadores
   - Filtrar listado
   - Ver su perfil de usuario
   - Modificar información personal, cargas familiares y contactos de emergencia de su perfil.
   - Cambiar su contraseña
2. Jefe RR.HH.
La identificación “Jefe RR.HH.” tiene el acceso total al sistema con todas sus funcionalidades.
   - Listar trabajadores
   - Registrar trabajadores
   - Modificar trabajadores
   - Eliminar trabajadores
   - Filtrar listado
   - Ver su perfil de usuario
   - Modificar información personal, cargas familiares y contactos de emergencia de su perfil.
   - Cambiar su contraseña
3. Personal RR.HH.
La identificación “Personal RR.HH.” tiene el acceso casi total al sistema, las funcionalidades
disponibles son las siguientes:
   - Listar trabajadores
   - Registrar trabajadores
   - Modificar trabajadores
   - Eliminar trabajadores
   - Ver su perfil de usuario
   - Modificar información personal, cargas familiares y contactos de emergencia de su perfil.
   - Cambiar su contraseña
5. Trabajador
La identificación “Trabajador” tiene el acceso parcial al sistema, las funcionalidades
disponibles son las siguientes:
   - Ver su perfil de usuario
   - Modificar información personal, cargas familiares y contactos de emergencia de su perfil.
   - Cambiar su contraseña
