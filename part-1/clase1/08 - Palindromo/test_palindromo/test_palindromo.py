import ipytest
ipytest.autoconfig()
import unittest


class TestPalindromoString(unittest.TestCase):
    @staticmethod
    def validar_palindromo_string(s: str) -> int:
        raise NotImplementedError("Debes realizar la implementacion de la funcion!")

    def test_palindromo_string1(self):
        self.assertEqual(TestPalindromoString.validar_palindromo_string("aabca"), 3)

    def test_palindromo_string2(self):
        self.assertEqual(TestPalindromoString.validar_palindromo_string("abcdabcdabcd"), 10)

    def test_palindromo_string3(self):
        self.assertEqual(TestPalindromoString.validar_palindromo_string("aabb"), 4)


if __name__ == '__main__':
    unittest.main()