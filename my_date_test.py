import unittest
import my_date


class TestIsLeapYear(unittest.TestCase):

    def test_year_divisible_by_4(self):
        self.assertTrue(is_leap_year(2024))
        self.assertTrue(is_leap_year(2012))
        self.assertTrue(is_leap_year(1996))

    def test_year_divisible_by_100_but_not_400(self):
        self.assertFalse(is_leap_year(1900))
        self.assertFalse(is_leap_year(1800))
        self.assertFalse(is_leap_year(1700))

    def test_year_divisible_by_400(self):
        self.assertTrue(is_leap_year(2000))
        self.assertTrue(is_leap_year(1600))
        self.assertTrue(is_leap_year(1200))

    def test_year_not_divisible_by_4(self):
        self.assertFalse(is_leap_year(2023))
        self.assertFalse(is_leap_year(2013))
        self.assertFalse(is_leap_year(1997))

if __name__ == '__main__':
    unittest.main()