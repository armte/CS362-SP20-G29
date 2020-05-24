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
        val = '12345'
        expected = 12345
        self.assertEqual(conv_num(val), expected)

    def test3(self):
        val = '123.45'
        expected = 123.45
        self.assertEqual(conv_num(val), expected)

    def test4(self):
        val = '.45'
        expected = 0.45
        self.assertEqual(conv_num(val), expected)

    def test5(self):
        val = '123.'
        expected = 123.0
        self.assertEqual(conv_num(val), expected)

    def test6(self):
        val = '0xAD4'
        expected = 2772
        self.assertEqual(conv_num(val), expected)


if __name__ == "__main__":
    unittest.main()
