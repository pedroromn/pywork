#! -*- coding: utf-8 -*-
# Unsynchronized acces to an integer

import threading 


class UnsynchronizedInteger(object):

    def __init__(self):
        self.sharedNumber = -1

    def setSharedNumber(self, new_number):
        #global new_number
        print "{} setting sharedNumber to {}".format(
            threading.currentThread().getName(),
            newNumber)
        self.sharedNumber = new_number

    def getSharedNumber(self):
        temp_number = self.sharedNumber
        print "{} retrieving sharedNumber value {}".format(
            threading.currentThread().getName(),
            temp_number
        )
        return temp_number