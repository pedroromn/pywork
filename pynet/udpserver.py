#! -*- coding: utf-8 -*-
# Set up a server that will receive packets from a 
# client and send packets to a client

import socket

HOST = '127.0.0.1'
PORT = 5000

# step 1: create a socket
server_socket = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )

# step 2 : bind the socket
