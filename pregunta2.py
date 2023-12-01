# Pregunta 2 (5 puntos)
"""
Realizar 4 pruebas unitarias para un caso de éxito y tres de error. Incluir las pruebas unitarias
en el mismo repositorio Github.
Adicionar comentarios en cada prueba indicando el caso de prueba.
"""
import unittest
from pregunta1 import app, BaseDatos, Cuenta, Operacion
from datetime import datetime

class TestBilletera(unittest.TestCase):
    def setUp(self): #Configuracion inicial para las pruebas
        app.testing = True
        self.app = app.test_client()
        self.cuenta = Cuenta("21345", "Arnaldo", 200, ["123", "456"])
        BaseDatos["21345"] = self.cuenta
        BaseDatos["123"] = Cuenta("123", "Luisa", 400, ["456"])
        BaseDatos["456"] = Cuenta("456", "Andrea", 300, ["21345"])

    # 1 Caso éxito: Prueba para /billetera/contactos
    def test_contactos_exitoso(self): # Se espera que el numero 123 y 456 esten en los contactos
        response = self.app.get('/billetera/contactos?minumero=21345')
        self.assertEqual(response.status_code, 200)
        self.assertIn("123", str(response.data))
        self.assertIn("456", str(response.data))

    # 1 Caso de error: Prueba para /billetera/pagar
    def test_pagar_saldo_insuficiente(self): # Tomaremos en cuenta que el saldo es insuficiente
        response = self.app.get('/billetera/pagar?minumero=123&numerodestino=456&valor=1000')
        self.assertEqual(response.status_code, 200)
        self.assertIn("No tiene saldo suficiente", str(response.data))

    # 2 Caso de error: Prueba para /billetera/pagar
    def test_no_encontrado(self): # Tomaremos en cuenta que el numero de destino no se encuentra en los contactos
        response = self.app.get('/billetera/pagar?minumero=123&numerodestino=789&valor=50')
        self.assertEqual(response.status_code, 200)
        self.assertIn("No se encontró el número destino", str(response.data))  

    # 3 Caso de error: Prueba para /billetera/historial
    def test_historial_numero_no_encontrado(self): # Tomaremos en cuenta que el numero no se encuentra en los contactos, por lo que no se puede mostrar el historial
        response = self.app.get('/billetera/historial?minumero=99900')
        self.assertEqual(response.status_code, 404)
        self.assertIn("No se encontró el numero", str(response.data))

if __name__ == '__main__':
    unittest.main()

