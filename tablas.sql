-- BD
CREATE DATABASE trabajadores;
USE trabajadores;

-- TABLAS

CREATE TABLE identificacion (
    id     INT NOT NULL,
    nombre VARCHAR(30) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE sexo (
    id     INT NOT NULL,
    nombre VARCHAR(10) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE parentesco (
    id     INT NOT NULL,
    nombre VARCHAR(30) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE cargo (
    id     INT NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE areadepartamento (
    id     INT NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE trabajador (
    rut       INT NOT NULL,
    rut_dv    CHAR(1) NOT NULL,
    nombre    VARCHAR(30) NOT NULL,
    apellido  VARCHAR(30) NOT NULL,
    sexo      INT NOT NULL,
    direccion VARCHAR(120) NOT NULL,
    PRIMARY KEY (rut),
    FOREIGN KEY (sexo) REFERENCES sexo (id)
);

CREATE TABLE telefono (
    id             INT AUTO_INCREMENT,
    numero         VARCHAR(12) NOT NULL,
    trabajador_rut INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (trabajador_rut) REFERENCES trabajador (rut)
);

CREATE TABLE datoslaborales (
    id                INT AUTO_INCREMENT,
    cargo_id          INT NOT NULL,
    area_departamento INT NOT NULL,
    fecha_ingreso     DATE NOT NULL,
    trabajador_rut    INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (cargo_id) REFERENCES cargo (id),
    FOREIGN KEY (area_departamento) REFERENCES areadepartamento (id),
    FOREIGN KEY (trabajador_rut) REFERENCES trabajador (rut)
);

CREATE TABLE contactosemergencia (
    id             INT AUTO_INCREMENT,
    nombre         VARCHAR(30) NOT NULL,
    apellido       VARCHAR(30) NOT NULL,
    relacion       INT NOT NULL,
    telefono       INT NOT NULL,
    trabajador_rut INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (relacion) REFERENCES parentesco (id),
    FOREIGN KEY (trabajador_rut) REFERENCES trabajador (rut)
);

CREATE TABLE credencial (
    username VARCHAR(30) NOT NULL,
    password VARCHAR(30) NOT NULL,
    identificacion_id INT NOT NULL,
    PRIMARY KEY (username),
    FOREIGN KEY (identificacion_id) REFERENCES identificacion (id)
);

CREATE TABLE cargafamiliar (
    id             INT AUTO_INCREMENT,
    rut            INT NOT NULL,
    rut_dv         CHAR(1) NOT NULL,
    nombre         VARCHAR(30) NOT NULL,
    apellido       VARCHAR(30) NOT NULL,
    sexo           INT NOT NULL,
    parentesco_id  INT NOT NULL,
    trabajador_rut INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (parentesco_id) REFERENCES parentesco (id),
    FOREIGN KEY (sexo) REFERENCES sexo (id),
    FOREIGN KEY (trabajador_rut) REFERENCES trabajador (rut)
);

CREATE TABLE credencialtrabajador (
    usuario_username VARCHAR(30) NOT NULL,
    trabajador_rut   INT NOT NULL,
    FOREIGN KEY (trabajador_rut) REFERENCES trabajador (rut),
    FOREIGN KEY (usuario_username) REFERENCES credencial (username)
);

-- INSERTS

INSERT INTO identificacion (id, nombre)
VALUES
    (1, 'Administrador'),
    (2, 'Personal RRHH'),
    (3, 'Jefe RRHH'),
    (4, 'Trabajador');

INSERT INTO sexo (id, nombre)
VALUES
    (1, 'Masculino'),
    (2, 'Femenino');

INSERT INTO parentesco (id, nombre)
VALUES
    (1, 'Hijo/a'),
    (2, 'Cónyuge'),
    (3, 'Padre'),
    (4, 'Madre'),
    (5, 'Hermano/a'),
    (6, 'Abuelo/a'),
    (7, 'Nieto/a'),
    (8, 'Suegro/a'),
    (9, 'Yerno'),
    (10, 'Nuera'),
    (11, 'Hermanastro/a'),
    (12, 'Cuñado/a'),
    (13, 'Tío/a'),
    (14, 'Sobrino/a'),
    (15, 'Primo/a'),
    (16, 'Otro'),
    (17, 'Amigo/a cercano/a');

INSERT INTO cargo (id, nombre)
VALUES
    (1, 'Gerente de Operaciones'),
    (2, 'Supervisor de Distribución'),
    (3, 'Supervisor de Entrega'),
    (4, 'Personal de Clasificación y Distribución'),
    (5, 'Personal de Entrega'),
    (6, 'Gerente de Atención al Cliente'),
    (7, 'Representante de Servicio al Cliente'),
    (8, 'Especialista en Seguimiento de Envíos'),
    (9, 'Coordinador de Reclamaciones'),
    (10, 'Gerente de Ventas y Marketing'),
    (11, 'Ejecutivo de Ventas'),
    (12, 'Especialista en Marketing Digital'),
    (13, 'Coordinador de Alianzas Comerciales'),
    (14, 'Gerente de Recursos Humanos'),
    (15, 'Contador'),
    (16, 'Analista Financiero'),
    (17, 'Especialista en Cuentas por Pagar'),
    (18, 'Especialista en Cuentas por Cobrar'),
    (19, 'Gerente Financiero'),
    (20, 'Especialista en Reclutamiento y Selección'),
    (21, 'Especialista en Capacitación y Desarrollo'),
    (22, 'Coordinador de Nómina y Beneficios'),
    (23, 'Especialista en Relaciones Laborales'),
    (24, 'Gerente de Tecnología de la Información'),
    (25, 'Administrador de Sistemas'),
    (26, 'Desarrollador de Software'),
    (27, 'Especialista en Seguridad Informática'),
    (28, 'Técnico de Soporte Técnico'),
    (29, 'Gerente de Logística y Almacén'),
    (30, 'Coordinador de Inventarios'),
    (31, 'Planificador de Rutas'),
    (32, 'Especialista en Cadena de Suministro'),
    (33, 'Almacenista');

INSERT INTO areadepartamento (id, nombre)
VALUES
    (1, 'Departamento de Operaciones'),
    (2, 'Departamento de Servicio al Cliente'),
    (3, 'Departamento de Ventas y Marketing'),
    (4, 'Departamento de Recursos Humanos'),
    (5, 'Departamento Financiero y Contable'),
    (6, 'Departamento de Tecnología de la Información'),
    (7, 'Departamento de Calidad y Control de Procesos');

INSERT INTO credencial (username, password, identificacion_id)
VALUES ('admin', 'admin', 1);