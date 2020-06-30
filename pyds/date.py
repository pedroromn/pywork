#! -*- coding: utf-8 -*- 
# Definition of class Date


class Date(object):

    # class attribute lists number of day in each month
    days_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, month, day, year):
        if 0 < month <= 12:
            self.month = month
        else:
            raise ValueError, "Invalid value for month: {}".format(month)
        if year >= 0:
            self.year = year
        else:
            raise ValueError, "Invalid value for year: {}".format(year)
        self.day = self.check_day(day)      # validate day
        print "Date constructor: {}".format(self.display())

    def __del__(self):
        print "Date object about to be destroyed: {}".format(self.display())

    def display(self):
        return "{}/{}/{}".format(self.month, self.day, self.year)

    def check_day(self, test_day):
        if 0 < test_day <= Date.days_month[self.month]:
            return test_day
        elif self.month == 2 and test_day == 29 and \
            (self.year % 400 == 0 or
            self.year % 100 != 0 and self.year % 4 == 0):
            return test_day
        else:
            raise ValueError, "Invalid day: {} for month {}".format(
                self.day, self.month)



