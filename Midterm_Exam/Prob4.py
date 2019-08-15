#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 20:43:31 2019

@author: artlist
"""

# Problem 4
# 10/10 points (graded)
# Implement a function called closest_power that meets the specifications below.

# def closest_power(base, num):
#     '''
#     base: base of the exponential, integer > 1
#     num: number you want to be closest to, integer > 0
#     Find the integer exponent such that base**exponent is closest to num.
#     Note that the base**exponent may be either greater or smaller than num.
#     In case of a tie, return the smaller value.
#     Returns the exponent.
#     '''
#     # Your code here

#For example,
# closest_power(3,12) returns 2
# closest_power(4,12) returns 2
# closest_power(4,1) returns 0

 

# Paste your function here


def closest_power(base, num):
     '''
     base: base of the exponential, integer > 1
     num: number you want to be closest to, integer > 0
     Find the integer exponent such that base**exponent is closest to num.
     Note that the base**exponent may be either greater or smaller than num.
     In case of a tie, return the smaller value.
     Returns the exponent.
     '''
     # Your code here
     result = 0
     if base in [ 0 ,1]:
         #print('Do not have value')
         return None
     if base > num:
         return result # result = 0
     elif base == num:
         result = 1 
         return result
     else:
         for a in range(1, round(num/2)):
             if abs(num - base ** result) <= abs(num - base ** (result + 1)):
                 return a
             else:
                 return a + 1
