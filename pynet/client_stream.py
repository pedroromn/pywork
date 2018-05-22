#! -*- coding: utf-8 -*-

import socket


HOST = "127.0.0.1"
PORT = 5000
MAX_BYTES = 1024


# step 1: create a socket
print "Attempting connection"
client_socket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )


# step 2: connect to server
client_socket.connect( (HOST, PORT) )
print "connected to server"

# step 3: process connection
server_message = client_socket.recv( MAX_BYTES )

while server_message != "SERVER>> TERMINATE":

    if not server_message:
        break

    print server_message
    client_message = raw_input("CLIENT>>> ")
    client_socket.send( "CLIENT>>> " + client_message )
    server_message = client_socket.recv( MAX_BYTES )

# step 4: close connection
print "Connection terminated"
client_socket.close()
