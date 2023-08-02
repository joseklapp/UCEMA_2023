import ipytest
ipytest.autoconfig()
import unittest


class TestSumEvery(unittest.TestCase):
    @staticmethod
    def sum_every(*args):
        total = 0
        for one_number in args:
            total += one_number
        return total

    def test_sum_empty(self):
        self.assertEqual(TestSumEvery.sum_every(), 0)

    def test_sum_single_value(self):
        self.assertEqual(TestSumEvery.sum_every(5), 5)

    def test_sum_two_values(self):
        self.assertEqual(TestSumEvery.sum_every(2, 3), 5)

    def test_sum_multiple_values(self):
        self.assertEqual(TestSumEvery.sum_every(1, 2, 3, 4, 5), 15)

    def test_sum_negative_values(self):
        self.assertEqual(TestSumEvery.sum_every(-1, -2, -3), -6)


if __name__ == "__main__":
    unittest.main()