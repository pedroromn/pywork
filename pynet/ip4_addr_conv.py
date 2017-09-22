# -*- coding: utf-8 -*-

import socket
from binascii import hexlify


def get_ipaddr():
    host_list = ['www.google.com', 'www.python.org','www.unimagdalena.edu.co', 
                    'cartera.unimagdalena.edu.co']
    ip_list = []
    for host in host_list:
        ip_list.append(socket.gethostbyname(host))
    return ip_list


def convert_ip4_address():
    ipaddr = get_ipaddr()
    for ip_addr in ipaddr:
        packed_ip_addr = socket.inet_aton(ip_addr)
        unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
        print "IP address: {} => Packed: {}, Unpacked: {}".format(ip_addr, 
        hexlify(packed_ip_addr), unpacked_ip_addr)


if __name__ == '__main__':
    convert_ip4_address()