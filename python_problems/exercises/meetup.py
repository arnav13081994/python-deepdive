# MIT Licensed
# https://github.com/exercism/python/blob/master/LICENSE
from calendar import day_name


def weekdays_in_month(year, month, weekday):
    """Return list of all 4/5 dates with given weekday and year/month."""


def meetup_day(year, month, weekday, nth):
    weekday_names = list(day_name)
    shift_by = {'1st': 0, '2nd': 1, '3rd': 2, '4th': 3, '5th': 4, 'last': -1}
    dates = weekdays_in_month(year, month, weekday_names.index(weekday))
    if nth == 'teenth':
        return next(d for d in dates if d.day > 12)
    else:
        return dates[shift_by[nth]]
