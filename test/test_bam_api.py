import unittest
import sys
# sys.path.insert(0, '/home/ludaone/andela/book-a-meal')

from app.bamApi import app
import json

class BamApiTestCase(unittest.TestCase):

    def setup(self):
        app.testing = True
        self.app = app.test_client()

    # Basic test for a status 200 on index route
    def test_index(self):
        response = self.app.get('/')
        result = json.loads(response.data)

        self.assertEqual(result.status_code, 200)

if __name__ == '__name__':
    unittest.main()
