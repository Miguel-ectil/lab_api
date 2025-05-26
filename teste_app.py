import unittest
from app import app
import werkzeug
# Patch temporário para adicionar o atributo '__version__' em werkzeug

if not hasattr(werkzeug, '__version__'):
  werkzeug.__version__ = "mock-version"

class APITestCase(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    # Criação do cliente de teste
    cls.client = app.test_client()

  def test_home(self):
    response = self.client.get('/')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.json, {"message": "API is running"})

  def test_login(self):
    response = self.client.post('/login')
    self.assertEqual(response.status_code, 200)
    self.assertIn('access_token', response.json)

  def test_protected_no_token(self):
    response = self.client.get('/protected')
    self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()