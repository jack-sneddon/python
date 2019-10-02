import unittest

class TestRegex(unittest.TestCase):
    def test_None (self, match_object, search_string):
        self.assertIsNone(match_object, f"Expected match to be 'NONE'")
        print(f"==>Pass: {search_string} == 'NONE'")

    def test_full_match_found(self, match_object, search_string) :
        print(match_object.group(0))
        print(search_string)
        # self.assertEqual(match_object.groups(0), search_string, f"Full match failure for {search_string}")

    def test_match_found(self, match_object) :
        print(match_object.group(0))
        self.assertIsNotNone(match_object)
