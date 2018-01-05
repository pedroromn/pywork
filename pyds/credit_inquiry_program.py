#! -*- coding: utf-8 -*-
# Credit inquiry program

import sys

# retrieve one user command
def get_request():

    while 1:
        request = int(raw_input("\n?"))
        if 1 <= request <= 4:
            break
    return request

