#! -*- coding:utf-8 -*-

from __future__ import print_function

class Time1(object):

    def set_time(self, hour, minute, second):
        if (hour < 0 or hour >= 24 or minute < 0 or minute >= 60 or
        second < 0 or second >= 60):
            raise ValueError("hour, minute and/or second was out of range")
        self._hour = hour
        self._minute = minute
        self._second = second

    def to_universal_string(self):
        return "{:02d}:{:02d}:{:02d}".format(self._hour,
                                             self._minute,
                                             self._second)

    def to_string(self):
        h = 12 if (self._hour == 0 or self._hour == 12) else self._hour % 12
        x = "AM" if (self._hour < 12) else "PM"
        return "{:d}:{:02d}:{:02d} {ind}".format(h,
                                                 self._minute,
                                                 self._second,
                                                 ind=x)
