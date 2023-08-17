import ipytest
ipytest.autoconfig()
import unittest
from typing import List


class TestBotesSalvavidas(unittest.TestCase):
    @staticmethod
    def validate_botes_salvavidas(personas, limite) -> int:
        return TestBotesSalvavidas.botes_salvavidas(personas, limite)

    def test_botes_salvavidas1(self):
        self.assertEqual(TestBotesSalvavidas.validate_botes_salvavidas([1, 2, 3, 4, 5], 5), 3)

    def test_botes_salvavidas2(self):
        self.assertEqual(TestBotesSalvavidas.validate_botes_salvavidas([3, 2, 2, 1], 4), 2)

    def test_botes_salvavidas3(self):
        self.assertEqual(TestBotesSalvavidas.validate_botes_salvavidas([5, 1, 4, 2], 6), 2)

    def test_botes_salvavidas4(self):
        self.assertEqual(TestBotesSalvavidas.validate_botes_salvavidas([5, 3, 2, 2], 7), 2)


if __name__ == '__main__':
    unittest.main()