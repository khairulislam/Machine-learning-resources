import holidays
import datetime
# Select country
us_holidays = holidays.US(years=[2018])

# If it is a holidays then it returns True else False
print('01-01-2018' in us_holidays)
print('02-01-2018' in us_holidays)

# What holidays is it?
print(us_holidays.get('01-01-2018'))
print(us_holidays.get('02-01-2018'))


# using pandas
from pandas.tseries.holiday import USFederalHolidayCalendar
holidays = USFederalHolidayCalendar().holidays(start='2014-01-01', end='2014-12-31').to_pydatetime()
if datetime.datetime(year=2014, month=1,  day=1) in holidays:
    print(True)