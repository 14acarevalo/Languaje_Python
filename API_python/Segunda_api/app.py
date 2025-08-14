from flask import Flask

api = Flask(__name__)

@api.route('/api_segunda')
def segunda_api():
    return "He creado el esqueleto de mi segunda API con Flask"

if __name__ == '__main__':
    api.run(debug=True)