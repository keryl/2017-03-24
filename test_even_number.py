import unittest
import even_number

class TestEven_numbers(unittest.TestCase):

    def test_returns_even_numbers_only(self):
        even_numbers = even_number.even_num([1, 2, 3, 4, 5, 6, 7, 8, 9 ])
        expected_even_numbers = [2, 4, 6, 8]
        self.assertEqual(expected_even_numbers, even_numbers)

    def test_list_should_have_numbers_only(self):
        result = even_number.even_num(["1", "abcf", 3, 4, 5, 6, "type", 8, 9, ])
        self.assertEqual("some elements in your list are not numbers", result)

    def test_if_argument_is_not_a_list(self):

        # should return error if argument is a boolean
        result = even_number.even_num(True)
        self.assertEqual("argument passed is not a list of numbers", result)

        # should return error if argument is a string
        result = even_number.even_num("test")
        self.assertEqual("argument passed is not a list of numbers", result)

        # should return error if argument is a number
        result = even_number.even_num(1234)
        self.assertEqual("argument passed is not a list of numbers", result)

        # dictionary
        result = even_number.even_num({})
        self.assertEqual("argument passed is not a list of numbers", result)

if __name__=="__main__":
    unittest.main()