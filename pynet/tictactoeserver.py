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

