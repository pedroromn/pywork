#! /usr/bin/python
#! -*- coding: utf-8 -*-

import time

def print_header(title):
    print """Content-type: text/html

    <?xml version = "1.0" encoding = "UTF-8"?>
    <!DOCTYPE html>
    <html>
    <head><title>%s</title></head>

    <body>""" % title

def main():
    print_header("Current data and time")
    print time.ctime( time.time() )
    print "</body></html>"

if __name__ == '__main__':
    main()
