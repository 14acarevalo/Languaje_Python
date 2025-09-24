from flask import Flask, jsonify

app_presentacion = Flask(__name__)

# Permitir caracteres no ASCII (como tildes y ñ)
app_presentacion.config['JSON_AS_ASCII'] = False

@app_presentacion.route('/api/presentacion')
def presentacion_alberto_api():
    response = {
        "Nombre": "Alberto",
        "Apellido": "Campanero Arévalo",
        "Profesion": "Programador Full Stack",
        "Lenguajes": ["Python", "JavaScript", "Java"],
        "Formacion": [
            {
                "Titulo": "FP en Desarrollo de Aplicaciones Web",
                "Centro": "Instituto Nebrija",
                "Año": 2025
            },
            {
                "Titulo": "Máster en Python, Machine Learning y Big Data",
                "Centro": "Grupo Atrium",
                "Año": 2025
            },
            {
                "Titulo": "Bootcamp de Programación Full Stack",
                "Centro": "Open Bootcamp",
                "Año": 2025
            }
        ]
    }
    return jsonify(response)

if __name__ == '__main__':
    app_presentacion.run(debug=True, port=5000)