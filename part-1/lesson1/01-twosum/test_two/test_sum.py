import ipytest
ipytest.autoconfig()
import unittest



class TestTwoSum(unittest.TestCase):
    @staticmethod
    def two_sum(nums, target):
        raise NotImplementedError("You need to provide your own implementation of `two_sum`!")

    def test_two_sum1(self):
        self.assertEqual(TestTwoSum.two_sum([2,7,11,15], 9), [0,1])

    def test_two_sum2(self):
        self.assertEqual(TestTwoSum.two_sum([3,2,4], 6), [1,2])

    def test_two_sum3(self):
        self.assertEqual(TestTwoSum.two_sum([3,3], 6), [0,1])



