import unittest
from app import app
import werkzeug
# Patch temporário para adicionar o atributo '__version__' em werkzeug

if not hasattr(werkzeug, '__version__'):
    werkzeug.__version__ = "mock-version"

class APITestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, dict, "Resposta de / não é um JSON válido")
        self.assertIn("message", response.json, "Campo 'message' ausente na resposta")
        self.assertEqual(response.json["message"], "API is running", "Mensagem incorreta retornada")

    def test_login(self):
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 200, "Status code do login não é 200")
        self.assertIsInstance(response.json, dict, "Resposta do login não é um JSON")
        self.assertIn("access_token", response.json, "Campo 'access_token' ausente na resposta")
        self.assertIsInstance(response.json["access_token"], str, "'access_token' não é uma string")

        token_parts = response.json["access_token"].split('.')
        self.assertEqual(len(token_parts), 3, "Token JWT inválido: não tem 3 partes")

    def test_protected_no_token(self):
        response = self.client.get('/protected')
        self.assertEqual(response.status_code, 401, "Proteção falhou: acesso sem token não retornou 401")

        self.assertIsInstance(response.json, dict, "Resposta da rota protegida sem token não é JSON")
        self.assertIn("msg", response.json, "Mensagem de erro ausente na resposta")
        self.assertIn("Missing Authorization Header", response.json["msg"], "Mensagem de erro inesperada")

if __name__ == '__main__':
    unittest.main()