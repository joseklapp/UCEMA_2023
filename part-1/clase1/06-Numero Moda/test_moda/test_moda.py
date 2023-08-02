import ipytest
ipytest.autoconfig()
import unittest
from typing import List


class TestModa(unittest.TestCase):
    @staticmethod
    def validarmoda(nums) -> bool:
        raise NotImplementedError("Debes realizar la implementacion de la funcion!")

    def test_moda1(self):
        self.assertEqual(TestModa.validarmoda([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]), 4)

    def test_moda2(self):
        self.assertEqual(TestModa.validarmoda([5, 5, 5,2, 2, 2, 2, 2, 7, 7]), 2)

    def test_moda3(self):
        self.assertEqual(TestModa.validarmoda([10, 5, 10, 3, 5, 3, 10]), 10)

    def test_moda4(self):
        self.assertEqual(TestModa.validarmoda([8, 8, 8, 8, 8, 8, 8, 8, 8, 8]), 8)


if __name__ == '__main__':
    unittest.main()