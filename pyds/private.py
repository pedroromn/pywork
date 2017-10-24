#! -*- coding: utf-8 -*-
# PrivateClass : class with private member


class PrivateClass(object):

    def __init__(self):
        self.public_data = "public"         # public member
        self.__private_data = "private"     # private member
