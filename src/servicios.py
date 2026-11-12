from src.datos import (
    obtener_conexion,
    materia_existe_en_conexion,
    crear_materia_en_conexion,
    crear_horario_en_conexion
)


def registrar_materia_con_horarios(nombre, horarios):
    """
    Registra una materia y sus horarios dentro de una sola transacción.
    Si ocurre un error, revierte todos los cambios.
    """
    nombre = nombre.strip()

    if not nombre:
        raise ValueError("El nombre de la materia es obligatorio.")

    if not horarios:
        raise ValueError("Debe ingresar al menos un horario.")

    horarios_validos = []

    for numero, horario in enumerate(horarios, start=1):
        dia = str(horario.get("dia", "")).strip()
        hora = str(horario.get("hora", "")).strip()
        aula_id = str(horario.get("aula_id", "")).strip()

        if not dia or not hora or not aula_id:
            raise ValueError(
                f"Complete el día, la hora y el aula del horario {numero}."
            )

        try:
            aula_id = int(aula_id)
        except ValueError:
            raise ValueError(f"El aula del horario {numero} no es válida.")

        if aula_id <= 0:
            raise ValueError(f"El aula del horario {numero} no es válida.")

        horarios_validos.append({
            "dia": dia,
            "hora": hora,
            "aula_id": aula_id
        })

    conexion = obtener_conexion()

    try:
        conexion.start_transaction()

        if materia_existe_en_conexion(conexion, nombre):
            raise ValueError("Esta materia ya está registrada.")

        materia_id = crear_materia_en_conexion(conexion, nombre)

        for horario in horarios_validos:
            crear_horario_en_conexion(
                conexion,
                materia_id,
                horario["aula_id"],
                horario["dia"],
                horario["hora"]
            )

        conexion.commit()
        return materia_id

    except Exception:
        if conexion.in_transaction:
            conexion.rollback()
        raise

    finally:
        conexion.close()
