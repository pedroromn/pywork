#! -*- coding:utf-8 -*-

from time1 import Time1

def display_time(header, t):
    time_universal = t.to_universal_string()
    time_standard = t.to_string()
    print "{header}\nUniversal time: {tu}\nStandard time: {ts}\n".format(
        header=header,tu=time_universal,ts=time_standard)

def main():
    time = Time1()
    time.set_time(13, 27, 6)
    display_time("After calling set_time", time)
    try:
        time.set_time(99,99,99)
    except ValueError as e:
        print e.message
    display_time("After calling set_time with invalid values", time)
    print

    
if __name__ == '__main__':
    main()
