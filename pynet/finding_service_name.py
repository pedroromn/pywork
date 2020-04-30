# -*- coding: utf-8 -*- 

import socket


def find_service_name():
    protocol_name = 'tcp'
    for port in [80, 25]:
        print "Port: {} => service name: {}".format(port, socket.getservbyport(port, protocol_name))
    print "Port: {} => service name: {}".format(53, socket.getservbyport(53, 'udp'))


if __name__ == '__main__':
    find_service_name()