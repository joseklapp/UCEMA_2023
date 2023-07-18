import ipytest
ipytest.autoconfig()
import unittest



class TestContainsDuplicate(unittest.TestCase):
    @staticmethod
    def contains_duplicate(nums) -> bool:
        raise NotImplementedError("You need to provide your own implementation of `contains_duplicate`!")

    def test_contains_duplicate1(self):
        self.assertEqual(TestContainsDuplicate.contains_duplicate([1, 2, 3, 4, 5]), False)

    def test_contains_duplicate2(self):
        self.assertEqual(TestContainsDuplicate.contains_duplicate([1, 2, 3, 4, 1]), True)

    def test_contains_duplicate3(self):
        self.assertEqual(TestContainsDuplicate.contains_duplicate([1, 1, 1, 1, 1]), True)




