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