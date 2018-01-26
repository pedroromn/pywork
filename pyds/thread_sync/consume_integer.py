#! -*- coding: utf-8 -*-
# Class that consumes integer

import threading
import random
import time


class ConsumeInteger( threading.Thread ):

    def __init__(self, name_thread, shared_object):
        threading.Thread.__init__(self, name = name_thread)
        self.sharedObject = shared_object

    def rum(self):
        sum = 0         # total sum of consumed values

        for i in range(10):
            time.sleep( random.randrange(4) )
            sum += self.sharedObject.getSharedNumber()

        print "{} retrieved values totaling: {}".format(self.getName, sum)
        print "Terminating ", self.getName()


    