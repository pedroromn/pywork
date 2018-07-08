#! -*- coding : utf-8 -*-
# Client for Tic-Tac-Toe program

import socket
import threading
from Tkinter import *
import Pmw

class TicTacToeClient(Frame, threading.Thread):
    "Client that plays a game of tic-tac-toe"

    def __init__(self):
        pass