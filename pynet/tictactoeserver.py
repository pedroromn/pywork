#! -*- coding: utf-8 -*-
# Class TicTacToeServer mantains a game of Tic-Tac-Toe
# for two clients, each managed by a Player Thread

import socket 
import threading

class Player( threading.Thread ):
    "Thread used to manage each Tic-Tac-Toe client individually"

    def __init__(self, connection, server, number):
        "Initialize thread and setup variables"

        threading.Thread.__init__(self)

        if number == 0:
            self.mark = 'X'
        else:
            self.mark = 'O'

        self.connection = connection
        self.server = server
        self.number = number
    
    def other_player_moved(self, location):
        "Notify client of opponent's last move"
        
        self.connection.send("Opponent moved.")
        self.connection.send( str(location) )

    def run( self ):
        "Play the game"

        self.server.display( "Player %s connected " % self.mark )
        self.connection.send( self.mark )
        self.connection.send( "%s connected " % self.mark )

        # wait for another player to arrive
        if self.mark == 'X':
            self.connected.send( "Waiting for another player... " )
            self.server.game_begin_event.wait()
            self.connection.send("Other player connected. Your move.")
        else:
            self.server.game_begin_event.wait()
            self.connection.send( "Waiting for first move..." )

        # play game
        while not self.server.game_over():
            location = self.connection.recv(2)

            if not location:
                break
            
            if self.server.valid_move( int(location), self.number ):
                self.server.display( "loc: " + location )
                self.connection.send( "Valid move." )
            else:
                self.connection.send("Invalid move, try again.")

        self.connection.close()
        self.server.display("Game Over")
        self.server.display("Connection closed")

class TicTacToeServer(object):
    "Server that mantains a game of TicTacToe for two clients"

    def __init__( self ):
        "Initialize variables and setup server"

        HOST = ""
        PORT = 5000

        self.board = []
        self.current_player = 0
        self.turn_condition = threading.Condition()
        self.game_begin_event = threading.Event()

        for i in range( 9 ):
            self.board.append(None)


        # setup server socket
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind( (HOST, PORT) )
        self.display("Server awaiting connections...")

    def execute( self ):
        "Play the game -- create and start both player threads"

        self.players = []

        for i in range( 2 ):
            self.server.listen(1)
            connection, address = self.server.accept()
            self.players.append( Player( connection, self, i) )
            self.players[-1].start()

        # players are suspended until player o connects
        # resume players now
        self.game_begin_event.set()

    def display( self, message ):
        "Display a message on the server"

        print message

    def valid_move( self, location, player ):
        "Determine if a moce is valid -- if so, make move"

        # only one move can be made at time
        self.turn_condition.acquire()

        while player != self.current_player:
            self.turn_condition.wait()

        if not self.is_occupied( location ):

            if self.current_player == 0:
                self.board[ location ] = 'X'
            else:
                self.board[ location ] = 'O'

            self.current_player = ( self.current_player + 1) % 2
            self.players[ self.current_player ].other_player_moved( location )
            self.turn_condition.notify()
            self.turn_condition.release()
            return 1
        else:
            self.turn_condition.notify()
            self.turn_condition.release()
            return 0

    def is_occupied( self, location ):
        "Determine if a space is occupied"

        return self.board[location]  # a empty space is None

    def game_over( self ):
        "Determine if the game is over"

        # place code here testing for a game winner
        # left as a exercise for the reader

        return 0    
