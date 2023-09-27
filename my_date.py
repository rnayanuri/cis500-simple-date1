#######################################################
# my_date
#
# Name: zzNAMEzz (Raghavendra)
# Section: 
#
# Fall 2023
#########################################################


def is_leap_year(year: int) -> bool:
    """Return True if year is a leap year, False otherwise"""
    if year % 4 != 0:
        return False
    elif year % 100 == 0 and year % 400 != 0:
        return False
    else:
        return True

 






def ordinal_date(year: int, month: int, day: int) -> int:


    def is_leap_year(year: int) -> bool:
        """Return True if year is a leap year, False otherwise."""
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    """Return the ordinal date for the given date (day number within the year)."""
    ordinal_dates_non_leap = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    ordinal_dates_leap = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
    ordinal_dates = ordinal_dates_leap if is_leap_year(year) else ordinal_dates_non_leap
    return ordinal_dates[month - 1] + day







def ordinal_date(year: int, month: int, day: int) -> int:
    def is_leap_year(year: int) -> bool:
        """Return True if year is a leap year, False otherwise."""
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    ordinal_dates_non_leap = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    ordinal_dates_leap = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
    ordinal_dates = ordinal_dates_leap if is_leap_year(year) else ordinal_dates_non_leap
    return ordinal_dates[month - 1] + day

def days_elapsed(year1: int, month1: int, day1: int, year2: int, month2: int, day2: int) -> int:
    """Return the number of days that have elapsed between two dates."""
    ordinal_date1 = ordinal_date(year1, month1, day1)
    ordinal_date2 = ordinal_date(year2, month2, day2)
    days_difference = ordinal_date2 - ordinal_date1
    
    return days_difference



# This is a tuple. It is immutable so that users can't accidentally modify it.
DAYS_OF_WEEK = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

def ordinal_date(year: int, month: int, day: int) -> int:
    def is_leap_year(year: int) -> bool:
        """Return True if year is a leap year, False otherwise."""
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    ordinal_dates_non_leap = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    ordinal_dates_leap = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
    ordinal_dates = ordinal_dates_leap if is_leap_year(year) else ordinal_dates_non_leap
    return ordinal_dates[month - 1] + day

DAYS_OF_WEEK = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

def day_of_week(year: int, month: int, day: int) -> str:

    Hint 1: 1 January 1753 was a Monday.
    Hint 2: Use the methods you've already written."""


    days_elapsed = ordinal_date(year, month, day) - ordinal_date(1753, 1, 1)


    day_of_week_index = (days_elapsed + 1) % 7


    return DAYS_OF_WEEK[day_of_week_index]
    
    
import datetime

def to_str(year: int, month: int, day: int) -> str:

    date_obj = datetime.date(year, month, day)


    day_name = date_obj.strftime("%A")


    format_date = date_obj.strftime(f"{day_name}, %d %B %Y")

    return format_date
              
    