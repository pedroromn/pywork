#! -*- coding: utf-8 -*-

import random
import time
from threading import Thread


class SleepyThread(Thread):
    
    def __init__(self, number, sleep_max):
        Thread.__init__(self, name="Thread "+str(number))
        self._sleep_interval = random.randint(1, sleep_max)

    def run(self):
        print "%s, sleep interval: %d seconds\n" % \
                (self.getName(), self._sleep_interval)
        time.sleep(self._sleep_interval)
        print "%s waking up \n" % self.getName()


def main():
    num_threads = input("Enter the number of threads: ")
    sleep_max = input("Enter the maximum sleep time: ")
    thread_list = []
    for count in xrange(num_threads):
        thread_list.append(SleepyThread(count + 1, sleep_max))
    for thread in thread_list:
        thread.start()


if __name__ == "__main__":
    main()