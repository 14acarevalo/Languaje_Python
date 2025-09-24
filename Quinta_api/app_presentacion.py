from flask import Flask, jsonify, request

app = Flask(__name__)

#Creacion de una lista con usuarios para simular una base de datos
presentacion= [
    {"id": 1, "Nombre": "Alberto", "Apellidos": "Campanero Arevalo", "Edad": 30},
    {"id": 2, "Nombre": "María", "Apellidos": "Gómez Pérez", "Edad": 28},
    {"id": 3, "Nombre": "Carlos", "Apellidos": "López Fernández", "Edad": 35},
    {"id": 4, "Nombre": "Ana", "Apellidos": "Martínez García", "Edad": 32},
    {"id": 5, "Nombre": "Laura", "Apellidos": "Sánchez Rodríguez", "Edad": 29},
    {"id": 6, "Nombre": "David", "Apellidos": "Torres Jiménez", "Edad": 31},
    {"id": 7, "Nombre": "Sara", "Apellidos": "Moreno Ruiz", "Edad": 27},
    {"id": 8, "Nombre": "Javier", "Apellidos": "Hernández Díaz", "Edad": 34},
    {"id": 9, "Nombre": "Lucía", "Apellidos": "Ramírez González", "Edad": 26},
    {"id": 10, "Nombre": "Pedro", "Apellidos": "Pérez Martínez", "Edad": 33}
]

@app.route('/api/presentacion')
def obtener_datos_usuario():
    return jsonify(presentacion)

@app.route('/api/presentacion_individual/<int:id>', methods=['GET'])
def obtener_datos_por_usuario(id):
    usuario = next((p for p in presentacion if p["id"] == id), None)
    if usuario is None:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify(usuario)

@app.route('/api/crear_usuario/<int:id>', methods=['POST'])
def crear_usuario(id):
    # 1. Capturamos los datos JSON que el cliente envía en el cuerpo de la petición POST
    datos = request.get_json()

    # 2. Comprobamos que en esos datos están los campos que necesitamos (Nombre, Apellidos, Edad)
    if not all(k in datos for k in ("Nombre", "Apellidos", "Edad")):
        return jsonify({"error": "Faltan datos obligatorios"}), 400

    # 3. Comprobamos que el ID no exista ya en la lista (para evitar duplicados)
    if any(usuario["id"] == id for usuario in presentacion):
        return jsonify({"error": "El usuario ya existe en la base de datos con ese ID"}), 400

    # 4. Creamos el nuevo usuario con el id que viene en la URL y los datos del JSON
    nuevo_usuario = {
        "id": id,
        "Nombre": datos["Nombre"],
        "Apellidos": datos["Apellidos"],
        "Edad": datos["Edad"]
    }

    # 5. Añadimos ese nuevo usuario a la lista
    presentacion.append(nuevo_usuario)

    # 6. Devolvemos el usuario creado con código 201 (creado)
    return jsonify(nuevo_usuario), 201

@app.route('/api/actualizar_usuario/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    
    # 1. Capturamos los datos JSON que el cliente envía en el cuerpo de la petición POST
    datos = request.get_json()

    # 2. Comprobamos que el ID exista ya en la lista (para actualizar)
    if any(usuario["id"] == id for usuario in presentacion):
        
        # 3. Comprobamos que en esos datos están los campos que necesitamos (Nombre, Apellidos, Edad)
        if not all(k in datos for k in ("Nombre", "Apellidos", "Edad")):
            return jsonify({"error": "Faltan datos obligatorios"}), 400

        # 4. Actualizamos el usuario con el id que viene en la URL y los datos del JSON
        for usuario in presentacion:
            if usuario["id"] == id:
                usuario["Nombre"] = datos["Nombre"]
                usuario["Apellidos"] = datos["Apellidos"]
                usuario["Edad"] = datos["Edad"]
                break

        # 5. Devolvemos el usuario actualizado
        return jsonify(usuario)
    # 4. Creamos el nuevo usuario con el id que viene en la URL y los datos del JSON
    else:
        return jsonify({"error": "El usuario no existe en la base de datos con ese ID"}), 404


@app.route('/api/eliminar_usuarios', methods=['DELETE'])
def eliminar_usuarios():
    # 1. Limpiamos la lista de usuarios
    presentacion.clear()
    
    # 2. Devolvemos un mensaje de éxito
    return jsonify({"message": "Todos los usuarios han sido eliminados"}), 200
    


@app.route('/api/eliminar_usuario_por_id/<int:id>', methods=['DELETE'])
def eliminar_usuario_por_id(id):
    if any(usuario["id"] == id for usuario in presentacion):
        # 1. Filtramos la lista para eliminar el usuario con el ID especificado
        presentacion[:] = [usuario for usuario in presentacion if usuario["id"] != id]
        
        # 2. Devolvemos un mensaje de éxito
        return jsonify({"message": "Usuario eliminado correctamente"}), 200
    else:
        return jsonify({"error": "El usuario no existe en la base de datos con ese ID"}), 404




#Esto debe ir siempre al final del archivo para que se ejecute la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)
