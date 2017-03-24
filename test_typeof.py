import unittest
import t

class TypeofTestCaseTest(unittest.TestCase):

    def test_it_works(self):
        self.assertEqual('string', t.typeof("abcd"))
        self.assertEqual('number', t.typeof(1))
        self.assertEqual('number', t.typeof(1.1))
        self.assertEqual('array', t.typeof([]))
        self.assertEqual('dict', t.typeof({}))
        self.assertEqual('unknown', t.typeof(False))

if __name__ == '__main__':
    unittest.main()