#! -*- coding: utf-8 -*-
# Using a semaphore to control access to a critical section

import threading
import random
import time


class SemaphoreThread( threading.Thread ):

    available_tables = ["A", "B", "C", "D", "E"]

    def __init__(self, thread_name, semaphore):
        pass
