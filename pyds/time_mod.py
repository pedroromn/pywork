# ! -*- coding: utf-8 -*-


class Time(object):
    
    def __init__(self, hour=0, minute=0, second=0):
        self.setTime( hour, minute, second )

    def setTime(self, hour, minute, second):
        self.setHour(hour)
        self.setMinute(minute)
        self.setSecond(second)

    def setHour(self, hour):
        if 0 <= hour < 24:
            self.__hour = hour
        else:
            raise ValueError, "Invalid hour value {}".format(hour)

    def setMinute(self, minute):
        if 0 <= minute < 60:
            self.__minute = minute
        else:
            raise ValueError, "Invalid minute value {}".format(minute)

    def setSecond(self, second):
        if 0 <= second < 60:
            self.__second = second
        else:
            raise ValueError, "Invalid second value {}".format(second)

    def getHour(self):
        return self.__hour

    def getMinute(self):
        return self.__minute

    def getSecond(self):
        return self.__second

    def military_time(self):
        return "{:02}:{:02}:{:02}".format(self.__hour, self.__minute, self.__second)

    def standard_time(self):
        standard_time = ""

        if self.__hour == 0 or self.__hour == 12:
            standard_time += "12:"
        else:
            standard_time += "{:02}:".format(self.__hour % 12)

        standard_time += "{:02}:{:02}".format(self.__minute, self.__second)

        if self.__hour < 12:
            standard_time += " AM"
        else:
            standard_time += " PM"

        return standard_time   