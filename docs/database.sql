CREATE DATABASE IF NOT EXISTS ubicate;
USE ubicate;

CREATE TABLE pabellones (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(80) NOT NULL
);

CREATE TABLE aulas (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(30) NOT NULL,
  pabellon_id INT,
  FOREIGN KEY (pabellon_id) REFERENCES pabellones(id)
);

CREATE TABLE materias (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL
);

CREATE TABLE horarios (
  id INT AUTO_INCREMENT PRIMARY KEY,
  materia_id INT,
  aula_id INT,
  dia VARCHAR(20),
  hora VARCHAR(20),
  FOREIGN KEY (materia_id) REFERENCES materias(id),
  FOREIGN KEY (aula_id) REFERENCES aulas(id)
);

INSERT INTO pabellones (nombre) VALUES ('Pabellon de ejemplo');
INSERT INTO aulas (nombre, pabellon_id) VALUES ('Aula de ejemplo', 1);
INSERT INTO materias (nombre) VALUES ('Materia de ejemplo');
INSERT INTO horarios (materia_id, aula_id, dia, hora)
VALUES (1, 1, 'Lunes', '8:00');
