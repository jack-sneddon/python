import unittest
from name_function import get_full_name

# inheritance from TestCase
class NameTestCase(unittest.TestCase):
    """
    Tests for 'name_funtion.py'.

        Each test is a targeted check
        Asserts are the key to validation

    """

    def test_first_last_middle_name(self):
        """Do names like 'Johnny Lee Hooker' work?"""
        formatted_name = get_full_name('johnny', 'hooker', 'lee')
        # assert the expected value
        self.assertEqual(formatted_name, 'Johnny Lee Hooker')

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_full_name('janis', 'joplin')
        # assert the expected value
        self.assertEqual(formatted_name, 'Janis Joplin')


if __name__ == '__main__':
    unittest.main()
