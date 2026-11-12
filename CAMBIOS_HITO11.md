# Cambios realizados para el Hito 11

## Se conserva

- El nombre y propósito de ¡Ubícate!
- Los integrantes del equipo.
- Python, Flask, MySQL y las dependencias existentes.
- Las cuatro tablas y sus nombres.
- La búsqueda de materias.
- El registro individual de materias.
- Los datos de ejemplo del archivo SQL.

## Se mejora

- `src/app.py`: ahora también recibe el formulario de registro transaccional y muestra mensajes.
- `src/datos.py`: agrega funciones para listar aulas y para insertar la materia y sus horarios usando una conexión compartida.
- `src/inicio.html`: conserva la búsqueda, el registro individual y la lista de materias; agrega un formulario para registrar una materia con hasta tres horarios.
- `README.md`: agrega instrucciones de ejecución y de prueba.

## Archivo nuevo

- `src/servicios.py`: contiene las validaciones y coordina la transacción con `start_transaction`, `commit` y `rollback`.
- `src/prueba_rollback.py`: provoca un error de clave foránea en el tercer horario y comprueba que la materia no haya quedado guardada.
- `.env.example`: ejemplo de configuración sin contraseñas reales.
- `.gitignore`: evita subir el archivo `.env` y archivos temporales.

## Sobre la base de datos

Se conserva `docs/database.sql` sin cambiar nombres de tablas, columnas, relaciones ni registros de ejemplo. La relación existente entre `materias.id` y `horarios.materia_id` se utiliza para el patrón Maestro-Detalle.

## Límites de esta versión

- El formulario permite ingresar hasta tres horarios por materia.
- La prueba de Rollback requiere que exista al menos un aula.
- No se ha probado una conexión real con MySQL en este entorno. Antes de entregar, ejecutar la aplicación y las dos pruebas en el equipo donde está configurada la base de datos.
