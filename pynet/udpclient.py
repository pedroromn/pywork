#! -*- coding: utf-8 -*- 
# Set up a client that will send packets to a
# server and receive packets from a server

import socket

HOST = "127.0.0.1"
PORT = 5000

# step 1: create a socket
client_socket = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )

while 1:

    # step 2: send a packet
    packet = raw_input( "Packet>>> " )
    print "\nSending packet containing: ", packet
    client_socket.sendto(packet, (HOST, PORT) )
    print "packet sent\n"

    # step 3: receive packet back from server
    packet, address = client_socket.recvfrom(1024)

    print "Packet received: "
    print "From host: ", address[0]
    print "Host port: ", address[1]
    print "Length: ", len(packet)
    print "Containing: "
    print "\t" + packet + "\n"

client_socket.close()