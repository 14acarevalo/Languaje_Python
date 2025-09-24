from flask import Flask, jsonify, request

app = Flask(__name__)

presentacion = [
    {"id": 1, "Nombre": "Juan", "Apellidos": "Pérez", "Edad": 30},
    {"id": 2, "Nombre": "Ana", "Apellidos": "Gómez", "Edad": 25},
    {"id": 3, "Nombre": "Luis", "Apellidos": "Martínez", "Edad": 28},
    {"id": 4, "Nombre": "María", "Apellidos": "López", "Edad": 32},
    {"id": 5, "Nombre": "Pedro", "Apellidos": "Sánchez", "Edad": 27}
]

@app.route('/api/update_usuario/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    datos = request.get_json()
    
    if any(usuario["id"] == id for usuario in presentacion):
    
        if not all(k in datos for k in("Nombre", "Apellidos", "Edad")):
            return jsonify({"error": "Faltan datos obligatorios"}, 400)
        
        for usuario in presentacion:
            if usuario["id"] == id:
                usuario["Nombre"] = datos ["Nombre"],
                usuario["Apellidos"] = datos["Apellidos"],
                usuario["Edad"] = datos["Edad"]
                
        return jsonify(usuario), 200

    else:
            return jsonify({"error": "El usuario no existe en la base de datos con ese ID"}), 404
        
if __name__ == '__main__':
    app.run(debug=True)