import unittest
from app import app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Happy Learning With DevopClinics!!!', result.data)

    def test_color(self):
        result = self.app.get('/blue')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Happy Learning With DevopClinics!!!', result.data)

if __name__ == "__main__":
    unittest.main()
