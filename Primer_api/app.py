from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/') #Conducimos a la ruta raíz
def inicio(): #Creamos la funcion
    return "Bienvenido a mi primera API con Flask"

if __name__ == '__main__':
    app.run(debug=True)#Mensaje de bienvenida