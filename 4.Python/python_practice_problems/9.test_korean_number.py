from korean_0_to_100 import korean_number
import unittest


class TestKoreanNumber(unittest.TestCase):
    def test_0(self):
        self.assertEqual(korean_number(0), '영')

    def test_1(self):
        self.assertEqual(korean_number(1), '일')

    def test_2(self):
        self.assertEqual(korean_number(2), '이')


if __name__ == '__main__':
    unittest.main()
