import unittest
from app import app

class TestAppIntegration(unittest.TestCase):

    def setUp(self):
        # Setup test client
        self.app = app.test_client()
        self.app.testing = True

    def test_root_endpoint(self):
        # Test root endpoint
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Happy Learning With DevopClinics!!!', response.data)

    def test_custom_color_endpoint(self):
        # Test root endpoint with color change
        response = self.app.get('/green')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'background-color:green', response.data)
        
    def test_invalid_route_fallback(self):
        # Test invalid color input, which should fallback to the default color handling
        response = self.app.get('/<invalid>')
        self.assertEqual(response.status_code, 200)
        # Assuming default fallback if route parameter is ignored
        self.assertIn(b'Happy Learning With DevopClinics!!!', response.data)

if __name__ == '__main__':
    unittest.main()
