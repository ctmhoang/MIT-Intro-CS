# Exercise: biggest

# (5/5 points)
# ESTIMATED TIME TO COMPLETE: 7 minutes

# Consider the following sequence of expressions:
#
# animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
#
# animals['d'] = ['donkey']
# animals['d'].append('dog')
# animals['d'].append('dingo')
# We want to write some simple procedures that work on dictionaries to return information.

# This time, write a procedure, called biggest, which returns the key corresponding to the entry with the largest number of values
# associated with it. If there is more than one such entry, return any one of the matching keys.

# Example usage:
# >>> biggest(animals)
# 'd'
# If there are no values in the dictionary, biggest should return None.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed Jul 10 06:10:25 2019
@author: artlist
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    result = None
    biggestvalue = 0
    for key in aDict.keys():
        if len(aDict[key]) >= biggestvalue:
            result = key
            biggestvalue = len(aDict[key])
    return result
print(biggest(animals))
