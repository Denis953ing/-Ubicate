import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def obtener_conexion():
    """Conecta con la base de datos MySQL."""
    return mysql.connector.connect(
        host=os.getenv("db_host", "localhost"),
        user=os.getenv("db_user", "root"),
        password=os.getenv("db_password"),
        database=os.getenv("db_name", "ubicate")
    )


def buscar_materia(texto):
    """Busca una materia con su aula, pabellón y horario."""
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        consulta = """
            SELECT materias.nombre,
                   aulas.nombre,
                   pabellones.nombre,
                   horarios.dia,
                   horarios.hora
            FROM horarios
            JOIN materias
                ON materias.id = horarios.materia_id
            JOIN aulas
                ON aulas.id = horarios.aula_id
            JOIN pabellones
                ON pabellones.id = aulas.pabellon_id
            WHERE materias.nombre LIKE %s
        """
        cursor.execute(consulta, (f"%{texto}%",))
        return cursor.fetchall()

    finally:
        cursor.close()
        conexion.close()


def listar_materias():
    """Devuelve todas las materias registradas."""
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute(
            "SELECT id, nombre FROM materias ORDER BY nombre"
        )
        return cursor.fetchall()

    finally:
        cursor.close()
        conexion.close()


def registrar_materia(nombre):
    """Registra una materia nueva y evita duplicados."""
    nombre = nombre.strip()

    if not nombre:
        raise ValueError("El nombre de la materia es obligatorio.")

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        # Comprobar si la materia ya existe
        cursor.execute(
            "SELECT id FROM materias WHERE LOWER(nombre) = LOWER(%s)",
            (nombre,)
        )

        if cursor.fetchone():
            raise ValueError("Esta materia ya está registrada.")

        # Registrar la materia si no existe
        cursor.execute(
            "INSERT INTO materias (nombre) VALUES (%s)",
            (nombre,)
        )

        conexion.commit()

    except Exception:
        conexion.rollback()
        raise

    finally:
        cursor.close()
        conexion.close()