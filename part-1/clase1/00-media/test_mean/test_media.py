import ipytest
ipytest.autoconfig()
import unittest



import unittest

class TestCalculateMean(unittest.TestCase):
    @staticmethod
    def calculate_mean(arr):
        ''' calcula la media de una array sin usar librerias'''
        return sum(arr)/len(arr)

    def test_calculo_12345(self):
        self.assertEqual(TestCalculateMean.calculate_mean([1, 2, 3, 4, 5]), 3.0)

    def test_calculo_123410(self):
        self.assertEqual(TestCalculateMean.calculate_mean([1, 2, 3, 4, 10]), 4.0)

    def test_calculo_101(self):
        self.assertEqual(TestCalculateMean.calculate_mean([-1, 0, 1]), 0.0)

if __name__ == "__main__":
    unittest.main()


