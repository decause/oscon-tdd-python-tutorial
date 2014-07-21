from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

# Create your tests here.

#class SmokeTest(TestCase):
#    def test_bad_maths(self):
#        self.assertEqual(2 + 2, 5)

class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
