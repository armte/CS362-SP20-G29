import unittest
from conv_num import conv_num

class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)

class TestConvNum(unittest.TestCase):

    def test1(self):
        val = ''
        expected = None
        self.assertEqual(conv_num(val), expected)

    def test2(self):
        val = '10'
        expected = 10
        self.assertEqual(conv_num(val), expected)

    def test3(self):
        val = '10.0'
        expected = 10.0
        self.assertEqual(conv_num(val), expected)


if __name__ == "__main__":
    unittest.main()
