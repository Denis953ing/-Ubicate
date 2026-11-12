from flask import Flask, render_template, request, redirect, url_for, flash

from src.busqueda import buscar
from src.datos import listar_aulas, listar_materias, registrar_materia
from src.servicios import registrar_materia_con_horarios

app = Flask(__name__, template_folder=".")
app.secret_key = "ubicate-clave-local-cambiar"


@app.route("/", methods=["GET", "POST"])
def inicio():
    if request.method == "POST":
        accion = request.form.get("accion")

        if accion == "registrar_materia":
            nombre = request.form.get("nombre", "").strip()

            try:
                registrar_materia(nombre)
                flash("Materia registrada correctamente.", "exito")
            except ValueError as error:
                flash(str(error), "error")
            except Exception:
                app.logger.exception("Error al registrar la materia")
                flash(
                    "No se pudo registrar la materia. "
                    "Comprueba que no haya ocurrido un error en MySQL.",
                    "error"
                )

            return redirect(url_for("inicio"))

        if accion == "registrar_materia_horarios":
            nombre = request.form.get("nombre_transaccion", "").strip()
            dias = request.form.getlist("dia[]")
            horas = request.form.getlist("hora[]")
            aulas = request.form.getlist("aula_id[]")

            horarios = []
            for dia, hora, aula_id in zip(dias, horas, aulas):
                if not dia.strip() and not hora.strip() and not aula_id.strip():
                    continue

                horarios.append({
                    "dia": dia,
                    "hora": hora,
                    "aula_id": aula_id
                })

            try:
                materia_id = registrar_materia_con_horarios(nombre, horarios)
                flash(
                    "Materia y horarios registrados correctamente. "
                    f"ID de la materia: {materia_id}.",
                    "exito"
                )
            except ValueError as error:
                flash(str(error), "error")
            except Exception:
                app.logger.exception("Error en el registro de materia y horarios")
                flash(
                    "No se pudo completar el registro. "
                    "No se guardaron cambios parciales.",
                    "error"
                )

            return redirect(url_for("inicio"))

    texto = request.args.get("materia", "").strip()
    resultados = buscar(texto) if texto else []
    materias = listar_materias()
    aulas = listar_aulas()

    return render_template(
        "inicio.html",
        resultados=resultados,
        texto=texto,
        materias=materias,
        aulas=aulas
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
