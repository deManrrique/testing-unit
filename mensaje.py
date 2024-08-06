import unittest
from unittest.mock import patch, Mock
import requests
import io

# Función que realiza la solicitud GET y maneja la respuesta
def realizar_solicitud():
    response = requests.get('https://api.github.com')
    if response.status_code == 200:
        print("La solicitud fue exitosa.")
        print("Contenido de la respuesta:", response.json())
    else:
        print("La solicitud falló con el estado:", response.status_code)

# Clase de prueba
class TestSolicitud(unittest.TestCase):
    
    @patch('requests.get')
    def test_solicitud_exitosa(self, mock_get):
        # Configurar el mock para simular una respuesta exitosa
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"key": "value"}
        mock_get.return_value = mock_response
        
        # Capturar la salida impresa
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            realizar_solicitud()
            output = mock_stdout.getvalue()
        
        # Imprimir la salida capturada para depuración
        print("Salida capturada en test_solicitud_exitosa:", output)
        
        # Verificar que el mensaje de éxito está presente
        self.assertIn("La solicitud fue exitosa.", output)
        self.assertIn("Contenido de la respuesta: {'key': 'value'}", output)
    
    @patch('requests.get')
    def test_solicitud_fallida(self, mock_get):
        # Configurar el mock para simular una respuesta fallida
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        
        # Capturar la salida impresa
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            realizar_solicitud()
            output = mock_stdout.getvalue()
        
        # Imprimir la salida capturada para depuración
        print("Salida capturada en test_solicitud_fallida:", output)
        
        # Verificar el mensaje de fallo
        self.assertIn("La solicitud falló con el estado: 404", output)

if __name__ == '__main__':
    unittest.main()
