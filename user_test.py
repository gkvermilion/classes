import unittest
from super_duper_user import *

file = 'ura'
class TestUserCase(unittest.TestCase):

    def test_setting(self):
        test_file = set_file(file)
        self.assertEqual(test_file, 'users/ura.json')

    def test_getting(self):
        test_file = get_stored_name(file)
        self.assertEqual(test_file, 'dhdh')

    def test_none_getting(self):
        none_file = 'none'
        test_file = get_stored_name(none_file)
        self.assertIsNone(test_file)



if __name__ == '__main__':
    unittest.main()
