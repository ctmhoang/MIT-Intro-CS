#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 23:07:02 2019

@author: artlist
"""

# Problem 6
# 15/15 points (graded)
# Implement a function that meets the specifications below.

# def deep_reverse(L):
#     """ assumes L is a list of lists whose elements are ints
#     Mutates L such that it reverses its elements and also 
#     reverses the order of the int elements in every element of L. 
#     It does not return anything.
#     """
#     # Your code here
# For example, if L = [[1, 2], [3, 4], [5, 6, 7]] then deep_reverse(L) mutates L to be [[7, 6, 5], [4, 3], [2, 1]]



# Paste your function here
def deep_reverse(L):
    """
    assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    # Your code here
    L.reverse()
    for ele in L:
        ele.reverse()
        
# can use append[::1]
