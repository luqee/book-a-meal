import unittest
import sys
#when using python to run tests this is needed
# sys.path.insert(0, '/home/ludaone/andela/book-a-meal')

from app import app
import json

class BamApiTestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.user = {"username":"luke", "email":"luke@gmail.com","password":"12345"}
        self.meal_option = {'name': 'Fish & chips'}
        self.meal_option_list = [{'name': 'Ugali & nyama'}, {'name': 'chapati dunga'}]
        self.selected_meal_option_list = [{'name': 'chapati dunga'}]


    def test_user_signup(self):
        """Test for user sign up.

        This test checks in the response for message and user id keys.
        """
        response = self.app.post('api/v1/auth/signup', data = json.dumps(self.user) , content_type = 'application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201)
        self.assertTrue(result["message"] == "Successfull signup")


    def test_user_login(self):
        """Test for user login in.

        This test checks for a successful login by inspecting the status code and
        a key 'message'.
        """
        response = self.app.post('api/v1/auth/login', data = json.dumps({'username': self.user['username'], 'password': self.user['password']}) , content_type = 'application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["message"] ==  "Successfull login")

    def test_add_meal_option(self):
        """Test add meal option functionality .

        This test checks for a successful addition of a meal item by inspecting
        the status code and a key 'meal_opt_id'.
        """
        response = self.app.post('api/v1/meals/', data = json.dumps(self.meal_option) , content_type = 'application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result['message'] ==  'Successfull addition')

    def test_get_meal_option(self):
        """Test get meal option functionality .

        This test checks if the app can successfully retrieve meal optoins by inspecting
        the status code and a key 'meals'.
        """
        response = self.app.get('api/v1/meals/')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(type(result['meals']) == list)

    def test_update_meal_option(self):
        """Test meal option editing functionality .

        This test checks if the app can successfully update meal optoins by inspecting
        the status code and a key 'message'.
        """
        response = self.app.put('api/v1/meals/<mealId>', data={}, content_type = 'application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201)
        self.assertTrue(type(result['message']) == str)
        self.assertEqual(result['message'], 'Successful update')

    def test_delete_meal_option(self):
        """Test meal option deleting functionality .

        This test checks if the app can successfully remove a meal optoin
         by inspecting the status code and the keys 'message' and 'message_id'.
        """
        response = self.app.delete('api/v1/meals/<mealId>')# ?? placeholder for now
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201)
        self.assertTrue(type(result['message']) == str)
        self.assertEqual(result['message'], 'Successful removal')
        self.assertTrue(type(result['message_id']) == int)

    def test_set_menu(self):
        """Test for successful menu creation .

        This test checks for a result status of 200 and checks for a key 'message'.
        """
        response = self.app.post('api/v1/menu', data = json.dumps(self.meal_option_list) , content_type = 'application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['message'], 'Successfull setting of menu')

    def test_get_menu(self):
        """Test get menu functionality.

        This test checks for a result status of 200 and inspects various keys.
        """
        response = self.app.get('api/v1/menu')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(result['menu']), list)

    def test_order_from_meal_option(self):
        """Test for successful meal option selection.

        This test checks for successful selection
        of a meal_option from the menu by chcking for a result
        status of 200 and checks for a key 'message'.
        """
        response = self.app.post('api/v1/orders', data = json.dumps(self.selected_meal_option_list) , content_type = 'application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['message'], 'Order Successfully placed')

    def test_modify_order(self):
        """Test order editing functionality .

        This test checks if a user can successfully update
        their order by inspecting the status code and a key 'message'.
        """
        response = self.app.put('api/v1/orders/<orderId>', data = json.dumps(self.selected_meal_option_list), content_type = 'application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201)
        self.assertTrue(type(result['message']) == str)
        self.assertEqual(result['message'], 'Successful modification')

    def test_get_all_orders(self):
        """Test get orders functionality .

        This test checks if the admin can successfully retrieve
        all orders by inspecting the status code and checking for valid data.
        """
        response = self.app.get('api/v1/orders')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(type(result['orders']) == list)

if __name__ == '__main__':
    unittest.main()
