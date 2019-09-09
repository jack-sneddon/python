import unittest
from name_function import get_formatted_name

"""
Common Assert methods:
    assertEqual(a, b) --> verify that a==b
    assertNotEqual(a, b) --> verify that a!=b
    assertTrue(x)
    assertFalse(x)
    assertIn(item, list)
    assertNotIn(item, list)
"""


# inheritance from TestCase
class NameTestCase(unittest.TestCase):
    """
    Tests for 'name_funtion.py'.

        Each test is a targeted check
        Asserts are the key to validation

    """

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        # assert the expected value
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_missing_caps_name(self):
        """Do names like 'Jessie & Frank James' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        # assert the expected value
        self.assertNotEqual(formatted_name, 'janis joplin')

if __name__ == '__main__':
    unittest.main()
