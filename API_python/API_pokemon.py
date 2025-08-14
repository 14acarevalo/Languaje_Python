import requests

url = 'https://pokeapi.co/api/v2/pokemon/pikachu'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Nombre: {data['name']}")
    print(f"Altura: {data['height']}")
    print(f"Peso: {data['weight']}")
else:
    print("Error al acceder a la API")
