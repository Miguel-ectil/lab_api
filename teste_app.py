import unittest
from app import app
import werkzeug

if not hasattr(werkzeug, '__version__'):
    werkzeug.__version__ = "mock-version"

class APITestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "API is running"})

    def test_login_with_valid_credentials(self):
        payload = {"username": "admin", "password": "password"}
        response = self.client.post('/login', json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("access_token", response.json)

        # Armazena o token para usar em testes protegidos
        self.__class__.access_token = response.json["access_token"]

    def test_login_with_invalid_credentials(self):
        payload = {"username": "admin", "password": "wrong"}
        response = self.client.post('/login', json=payload)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json.get("message"), "Credenciais inválidas")

    def test_protected_no_token(self):
        response = self.client.get('/protected')
        self.assertEqual(response.status_code, 401)
        self.assertIn("msg", response.json)
        self.assertIn("Missing Authorization Header", response.json["msg"])

    def test_protected_with_token(self):
        # Primeiro, faz login para obter o token
        payload = {"username": "admin", "password": "password"}
        login_response = self.client.post('/login', json=payload)
        token = login_response.json["access_token"]

        # Usa o token para acessar a rota protegida
        headers = {"Authorization": f"Bearer {token}"}
        response = self.client.get('/protected', headers=headers)

        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json)
        self.assertTrue("Bem-vindo, admin!" in response.json["message"])

if __name__ == '__main__':
    unittest.main()
