import unittest
import sys
#when using python to run tests this is needed
sys.path.insert(0, '/home/ludaone/andela/book-a-meal')

from app.api import app
import json

class BamApiTestCase(unittest.TestCase):

    def setup(self):
        app.testing = True
        self.apiApp = app.test_client()

    # Basic test for a status 200 on index route
    def test_index(self):
        response = self.apiApp.get('/')
        result = json.loads(response.data)

        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
