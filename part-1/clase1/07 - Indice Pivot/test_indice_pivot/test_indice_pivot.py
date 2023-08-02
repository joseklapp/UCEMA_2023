import ipytest
ipytest.autoconfig()
import unittest


class TestPivotIndex(unittest.TestCase):
    @staticmethod
    def validar_indice(nums) -> bool:
        raise NotImplementedError("Debes realizar la implementacion de la funcion!")

    def test_pivot_index1(self):
        self.assertEqual(TestPivotIndex.validar_indice([1, 7, 3, 6, 5, 6]), 3)

    def test_pivot_index2(self):
        self.assertEqual(TestPivotIndex.validar_indice([1, 2, 3]), -1)

    def test_pivot_index3(self):
        self.assertEqual(TestPivotIndex.validar_indice([-1, -1, -1, 0, 1, 1]), 0)



if __name__ == '__main__':
    unittest.main()