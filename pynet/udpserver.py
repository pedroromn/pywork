#! -*- coding: utf-8 -*-
# Set up a server that will receive packets from a 
# client and send packets to a client

import socket

HOST = '127.0.0.1'
PORT = 5000

# step 1: create a socket
server_socket = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )

# step 2 : bind the socket
server_socket.bind( (HOST, PORT) )

while 1:

    # step 3: receive packet
    packet, address = server_socket.recvfrom( 1024 )

    print "Packet received"
    print "From host: ", address[0]
    print "Host port: ", address[1]
    print "Length: ", len(packet)
    print "Containing: "
    print "\t" + packet

    # step 4: echo packet back to client
    print "\nEcho data to client...",
    server_socket.sendto( packet, address )
    print "Packet sent\n"

server_socket.close()