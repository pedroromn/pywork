# Fig. 20.3: fig20_03.py
# Set up a client that will read information sent
# from a server and display that information.

import socket
import sys

HOST = "127.0.0.1"
PORT = 5000

# step 1: create socket
print "Attempting connection"
mySocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

# step 2: make connection request to server
try:
   mySocket.connect( ( HOST, PORT ) )
except socket.error:
   sys.exit( "Call to connect failed" )

print "Connected to Server"

# step 3: transmit data via connection
serverMessage = mySocket.recv( 1024 )

while serverMessage != "SERVER>>> TERMINATE":

   if not serverMessage:
      break

   print serverMessage
   clientMessage = raw_input( "CLIENT>>> " )
   mySocket.send( "CLIENT>>> " + clientMessage )
   serverMessage = mySocket.recv( 1024 )

# step 4: close connection
print "Connection terminated"
mySocket.close()
