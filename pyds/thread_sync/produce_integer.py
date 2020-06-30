#! -*- coding: utf-8 -*-
# Class that produces integer

import threading
import random
import time


class ProduceInteger( threading.Thread ):

    def __init__(self, thread_name, sharedObject):
        threading.Thread.__init__(self, name = thread_name)
        self.sharedObject = sharedObject

    def run(self):
        for i in range(1,11):
            time.sleep( random.randrange(4) )
            self.sharedObject.setSharedNumber(i)

        print self.getName(), "finished producing values"
        print "Terminating ", self.getName()
    
