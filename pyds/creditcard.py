# -*- coding: utf-8 -*-


from __future__ import division


class CreditCard(object):
    """A consumer credit card"""

    def __init__(self, costumer, bank, acnt, limit):
        self._costumer = costumer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = 0

    def get_costumer(self):
        return self._costumer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._acnt

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def charge(self, price):
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        self._balance -= amount


class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees"""

    def __init__(self, customer, bank, acnt, limit, apr):
        super(PredatoryCreditCard, self).__init__(customer, bank, acnt, limit)
        self._apr = apr

    def charge(self, price):
        success = super(PredatoryCreditCard, self).charge(price)
        if not success:
            self._balance += 5
        return success

    def process_month(self):
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor































