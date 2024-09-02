from django.test import TestCase, Client

import bs4

# Create your tests here.
class TestUrls(TestCase):

    def test_django_hide_form_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'name')

    def test_django_hide_form_view_post_without_csrf_header(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        cookies = response.cookies

        client = Client(enforce_csrf_checks=True)
        for cookie_name, cookie_value in cookies.items():
            client.cookies[cookie_name] = cookie_value.value

        response = client.post('/', {'name': 'test'})
        self.assertEqual(response.status_code, 403)
    
    def test_django_hide_form_view_post_with_django_hide_csrf(self):
        # Step 1: Perform GET request to retrieve the form with the CSRF token
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
        # Step 2: Extract the CSRF token and its name from the form
        soup = bs4.BeautifulSoup(response.content, 'html.parser')
        csrf_token_input = soup.find('input', {'type': 'hidden'})
        csrf_token = csrf_token_input.get('value')
        csrf_token_name = csrf_token_input.get('name')

        # Step 3: Capture the cookies set by the server during the GET request
        cookies = response.cookies

        # Step 4: Create a new client with enforced CSRF checks
        client = Client(enforce_csrf_checks=True)
        
        # Step 5: Set the cookies from the GET request into the new client
        for cookie_name, cookie_value in cookies.items():
            client.cookies[cookie_name] = cookie_value.value

        # Step 6: Perform POST request using the correct token and name
        post_data = {'name': 'test', csrf_token_name: csrf_token}
        response = client.post('/', post_data)
        
        # Step 7: Assert that the response status code is 200 (success)
        self.assertEqual(response.status_code, 200)
    
