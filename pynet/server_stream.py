#! -*- coding: utf-8 -*- 
# Set up a server tha will receive  a connection 
# from a client, send a string to the client
# and close the connection

import socket


HOST = "127.0.0.1"
PORT = 5000
MAX_BYTES = 1024
counter = 0

# step 1: create a socket
print "Waiting for connection"
socket_server = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

# step 2: bind the socket
socket_server.bind( (HOST, PORT) )

while 1:
    # prepare for a connection
    print "<< Waiting for connection >>"
    socket_server.listen(1)

    # step 4: wait for and accept a connection
    socket_conn, address = socket_server.accept()
    counter += 1
    print "Connection", counter, "received from ", address[0]

    # step 5: process connection
    socket_conn.send("SERVER>>> Connection successful")
    client_message = socket_conn.recv(MAX_BYTES)

    while client_message != "CLIENT>>> TERMINATE":

        if not client_message:
            break
        
        print client_message
        server_message = raw_input("SERVER>>> ")
        socket_conn.send("SERVER>>> " + server_message)
        client_message = socket_conn.recv(MAX_BYTES)

    print "Connection terminated"
    socket_conn.close()





