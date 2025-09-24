from flask import Flask, jsonify

app3 = Flask(__name__)



servicios = [
    {"id":1, "nombre": "Servicio Pádel", "descripcion": "Actividades deportivas de pádel"},
    {"id": 2, "nombre": "Servicio de fútbol", "descripcion": "Alquiler de pistas de fútbol"},
    {"id": 3, "nombre": "Servicio de tenis", "descripcion": "Servicio de liga de tenis"}
]

@app3.route('/api_tercera')
def tercera_api():
    return "He creado una tercera API y vamos a complicarla un poco más"

    
@app3.route('/api/servicios', methods= ['GET'])
def obtener_servicios():
    return jsonify(servicios)

if __name__ =='__main__':
    app3.run(debug=True)