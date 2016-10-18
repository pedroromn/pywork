#!/usr/bin/python
# -*- coding : utf-8 -*-


def linear_sum(S, n):
    """Return the sum of the first n numbers of sequence S."""
    if n == 0:
        return 0
    else:
        return linear_sum(S, n-1) + S[n-1]


def reverse(S, start, stop):
    """Reverse elements in implicit slice S[start:stop]."""
    if start < stop - 1:
        S[start], S[stop-1] = S[stop-1], S[start]
        reverse(S, start+1, stop-1)


def binary_search(data, target, low, high):
    """ Return True if target is found """
    if low > high:
        return False
    else:
        pass
