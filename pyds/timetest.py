#! -*- coding: utf-8 -*-
# Driver to test class Time

from time_mod import Time

def main():
    time = Time()
    print "The initial military time is:  ", time.military_time()
    print "time set to (13, 27, 6)"
    time.setTime(13,27,6)
    print "Military Time: ", time.military_time()
    print "Standard Time: ", time.standard_time() 

if __name__ == "__main__":
    main() 