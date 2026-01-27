from flask import Flask, request, jsonify
from config import PERSONAJES

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    mensaje = data.get("mensaje")
    personaje = data.get("personaje", "LUCA")

    perfil = PERSONAJES.get(personaje, PERSONAJES["LUCA"])

    respuesta = f"{perfil['nombre']} dice: Hola, soy un chatbot {perfil['genero']} con actitud {perfil['personalidad']}."

    return jsonify({"respuesta": respuesta})

if __name__ == "__main__":
    app.run(debug=True)
