import unittest
import even_numbers
class TestEven_numbers(unittest.TestCase):
    def test_accepts_list_of_numbers(self):
        result = even_numbers.is_even_num([2,4,6,8], even_numbers([1,2,3,4,5,6,7,8,9]))
        self.assertEqual(list_of_numbers_only, result)

    def test_returns_even_numbers_only(self):
        result = even_numbers.is_even_num([2,4,6,8,], even_numbers([1,2,3,4,5,6,7,8,9,]))
        self.assertEqual([2,4,6,8], result)


if __name__=="__main__":
    unittest.main()