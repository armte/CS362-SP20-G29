import unittest
from task import conv_endian


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertEqual(conv_endian(954786),'0E 91 A2')

    def test2(self):
        self.assertEqual(conv_endian(-954786),'-0E 91 A2')

    def test3(self):
        self.assertEqual(conv_endian(954786, 'big'),'0E 91 A2')

    def test4(self):
        self.assertEqual(conv_endian(954786, 'little'),'A2 91 0E')

    def test5(self):
        self.assertEqual(conv_endian(954786, 'huge'),'None')

    def test6(self):
        self.assertEqual(conv_endian(954786, ' '),'None')

if __name__ == "__main__":
    unittest.main()
