from flask import Flask, jsonify

app = Flask(__name__)

presentacion = [
    {"id": 1, "Nombre": "Juan", "Apellidos": "Pérez", "Edad": 30},
    {"id": 2, "Nombre": "Ana", "Apellidos": "Gómez", "Edad": 25},
    {"id": 3, "Nombre": "Luis", "Apellidos": "Martínez", "Edad": 28},
    {"id": 4, "Nombre": "María", "Apellidos": "López", "Edad": 32},
    {"id": 5, "Nombre": "Pedro", "Apellidos": "Sánchez", "Edad": 27}
]

# Esta ruta es la más sencilla, ya que simplemente devuelve todos los usuarios registrados
@app.route('/mostrar_usuarios', methods=['GET'])
def mostrar_usuarios():
    if not presentacion:
        return jsonify({"error": "No hay usuarios registrados"}), 404
    else:
        return jsonify(presentacion)

# En esta ruta vamos a buscar usuario por el ID
@app.route('/mostrar_usuario/<int:id>', methods=['GET'])
def mostrar_usuario(id):
    
    #Verificamos si está presente o no
    #Con el next() buscamos el primer usuario que coincida con el ID, facilitando la búsqueda y evitando un bucle for
    #Si no lo encuentra, devuelve None
    usuario = next((u for u in presentacion if u["id"] == id), None)
    if usuario is None:
        return jsonify({"error": "Usuario no encontrado"}), 404
    else:
        return jsonify(usuario)

#Esto siempre tiene que ir al final, ya que es la ruta que se encarga de insertar un nuevo usuario
if __name__ == '__main__':
    app.run(debug=True)