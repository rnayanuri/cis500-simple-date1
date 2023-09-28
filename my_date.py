#######################################################
# my_date
#
# Name: zzNAMEzz (replace with your name)
# Section: XX
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
 
def ordinal_date(year:int , month: int, day: int) -> int:
    """ Return the number of days elapsed since the beginning of the year, including any partial days.
        For example, the ordinal date for 1 January is 1.
        Hint: pre-compute the ordinal date for the first of each month."""
    l1 = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    l2 = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
    days = l2 if is_leap_year(year) else l1
    return days[month - 1] + day

def days_elapsed(year1: int, month1: int, day1: int, year2: int, month2: int, day2:int ) -> int:
    """ Return the number of days that have elapsed between year1-month1-day1 and year2-month2-day2.
        You may assume that year1-month1-day1 falls on or before year2-month2-day2. (In other words,
        your answer will always be >= 0.) """
    if(year1==year2):
        days1=ordinal_date(year1,month1,day1)
        days2=ordinal_date(year2,month2,day2)
        return abs(days1-days2)
    else:
        if(year1<year2):
            year1,year2=year2,year1
            month1,month2=month2,month1
            day1,day2=day2,day1
        year1Days=ordinal_date(year1,month1,day1)
        totalDaysInYear2=366 if(is_leap_year(year2)) else 365
        year2Days=totalDaysInYear2-ordinal_date(year2,month2,day2)
        daysBWyear1AndYear2=0
        for i in range(year2+1,year1):
            daysBWyear1AndYear2+=366 if(is_leap_year(i)) else 365
        return year2Days+year1Days+daysBWyear1AndYear2
        
# This is a tuple. It is immutable so that users can't accidentally modify it.
DAYS_OF_WEEK = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

def day_of_week(year: int, month: int, day: int) -> str:
    """ Return the day of the week (Sunday, Monday, Tuesday, etc.) for the given day
        Hint 1: 1 January 1753 was a Monday.
        Hint 2: Use the methods you've already written."""
    return DAYS_OF_WEEK[days_elapsed(1753,1,1,year,month,day)%7]
    
def to_str(year: int, month: int, day: int) -> str:
    """ Return this date as string of the form "Wednesday, 07 March 1833"."""
    month_list=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",  "December"]
    week_day=day_of_week(year,month,day)
    if(day<10):
        s="0"+str(day)
    else:
        s=str(day)
    result=str(week_day)+", "+s+" "+month_list[month-1]+" "+str(year)
    return result



