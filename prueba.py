import requests

# Función que realiza la solicitud GET y maneja la respuesta
def realizar_solicitud():
    response = requests.get('https://api.github.com')
    if response.status_code == 200:
        print("La solicitud fue exitosa.")
        print("Contenido de la respuesta:", response.json())
    else:
        print("La solicitud falló con el estado:", response.status_code)

# Ejecutar la función directamente
realizar_solicitud()
