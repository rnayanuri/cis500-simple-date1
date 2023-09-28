import unittest
import my_date 

class MyDateTest(unittest.TestCase):

    def test_year_divisible_by_4(self):
        self.assertTrue(my_date.is_leap_year(2024))
        self.assertTrue(my_date.is_leap_year(2012))
        self.assertTrue(my_date.is_leap_year(1996))

    def test_year_divisible_by_100_but_not_400(self):
        self.assertFalse(my_date.is_leap_year(1900))
        self.assertFalse(my_date.is_leap_year(1800))
        self.assertFalse(my_date.is_leap_year(1700))

    def test_year_divisible_by_400(self):
        self.assertTrue(my_date.is_leap_year(2000))
        self.assertTrue(my_date.is_leap_year(1600))
        self.assertTrue(my_date.is_leap_year(1200))

    def test_year_not_divisible_by_4(self):
        self.assertFalse(my_date.is_leap_year(2023))
        self.assertFalse(my_date.is_leap_year(2013))
        self.assertFalse(my_date.is_leap_year(1997))


    def test_january_1(self):
        self.assertEqual(my_date.ordinal_date(2023, 1, 1), 1)

    def test_february_15_non_leap(self):
        self.assertEqual(my_date.ordinal_date(2023, 2, 15), 46)

    def test_february_15_leap(self):
        self.assertEqual(my_date.ordinal_date(2024, 2, 15), 46)

    def test_december_31_non_leap(self):
        self.assertEqual(my_date.ordinal_date(2023, 12, 31), 365)

    def test_december_31_leap(self):
        self.assertEqual(my_date.ordinal_date(2024, 12, 31), 366)

    def test_february_29_leap(self):
        self.assertEqual(my_date.ordinal_date(2024, 2, 29), 60)

    def test_year_2023_month_1_day_1_to_year_2023_month_1_day_2(self):
        self.assertEqual(my_date.days_elapsed(2023, 1, 1, 2023, 1, 2), 1)

    def test_year_2023_month_1_day_1_to_year_2023_month_12_day_31(self):
        self.assertEqual(my_date.days_elapsed(2023, 1, 1, 2023, 12, 31), 364)

    def test_year_2000_month_1_day_1_to_year_2000_month_12_day_31(self):
        self.assertEqual(my_date.days_elapsed(2000, 1, 1, 2000, 12, 31), 365)

    def test_year_2020_month_2_day_29_to_year_2020_month_2_day_29(self):
        self.assertEqual(my_date.days_elapsed(2020, 2, 29, 2020, 2, 29), 0)

    def test_day_of_week1(self):
        self.assertEqual('Wednesday', my_date.day_of_week(2023, 9, 27))


    def test_ordinal_date_2023_month_1_day_1(self):
        self.assertEqual(my_date.ordinal_date(2023, 1, 1), 1)

    def test_ordinal_date_2023_month_9_day_26(self):
        self.assertEqual(my_date.ordinal_date(2023, 9, 26), 269)

    def test_ordinal_date_2024_month_2_day_29(self):
        self.assertEqual(my_date.ordinal_date(2024, 2, 29), 60)


    def test_year_2023_month_9_day_26(self):
        self.assertEqual(my_date.to_str(2023, 9, 26), "Tuesday, 26 September 2023")


    def test_year_2000_month_12_day_31(self):
        self.assertEqual(my_date.to_str(2000, 12, 31), "Sunday, 31 December 2000")
    def test_year_2023_month_9_day_26(self):
        self.assertEqual(my_date.to_str(2023, 9, 26), "Tuesday, 26 September 2023")
    def test_year_2000_month_12_day_31(self):
        self.assertEqual(my_date.to_str(2000, 12, 31), "Sunday, 31 December 2000")



if __name__ == '__main__':
    unittest.main()

