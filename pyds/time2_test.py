#! -*- coding: utf-8 -*-

from time_mod import Time


def print_time_values(time_object):
    print time_object.military_time()
    print time_object.standard_time()

def main():
    time1 = Time()
    time2 = Time(2)
    time3 = Time(21,34)
    time4 = Time(12, 25, 42)

    print "\nall arguments defaulted: "
    print_time_values(time1)
    
    print "\nhour specified; minute and second defaulted: "
    print_time_values(time2)
    
    print "\nhour and minute specified; second defaulted: "
    print_time_values(time3)

    print "\nhour, minute and second specified: "
    print_time_values(time4)


if __name__ == "__main__":
    main()
