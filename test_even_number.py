import unittest
import even_number

class TestEven_numbers(unittest.TestCase):

    def test_returns_even_numbers_only(self):
        even_numbers = even_number.even_num([1, 2, 3, 4, 5, 6, 7, 8, 9, ])
        expected_even_numbers = [2, 4, 6, 8]
        self.assertEqual(expected_even_numbers, even_numbers)

if __name__=="__main__":
    unittest.main()