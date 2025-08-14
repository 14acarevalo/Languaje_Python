from flask import Flask, jsonify, request

app = Flask(__name__)

presentacion = [
    {"id": 1, "Nombre": "Juan", "Apellidos": "Pérez", "Edad": 30},
    {"id": 2, "Nombre": "Ana", "Apellidos": "Gómez", "Edad": 25},
    {"id": 3, "Nombre": "Luis", "Apellidos": "Martínez", "Edad": 28},
    {"id": 4, "Nombre": "María", "Apellidos": "López", "Edad": 32},
    {"id": 5, "Nombre": "Pedro", "Apellidos": "Sánchez", "Edad": 27}
]

#Método para insertarlos usuarios
@app.route('/insertar_usuario', methods=['POST'])
def ingresar_usuario():
    
    #Con este método vamos a insertar un nuevo usuario en la lista de forma dinámica y con JSON
    datos = request.get_json()
    
    #Comprobamos que se está insertando/enviando los datos necesarios para nuestra base de datos
    if not all(u in datos for u in ("Nombre", "Apellidos", "Edad")):
        return jsonify({"error": "Faltan datos obligatorios"}), 400
    else:
        
        #Creamos un nuevo usuario, sumando 1 al ID del último usuario registrado
        nuevo_usuario = {
        "id": len(presentacion) + 1,
        "Nombre": datos["Nombre"],
        "Apellidos": datos["Apellidos"],
        "Edad": datos["Edad"]
        }
        
        presentacion.append(nuevo_usuario)
        return jsonify(nuevo_usuario), 201
    
if __name__ == '__main__':
    app.run(debug=True)