#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 08:20:45 2019

@author: artlist
"""

print("Hi I am here to guess your number(0-100) ")
high = 100
low = 0
ans = int((high+low)/2)
while high != low:
  print("Is your secret number ", ans)
  guess= input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly!")
  if guess == "h":
    high = int(ans)
  elif guess == "l":
    low = int(ans)
  elif guess == "c":
    break
  else:
      print('')
      print("Sorry, I did not understand your input.", end=" ")
      print("Pls retyping letter in the above regulation:")
  ans = int((high+low)/2)
if high == low:
    print("Game over. Your secret number was: ", ans)
print("Your secret number is", ans)
