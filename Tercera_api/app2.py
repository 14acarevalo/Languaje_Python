from flask import Flask, jsonify

app = Flask(__name__)

@app.route('api/route')
def funcion_ejemplo():
    return "Recordatorio de la construcción de una API con Flask"

if __name__ == '__main__':
    app.run(debug=True)