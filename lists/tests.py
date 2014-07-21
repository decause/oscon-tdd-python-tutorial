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
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)
