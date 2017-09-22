# -*- coding: utf-8 -*-

import socket

def remote_machine_info():
    remote_host = 'www.caltech.edu'
    try:
        print "IP address: {}".format(socket.gethostbyname(remote_host))
    except socket.error, err_msg :
        print "{}: {}".format(remote_host, err_msg)


if __name__ == '__main__':
    remote_machine_info()