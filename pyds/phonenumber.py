#! -*- coding: utf-8 -*-
# Definition of phone number in USA format: (xxx) xxx-xxxx

class PhoneNumber(object):

    def __init__(self, number):
        self.area_code = number[1:4]    # 3-digit for area code
        self.exchange = number[6:9]     # 3-digit for exchange
        self.line = number[10:14]       # 4-digit line

    def __str__(self):
        return "({}) {}-{}".format(self.area_code,
                                self.exchange, self.line)