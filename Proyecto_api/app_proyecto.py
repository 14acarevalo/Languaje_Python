from flask import Flask, jsonify, request

#Ponemos un nombre a nuestra aplicación - variable
app_proyecto = Flask(__name__)

#Creamos una lista de servicios que vamos a utilizar

servicios = [
    {"id": 1, "Nombre": "Tenis", "Descripcion": "Pista de tenis con iluminación y césped artificial"},
    {"id": 2, "Nombre": "Fútbol", "Descripcion": "Campo de fútbol 11 con césped natural"},
    {"id": 3, "Nombre": "Natación", "Descripcion": "Piscina cubierta de 25 metros"},
    {"id": 4, "Nombre": "Gimnasio", "Descripcion": "Gimnasio equipado con máquinas de última generación"},
    {"id": 5, "Nombre": "Baloncesto", "Descripcion": "Cancha de baloncesto con iluminación y gradas"},
    {"id": 6, "Nombre": "Pádel", "Descripcion": "Pista de pádel con iluminación y césped artificial"}
]

#Creamos nuestras rutas
#Empezamos por la ruta lista de servicios
@app_proyecto.route('/api/servicios', methods=['GET'])
def obtener_servicios():
    if servicios:
        return jsonify(servicios), 200
    else:
        return jsonify({"error": "No hay servicios disponibles"}), 404
    
#Creamos la ruta para sacar un servicio en concreto por su ID
@app_proyecto.route('/api/servicios/<int:id>', methods=['GET'])
def obtener_servicios_por_id(id):
    
    #Sacamos el servicio y en caso de que no existe, devolvemos el siguiente
    servicio_encontrado= next((servicio for servicio in servicios if servicio["id"] == id), None)
    
    #Entramos en el bucle
    if servicio_encontrado:
        return jsonify(servicio_encontrado), 200
    else:
        return jsonify({"error": "Servicio no encontrado"}), 404
    

#Creamos la ruta para insertar un nuevo servicio
@app_proyecto.route('/api/servicios', methods=['POST'])

#Primer paso, creamos la funcion que va a insertar el servicio
def insertar_servicio():
    datos = request.get_json()

    #Segundo paso, comprobamos que se inserta todos los datos necesarios
    
    if not all(servicio_creado in datos for servicio_creado in("Nombre", "Descripcion")):
        return jsonify({"error": "Faltan datos obligatorios"}), 400
    
    #Tercer paso, creamos el nuevo servicio
    nuevo_servicio = {
        "id": len(servicios)+1,
        "Nombre": datos["Nombre"],
        "Descripcion": datos ["Descripcion"]
    }
    
    #Cuarto paso, añadimos el servicio
    servicios.append(nuevo_servicio)
    return jsonify(nuevo_servicio), 201

#Creamos la ruta para actualizar un servicio por su ID
@app_proyecto.route('/api/servicios/<int:id>', methods=['PUT'])
def actualizar_servicio(id):
    servicio = next((s for s in servicios if s["id"] == id), None)
    
    if servicio:
        datos = request.get_json()
        # Actualizamos solo si se proporciona el dato, no es obligatorio enviar ambos
        if "Nombre" in datos:
            servicio["Nombre"] = datos["Nombre"]
        if "Descripcion" in datos:
            servicio["Descripcion"] = datos["Descripcion"]
        return jsonify(servicio), 200
    else:
        return jsonify({"error": f"Servicio con ID {id} no encontrado"}), 404

#Creamos la ruta para borrar todos los servicios
@app_proyecto.route('/api/servicios', methods=['DELETE'])
def borrar_servicios():
    if servicios:
        servicios.clear()
        return jsonify({"message": "Todos los servicios han sido eliminados"}), 200
    else:
        return jsonify({"error": "No hay servicios para eliminar"}), 404

#Creamos la ruta para borrar un servicio por su ID   
@app_proyecto.route('/api/servicios/<int:id>', methods= ['DELETE'])
def borrar_servicio_por_id(id):
    #Buscamos el servicio por su ID
    servicio_encontrado = next((s for s in servicios if s["id"] == id), None)
    
    #Si lo encontramos, lo eliminamos
    if servicio_encontrado:
        servicios.remove(servicio_encontrado)
        return jsonify({"message": f"Servicio con ID {id} ha sido eliminado correctamente"}), 200
    #Si no lo encontramos, devolvemos un error
    else:
        return jsonify({"error": f"Servicio con ID {id} no encontrado"}), 404
    
    
#Por último, ejecutamos nuestra aplicación
if __name__ == '__main__':
    #Recuerda que debe de llamarse así para que se ejecute la aplicación, ya que la nombramos al principio
    app_proyecto.run(debug=True)