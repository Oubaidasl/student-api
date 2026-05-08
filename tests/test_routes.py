import unittest
from src.app import app

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_get_etudiants(self):
        response = self.client.get('/etudiants')
        self.assertEqual(response.status_code, 200)

    def test_get_etudiant_exist(self):
        response = self.client.get('/etudiants/1')
        self.assertEqual(response.status_code, 200)

    def test_get_etudiant_not_found(self):
        response = self.client.get('/etudiants/999')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
