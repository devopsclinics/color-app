import unittest
from app import app

class TestAppUnit(unittest.TestCase):

    def setUp(self):
        # Setup test client
        self.app = app.test_client()
        self.app.testing = True

    def test_display_pattern_default_color(self):
        # Test default color behavior (should use 'red' as specified in the code).
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'background-color:red', response.data)

    def test_display_pattern_custom_color(self):
        # Test with a custom color (e.g., 'blue').
        response = self.app.get('/blue')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'background-color:blue', response.data)

    def test_display_pattern_invalid_route(self):
        # Test handling of an invalid route.
        response = self.app.get('/invalid')
        self.assertEqual(response.status_code, 200)
        # Expecting default color if route parameter is ignored or invalid.

    def test_display_pattern_content(self):
        # Test that the page content includes the text "Happy Learning With DevopClinics!!!".
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Happy Learning With DevopClinics!!!', response.data)

if __name__ == '__main__':
    unittest.main()
