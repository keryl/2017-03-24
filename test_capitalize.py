import unittest
from capitalize import capitalize

class TestCapitalize(unittest.TestCase):

    def test_it_capitalizes_strings(self):
        self.assertEqual('ABCD', capitalize('abcD'))

    def test_it_does_not_capitalize_non_strings(self):
        self.assertEqual('argument should be of type string', capitalize(1))
        self.assertEqual('argument should be of type string', capitalize(True))
        self.assertEqual('argument should be of type string', capitalize([]))
        self.assertEqual('argument should be of type string', capitalize({}))

if __name__=="__main__":
    unittest.main()
