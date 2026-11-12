# ¡Ubícate!

Este proyecto ayuda a los estudiantes a encontrar aulas y horarios de la UNAN-León.

## Integrantes

- Hanzell Alberto Ferrufino Varela
- Denis Jose Davila Cruz
- Samuel Isai Alvarado Cruz
- Leader Ariel Martinez Campo

## Que usamos

- Python
- Flask
- MySQL
- Figma

## Como se divide

- `src/app.py`: aplicación Flask y rutas.
- `src/busqueda.py`: lógica de búsqueda.
- `src/datos.py`: conexión y consultas a MySQL.
- `src/servicios.py`: reglas y registro transaccional de materias con horarios.
- `src/inicio.html`: página que utiliza el estudiante.
- `docs/database.sql`: creación de la base de datos, tablas y datos de ejemplo.
- `requirements.txt`: dependencias.
- `.env`: configuración local privada; no debe publicarse.

## Para empezar

1. Instalar Python y MySQL.
2. Instalar las librerías:

   `pip install -r requirements.txt`

3. Crear la base de datos ejecutando `docs/database.sql` en MySQL.
4. Copiar `.env.example` como `.env` y colocar los datos de conexión de MySQL.
5. Ejecutar la aplicación desde la carpeta del proyecto:

   `python -m src.app`

6. Abrir la dirección local que muestra Flask en el navegador.

## Registro transaccional

La opción nueva permite registrar una materia con hasta tres horarios desde el formulario.

El servicio valida los datos, inicia una transacción, registra la materia y sus horarios y confirma con `commit`. Si ocurre un error, utiliza `rollback` para cancelar los cambios.

## Prueba de Rollback

Debe existir al menos un aula en la base de datos. Ejecutar:

`python -m src.prueba_rollback`

El programa intenta registrar una materia de prueba y provoca un error de clave foránea en el tercer horario. Después comprueba que la materia no haya quedado guardada.

La prueba es para desarrollo y no debe ejecutarse durante un registro real.

Prototipo:
https://www.figma.com/proto/EXnLgGlutDsBMBIJoJ3kn5/Sin-t%C3%ADtulo?node-id=4-1799&p=f&t=Tjxiv26jAjFDk3Vx-1&scaling=scale-down&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=4%3A1480
