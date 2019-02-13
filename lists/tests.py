from django.test import TestCase

# Create your tests here.

# Silly test to see if everything works fine
class SmokeTest(TestCase):

    def test_bad_maths(self):
        self.assertEqual(1+1, 3)   
