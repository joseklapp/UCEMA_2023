# pylint: disable-all
import ipytest
ipytest.autoconfig()
import unittest


class TestAgregarComa(unittest.TestCase):
    @staticmethod
    def agregar_coma(s):
        pass  # Deberás definir esta función en tu notebook

    def test_strings_juan_pedro_seba(self):
        self.assertEqual(TestAgregarComa.agregar_coma("juan pedro seba"), "juan, pedro, seba")

    def test_strings_juan_seba_pedro(self):
        self.assertEqual(TestAgregarComa.agregar_coma("juan seba pedro"), "juan, seba, pedro")


class TestPerteneceA(unittest.TestCase):
    @staticmethod
    def pertence_a(s, word):
        pass  # Deberás definir esta función en tu notebook

    def test_include_word(self):
        self.assertEqual(TestPerteneceA.pertence_a("hey jude", "jude"), True)

    def test_do_not_include_word(self):
        self.assertEqual(TestPerteneceA.pertence_a("hey jude", "joe"), False)


class TestCuentaRep(unittest.TestCase):
    @staticmethod
    def cuenta_repetido(s, substring):
        pass  # Deberás definir esta función en tu notebook

    def test_numbers_0_0_1_2_0_on_0(self):
        self.assertEqual(TestCuentaRep.cuenta_repetido("00120", "0"), 3)

    def test_numbers_0_0_1_2_0_on_3(self):
        self.assertEqual(TestCuentaRep.cuenta_repetido("00120", "3"), 0)


class TestEsUnaPregunta(unittest.TestCase):
    @staticmethod
    def es_una_pregunta(s):
        pass  # Deberás definir esta función en tu notebook

    def test_es_una_pregunta(self):
        self.assertEqual(TestEsUnaPregunta.es_una_pregunta("How are you?"), True)

    def test_is_not_a_question(self):
        self.assertEqual(TestEsUnaPregunta.es_una_pregunta("Fine."), False)


class TestWhitespace(unittest.TestCase):
    @staticmethod
    def eliminar_espacios_exteriores(s):
        pass  # Deberás definir esta función en tu notebook

    def test_leading_whitespaces(self):
        self.assertEqual(TestWhitespace.eliminar_espacios_exteriores("  hey yo"), "hey yo")
    def test_trailing_whitespaces(self):
        """This method should work with trailing whitespaces"""
        self.assertEqual(TestWhitespace.eliminar_espacios_exteriores("hey yo  "), "hey yo")

    def test_whitespaces(self):
        """This method should work with leading and trailing whitespaces"""
        self.assertEqual(TestWhitespace.eliminar_espacios_exteriores(" hey yo  "), "hey yo")


class Testreemplazar_una_letra(unittest.TestCase):
    @staticmethod
    def reemplazar_una_letra(s, original, new):
        pass  # Deberás definir esta función en tu notebook

    def test_casanova_to_cosonovo(self):
        """This method should correctly reemplazar_una_letra the letter(s) in the string"""
        self.assertEqual(Testreemplazar_una_letra.reemplazar_una_letra("casanova", "a", "o"), "cosonovo")

    def test_kosovo_to_kasava(self):
        """This method should correctly reemplazar_una_letra the letter(s) in the string"""
        self.assertEqual(Testreemplazar_una_letra.reemplazar_una_letra("kosovo", "o", "a"), "kasava")

class TestFString(unittest.TestCase):
    @staticmethod
    def f_string_nombreyapellido(nombre, apellido, age):
        pass  # Deberás definir esta función en tu notebook

    def test_john_doe_33_formatting(self):
        """Este método debe retornar "Fede Moreno tiene 33"""
        self.assertEqual(TestFString.f_string_nombreyapellido("Fede", "Moreno", 33), "Fede Moreno tiene 33")

