from flask import Flask, jsonify

app = Flask(__name__)

presentacion = [
    {"id": 1, "Nombre": "Juan", "Apellidos": "Pérez", "Edad": 30},
    {"id": 2, "Nombre": "Ana", "Apellidos": "Gómez", "Edad": 25},
    {"id": 3, "Nombre": "Luis", "Apellidos": "Martínez", "Edad": 28},
    {"id": 4, "Nombre": "María", "Apellidos": "López", "Edad": 32},
    {"id": 5, "Nombre": "Pedro", "Apellidos": "Sánchez", "Edad": 27}
]


@app.route('/api/delete_usuarios', methods=['DELETE'])
def eliminar_usuarios():
    if presentacion:
        presentacion.clear()
        return jsonify({"message": "Todos los usuarios han sido eliminados"}), 200
    else:
        return jsonify({"error": "No hay usuarios para eliminar"}), 404
    

@app.route('/api/eliminar_usuario/<int:id>', methods=['DELETE'])
def eliminar_usuario_por_id(id):
    
    usuario = next((usuario for usuario in presentacion if usuario["id"]==id), None)
    if usuario:
        presentacion.remove(usuario)
        return jsonify({"message": f"Usuario con ID {id} ha sido eliminado correctamente"}), 200
    else:
        return jsonify({"error": f"Usuario con ID {id} no encontrado"}), 404
    