#! /usr/bin/python
#! -*- coding: utf-8 -*-

import os
import cgi

def print_header(title):
    print "Content-type: text/html\n"
    print """
    <?xml version = "1.0" encoding = "UTF-8" ?>
    <DOCTYPE html>
    <html>
    <head><title>{title}</title></head>
    <body>
    """.format(title=title)

def web_action():
    row_number = 0
    bacground_color = "white"
    print_header("Enviroment variables")
    