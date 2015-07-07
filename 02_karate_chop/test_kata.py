import unittest
from kata_code import chop_v1 as chop

class TestChop(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(-1, chop(3, []))

    def test_not_found_in_array_of_1(self):
        self.assertEqual(-1, chop(3, [1]))

    def test_exists_in_array_of_1(self):
        self.assertEqual(0,  chop(1, [1]))

    def test_exists_in_array_of_3(self):
        self.assertEqual(0,  chop(1, [1, 3, 5]))
        self.assertEqual(1,  chop(3, [1, 3, 5]))
        self.assertEqual(2,  chop(5, [1, 3, 5]))

    def test_not_found_in_array_of_3(self):
        self.assertEqual(-1, chop(0, [1, 3, 5]))
        self.assertEqual(-1, chop(2, [1, 3, 5]))
        self.assertEqual(-1, chop(4, [1, 3, 5]))
        self.assertEqual(-1, chop(6, [1, 3, 5]))

    def test_exists_in_array_of_4(self):
        self.assertEqual(0,  chop(1, [1, 3, 5, 7]))
        self.assertEqual(1,  chop(3, [1, 3, 5, 7]))
        self.assertEqual(2,  chop(5, [1, 3, 5, 7]))
        self.assertEqual(3,  chop(7, [1, 3, 5, 7]))

    def test_not_found_in_array_of_4(self):
        self.assertEqual(-1, chop(0, [1, 3, 5, 7]))
        self.assertEqual(-1, chop(2, [1, 3, 5, 7]))
        self.assertEqual(-1, chop(4, [1, 3, 5, 7]))
        self.assertEqual(-1, chop(6, [1, 3, 5, 7]))
        self.assertEqual(-1, chop(8, [1, 3, 5, 7]))

if __name__ == '__main__':
    unittest.main()
