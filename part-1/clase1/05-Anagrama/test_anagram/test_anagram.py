import ipytest
ipytest.autoconfig()
import unittest



class TestValidAnagram(unittest.TestCase):
    @staticmethod
    def validaranagrama(nums) -> bool:
        raise NotImplementedError("You need to provide your own implementation of `contains_duplicate`!")

    def test_valid_anagram1(self):
        self.assertEqual(TestValidAnagram.validaranagrama("listen", "silent"), True)

    def test_triangle_integral(self):
        self.assertEqual(TestValidAnagram.validaranagrama("triangle", "integral"), True)

    def test_valid_anagram3(self):
        self.assertEqual(TestValidAnagram.validaranagrama("hello", "world"), False)

    def test_valid_anagram4(self):
        self.assertEqual(TestValidAnagram.validaranagrama("hello", "hell"), False)

if __name__ == '__main__':
    unittest.main()




