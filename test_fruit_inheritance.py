import unittest
import inheritance

class TestInheritance(unittest.TestCase):
    def test_food_instance(self):
        orange = Food("orange")
        self.assertIsInstance(Orange, Food, msg="The object should be an instance of the 'Food' class")

    def test_object_type(self):
        orange = Food("orange")
        self.assertTrue((type(Orange) is Food), msg="The object should be a type of `Food`")

if __name__=="__main__":
    unittest.main()