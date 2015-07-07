import unittest
from kata_code import kata_v1 as kata

class TestCode(unittest.TestCase):
    def test_pass(self):
        self.assertEqual(0, kata())

    def test_fail(self):
        self.assertEqual(1, kata())

if __name__ == '__main__':
    unittest.main()
