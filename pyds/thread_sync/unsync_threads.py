#! -*- coding: utf-8 -*- 
# Show multiple threads modifyng  shared objects

from unsync_integer import UnsynchronizedInteger
from produce_integer import ProduceInteger
from consume_integer import ConsumeInteger

# initialize integer and threads
number = UnsynchronizedInteger()
producer = ProduceInteger("Producer", number)
consumer = ConsumeInteger("Consumer", number)

print "Starting threads ...\n"

# start threads
producer.start()
consumer.start()

# wait for threads to terminate
producer.join()
consumer.join()

print "\nAll threads have terminated."