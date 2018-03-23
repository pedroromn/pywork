#! -*- coding: utf-8 -*-
# Using a semaphore to control access to a critical section

import threading
import random
import time


class SemaphoreThread( threading.Thread ):

    available_tables = ["A", "B", "C", "D", "E"]

    def __init__(self, thread_name, semaphore):
        """ Initialize thread """
        threading.Thread.__init__(self, name = thread_name)
        self.sleep_time = random.randrange(1, 6)

        # set the semaphore as a data attribute of the class
        self.thread_semaphore = semaphore

    def run(self):
        """ Print message and release semaphore """

        # acquire the semaphore
        self.thread_semaphore.acquire()

        # remove a table from the list
        table = SemaphoreThread.available_tables.pop()

        print "{} entered; seated at table {}".format(
            self.getName(), table)
        print SemaphoreThread.available_tables

        time.sleep( self.sleep_time )   # enjoy a meal

        # free a table
        print " {} exiting; freeing table {}".format(
            self.getName(), table),
        SemaphoreThread.available_tables.append(x)

