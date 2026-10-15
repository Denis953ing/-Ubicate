import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def buscar_materia(texto):
    conexion = mysql.connector.connect(
        host=os.getenv("db_host", "localhost"),
        user=os.getenv("db_user", "root"),
        password=os.getenv("db_password", ""),
        database=os.getenv("db_name", "ubicate")
    )
    cursor = conexion.cursor()
    cursor.execute(
        "select materias.nombre, aulas.nombre, pabellones.nombre, horarios.dia, horarios.hora "
        "from horarios join materias on materias.id = horarios.materia_id "
        "join aulas on aulas.id = horarios.aula_id "
        "join pabellones on pabellones.id = aulas.pabellon_id "
        "where materias.nombre like %s",
        ("%" + texto + "%",)
    )
    datos = cursor.fetchall()
    cursor.close()
    conexion.close()
    return datos
