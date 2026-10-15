from flask import Flask, render_template, request
from src.business.busqueda import buscar
app = Flask(__name__, template_folder="presentation/templates")

@app.route("/")
def inicio():
    texto = request.args.get("materia", "")
    resultados = buscar(texto)
    return render_template("inicio.html", resultados=resultados, texto=texto)

if __name__ == "__main__":
    app.run(debug=True)
