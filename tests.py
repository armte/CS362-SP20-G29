import unittest
from task import conv_endian


class TestConvEndian(unittest.TestCase):

    def test_endian1(self):
        self.assertEqual(conv_endian(954786), '0E 91 A2')

    def test_endian2(self):
        self.assertEqual(conv_endian(-954786), '-0E 91 A2')

    def test_endian3(self):
        self.assertEqual(conv_endian(954786, 'big'), '0E 91 A2')

    def test_endian4(self):
        self.assertEqual(conv_endian(954786, 'little'), 'A2 91 0E')

    def test_test5(self):
        self.assertEqual(conv_endian(954786, 'huge'), None)

    def test_test6(self):
        self.assertEqual(conv_endian(954786, ' '), None)

    def test_test7(self):
        self.assertEqual(conv_endian(-954786, 'big'), '-0E 91 A2')

    def test_test7a(self):
        self.assertEqual(conv_endian(568944, 'big'), '08 AE 70')  # odd int


if __name__ == "__main__":
    unittest.main()
