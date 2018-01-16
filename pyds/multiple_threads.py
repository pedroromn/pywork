#! -*- coding: utf-8 -*-
# Show multiple threads printing at different intervals

import threading
import random
import time


class PrintThread( threading.Thread ):

    def __init__(self, thread_name):
        threading.Thread.__init__(self, name=thread_name)
        self.sleep_time = random.randrange(1, 6)
        print "Name: {}; sleep: {}".format(self.getName(), self.sleep_time)

    # Overridden Thread run method
    def run(self):
        print "{} going to sleep".format(self.getName())
        time.sleep(self.sleep_time)
        print "{} done sleeping".format(self.getName())

def main():
    thread1 = PrintThread("thread1")
    thread2 = PrintThread("thread2")
    thread3 = PrintThread("thread3")
    thread4 = PrintThread("thread4")
    thread5 = PrintThread("")

    print "\nStarting threads\n"

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()

    print "\nThreads started\n"


if __name__ == "__main__":
    main()

