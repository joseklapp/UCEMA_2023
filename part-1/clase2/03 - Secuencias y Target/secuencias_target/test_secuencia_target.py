import ipytest
ipytest.autoconfig()
import unittest


class TestNumSubseq(unittest.TestCase):
    @staticmethod
    def validate_num_subseq(nums, target) -> int:
        return TestNumSubseq.numSubseq(nums, target)

    def test_num_subseq1(self):
        self.assertEqual(TestNumSubseq.validate_num_subseq([3, 5, 6, 7], 9), 4)

    def test_num_subseq2(self):
        self.assertEqual(TestNumSubseq.validate_num_subseq([3, 3, 6, 8], 10), 6)

    def test_num_subseq3(self):
        self.assertEqual(TestNumSubseq.validate_num_subseq([2, 3, 3, 4, 6, 7], 10), 61)

    def test_num_subseq4(self):
        self.assertEqual(TestNumSubseq.validate_num_subseq([1, 2, 3, 4, 5], 10), 32)


if __name__ == '__main__':
    unittest.main()