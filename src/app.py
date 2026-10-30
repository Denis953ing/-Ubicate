from flask import Flask, render_template, request, redirect, url_for, flash
from src.busqueda import buscar
from src.datos import listar_materias, registrar_materia

app = Flask(__name__, template_folder=".")
app.secret_key = "ubicate-clave-local-cambiar"

@app.route("/", methods=["GET", "POST"])
def inicio():
    texto = ""
    resultados = []
    mensaje = None

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

    texto = request.args.get("materia", "").strip()
    resultados = buscar(texto) if texto else []

    materias = listar_materias()

    return render_template(
        "inicio.html",
        resultados=resultados,
        texto=texto,
        materias=materias
    )


if __name__ == "__main__":
    app.run(debug=True)