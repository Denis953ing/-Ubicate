from datetime import datetime

from src.datos import obtener_conexion, listar_aulas
from src.servicios import registrar_materia_con_horarios


def comprobar_rollback():
    aulas = listar_aulas()

    if not aulas:
        print("Primero debe existir al menos un aula en la base de datos.")
        return

    nombre_prueba = "PRUEBA ROLLBACK " + datetime.now().strftime("%Y%m%d%H%M%S")
    aula_valida = aulas[0][0]

    horarios = [
        {
            "dia": "Lunes",
            "hora": "8:00",
            "aula_id": aula_valida
        },
        {
            "dia": "Miércoles",
            "hora": "10:00",
            "aula_id": aula_valida
        },
        {
            "dia": "Viernes",
            "hora": "8:00",
            "aula_id": 2147483647
        }
    ]

    try:
        registrar_materia_con_horarios(nombre_prueba, horarios)
        print("La prueba no produjo el error esperado.")
        return
    except Exception as error:
        print("Se produjo el error esperado en el tercer horario:")
        print(error)

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute(
            "SELECT id FROM materias WHERE nombre = %s",
            (nombre_prueba,)
        )
        materia = cursor.fetchone()

        if materia is None:
            print("Rollback comprobado: la materia no quedó guardada.")
        else:
            print("Revisar la prueba: la materia todavía aparece guardada.")

    finally:
        cursor.close()
        conexion.close()


if __name__ == "__main__":
    comprobar_rollback()
