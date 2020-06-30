#! -*- coding : utf-8 -*-
# Client for Tic-Tac-Toe program

import socket
import threading
from Tkinter import *
import Pmw

class TicTacToeClient(Frame, threading.Thread):
    "Client that plays a game of tic-tac-toe"

    def __init__(self):
        "Create GUI and play game"

        threading.Thread.__init__( self )

        # initialize GUI

        Frame.__init__( self )
        Pmw.initialise()
        self.pack( expand=YES, fill=BOTH )
        self.master.title("Tic-Tac-Toe Client")
        self.master.geometry( "250x325" )

        self.id = Label(self, anchor = W )
        self.id.grid( columnspan = 3, sticky = W+E+N+S )

        self.board = []

        # create and add all buttons to the board
        for i in range( 9 ):
            new_button = Button( self, font = "Courier 20 bold",
                height = 1, width = 1, relief = GROOVE,
                name = str(i) )
            new_button.bind( "<Button-1>", self.send_clicked_square)
            self.board.append( new_button )

        current = 0

        # display all buttons in 3x3 grid
        for i in range(1, 4):

            for j in range(3):
                self.board[ current ].grid( row = i, column = j, 
                    sticky = W+E+N+S )
                current += 1

        
        # area for server messages
        self.display = Pmw.ScrolledText( self, text_height = 10, 
            text_width = 35, vscrollmode = "static")
        self.display.grid( row = 4, columnspan = 3)

        self.start() # run thread

    
    def run( self ):
        "Control thread that allows continuous update of the display"




        