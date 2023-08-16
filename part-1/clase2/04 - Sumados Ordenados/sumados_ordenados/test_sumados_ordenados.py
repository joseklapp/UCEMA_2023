import ipytest
ipytest.autoconfig()
import unittest
from typing import List


class TestSumadosOrdenados(unittest.TestCase):
    @staticmethod
    def validate_sumados_ordenados(numbers, target) -> List[int]:
        return TestSumadosOrdenados.sumados_ordenados(numbers, target)

    def test_sumados_ordenados1(self):
        self.assertEqual(TestSumadosOrdenados.validate_sumados_ordenados([2, 7, 11, 15], 9), [1, 2])

    def test_sumados_ordenados2(self):
        self.assertEqual(TestSumadosOrdenados.validate_sumados_ordenados([2, 3, 4], 6), [1, 3])

    def test_sumados_ordenados3(self):
        self.assertEqual(TestSumadosOrdenados.validate_sumados_ordenados([-1, 0], -1), [1, 2])

    def test_sumados_ordenados4(self):
        self.assertEqual(TestSumadosOrdenados.validate_sumados_ordenados([3, 3], 6), [1, 2])

if __name__ == '__main__':
    unittest.main()