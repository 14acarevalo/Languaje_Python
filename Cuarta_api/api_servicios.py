from flask import Flask, jsonify

app = Flask (__name__)

servicios = [
        {"id": 1, "nombre": "Servicio de natación", "descripcion": "Clases y entrenamientos de natación"},
        {"id": 2, "nombre": "Servicio de yoga", "descripcion": "Clases de yoga para todos los niveles"},
        {"id": 3, "nombre": "Servicio de gimnasio", "descripcion": "Acceso a instalaciones de gimnasio"}
    ]

@app.route('/api/servicios', methods=['GET'])
def obtener_servicios():
    return jsonify(servicios)

@app.route('/api/servicios/<int:id>', methods=['GET'])
def obtener_servicio_por_id(id):
    if id < 1 or id > len(servicios):
        return jsonify({"error": "Servicio no encontrado"}), 404
    else:
        return jsonify(servicios[id - 1])
    
    
    
    
    

if __name__ == '__main__':
    app.run(debug=True)