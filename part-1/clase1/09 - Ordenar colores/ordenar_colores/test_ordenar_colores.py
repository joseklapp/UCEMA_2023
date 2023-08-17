import ipytest
ipytest.autoconfig()
import unittest


class TestOrdenarColores(unittest.TestCase):
    @staticmethod
    def validar_ordenar_colores(nums) -> bool:
        raise NotImplementedError("Debes realizar la implementacion de la funcion!")

    def test_ordenar_colores1(self):
        nums = [2, 0, 2, 1, 1, 0]
        TestOrdenarColores.validar_ordenar_colores(nums)
        self.assertEqual(nums, [0, 0, 1, 1, 2, 2])

    def test_ordenar_colores2(self):
        nums = [2, 0, 1]
        TestOrdenarColores.validar_ordenar_colores(nums)
        self.assertEqual(nums, [0, 1, 2])

    def test_ordenar_colores3(self):
        nums = [0]
        TestOrdenarColores.validar_ordenar_colores(nums)
        self.assertEqual(nums, [0])


if __name__ == '__main__':
    unittest.main()