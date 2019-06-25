#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 07 15:45:49 2019

@author: artlist
"""
# Problem 2
# (10/10 points)
# Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your
# program should print
# Number of times bob occurs is: 2

# Paste your code into this box

s = 'azcbobobegghakl'
bob = 0
for x in range(len(s)):
    if s[x:x+3] == "bob":
        bob += 1
