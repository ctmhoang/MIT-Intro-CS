#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 20:45:43 2019

@author: artlist
"""

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
            Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
            Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    
    def intersect(self,other):
#        self.result = []
#        for e in self.vals:
#            if e in other.vals:
#                self.result.append(e)
#        return("{" + ",".join(str(f) for f in self.result)+"}")
        return '{' + ','.join([str(e) for e in sorted(self.vals) if e in other.vals]) + '}'
        
    def __len__(self):
        self.counter = 0
        for i in self.vals:
            self.counter += 1
            return self.counter
        
        
# class intSet(set):
#     """An intSet is a set of integers
#     The value is represented by a list of ints, self.vals.
#     Each int in the set occurs in self.vals exactly once."""

#     # def __init__(self, st=None):
#     #     """Create an empty set of integers"""
#     #     self = set() if st is None else set(st)

#     def insert(self, e):
#         """Assumes e is an integer and inserts e into self"""
#         self.add(e)

#     def member(self, e):
#         """Assumes e is an integer
#             Returns True if e is in self, and False otherwise"""
#         return e in self

#     def remove(self, e):
#         """Assumes e is an integer and removes e from self
#             Raises ValueError if e is not in self"""
#         try:
#             self.remove(5)
#         except KeyError:
#             raise ValueError(str(e) + ' not found')

#     def intersect(self, other):
#         return intSet({e for e in self if e in other})

#     # def __len__(self):
#     #     return len(self)

#     def __str__(self):
#         """Returns a string representation of self"""
#         return '{' + ','.join([str(e) for e in sorted(self)]) + '}'

        
