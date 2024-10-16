"""Sample tests"""

from django.test import SimpleTestCase

from app import calc

def test_calc(SimpleTestCase):
    """Test the Calc module"""

    def test_add(self):
        """Test Add method"""

        res = calc.add(2, 2)

        self.assertEqual(res, 4)
        