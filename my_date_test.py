import unittest
import my_date

class MyDateTest(unittest.TestCase):

    def test_is_leap_year1(self):
        self.assertTrue(my_date.is_leap_year(1984))

    def test_is_leap_year2(self):
        self.assertFalse(my_date.is_leap_year(1985))

if __name__ == '__main__':
    unittest.main()