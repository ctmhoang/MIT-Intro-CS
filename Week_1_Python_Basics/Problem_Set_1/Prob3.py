#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 08 14:20:23 2019

@author: artlist
"""
# Problem 3

# (15/15 points)
# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if
# s = 'azcbobobegghakl', then your program should print:
# Longest substring in alphabetical order is: beggh

# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print:
# Longest substring in alphabetical order is: abc

# Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we
# suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and
# cleared your head.


# Paste your code into this box
s = "azcbobobegghakl"
substr = ""
for start in range(len(s) -1):
    for end in range(1 + start,len(s) -1):
        temp = s[start:end]
        alph_list = sorted(temp)
        alph_str = "".join(alph_list)
        if alph_str == temp and len(substr) < len(temp):
            substr = temp
print(substr)
