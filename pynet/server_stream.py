#! -*- coding: utf-8 -*- 
# Set up a server tha will receive  a connection 
# from a client, send a string to the client
# and close the connection

import socket


HOST = "127.0.0.1"
PORT = 5000
counter = 0

