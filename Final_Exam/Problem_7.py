#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 05:43:21 2019

@author: artlist
"""


# Problem 7
# 20.0/20.0 points (graded)
# Write a function called general_poly, that meets the specifications below.

# For example, general_poly([1, 2, 3, 4])(10) should evaluate to 1234 because 
# 1 * 10^3 + 2 * 10^2 + 3 * 10^1 + 4 * 10^0

# So in the example the function only takes one argument with general_poly([1, 2, 3, 4]) and it returns a function that you can apply to a
# value, in this case x = 10 with general_poly([1, 2, 3, 4])(10).

# Paste your code here
def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def apply(x):
        tot = 0
        for i in L:
            tot = tot * x + i
        return tot
    return apply
