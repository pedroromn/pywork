# ! -*- coding: utf-8 -*-


class Time(object):
    
    def __init__(self):
        self._hour = 0      # 0-23
        self._minute = 0    # 0-59
        self._second = 0    # 0-59

    def setTime(self, hour, minute, second):
        self.setHour(hour)
        self.setMinute(minute)
        self.setSecond(second)

    def setHour(self, hour):
        if 0 <= hour < 24:
            self._hour = hour
        else:
            raise ValueError, "Invalid hour value {}".format(hour)

    def setMinute(self, minute):
        if 0 <= minute < 60:
            self._minute = minute
        else:
            raise ValueError, "Invalid minute value {}".format(minute)

    def setSecond(self, second):
        if 0 <= second < 60:
            self._second = second
        else:
            raise ValueError, "Invalid second value {}".format(second)

    def getHour(self):
        return self._hour

    def getMinute(self):
        return self._minute

    def getSecond(self):
        return self._second

    def military_time(self):
        return "{:02}:{:02}:{:02}".format(self._hour, self._minute, self._second)

    def standard_time(self):
        standard_time = ""

        if self._hour == 0 or self._hour == 12:
            standard_time += "12:"
        else:
            standard_time += "{:02}".format(self._hour % 12)

        standard_time += ":{:02}:{:02}".format(self._minute, self._second)

        if self._hour < 12:
            standard_time += " AM"
        else:
            standard_time += " PM"

        return standard_time   