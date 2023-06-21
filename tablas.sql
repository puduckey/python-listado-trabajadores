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
    nombre VARCHAR(40) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE areadepartamento (
    id     INT NOT NULL,
    nombre VARCHAR(30) NOT NULL,
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
    id             INT NOT NULL,
    numero         VARCHAR(12) NOT NULL,
    trabajador_rut INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (trabajador_rut) REFERENCES trabajador (rut)
);

CREATE TABLE datoslaborales (
    id                INT NOT NULL,
    cargo_id          INT NOT NULL,
    area_deparmatento INT NOT NULL,
    fecha_ingreso     DATE NOT NULL,
    trabajador_rut    INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (cargo_id) REFERENCES cargo (id),
    FOREIGN KEY (area_deparmatento) REFERENCES areadepartamento (id),
    FOREIGN KEY (trabajador_rut) REFERENCES trabajador (rut)
);

CREATE TABLE contactosemergencia (
    id             INT NOT NULL,
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
    rut            INT NOT NULL,
    rut_dv         CHAR(1) NOT NULL,
    nombre         VARCHAR(30) NOT NULL,
    apellido       VARCHAR(30) NOT NULL,
    sexo           INT NOT NULL,
    parentesco_id  INT NOT NULL,
    trabajador_rut INT NOT NULL,
    PRIMARY KEY (rut),
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
