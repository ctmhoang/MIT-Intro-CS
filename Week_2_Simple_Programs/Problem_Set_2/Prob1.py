# Problem 1 - Paying Debt off in a Year

# (10/10 points)
# Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the
# credit card company each month.

# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal
# monthlyPaymentRate - minimum monthly payment rate as a decimal

# For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining
# balance. Be sure to print out no more than two decimal digits of accuracy - so print

# Remaining balance: 813.41
# instead of
# Remaining balance: 813.4141998135

# So your program only prints out one thing: the remaining balance at the end of the year in the format:
# Remaining balance: 4784.0

# A summary of the required math is found below:
# Monthly interest rate= (Annual interest rate) / 12.0
# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)



# Paste your code into this box
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 10:22:14 2019

@author: artlist
"""
# Calculate the credit card balance after one year
#if a person only pays the minimum monthly payment required
# by the credit card company each month.
def maxub(bl, annualIr, monthlyPr, m):
    monthlyIr = annualIr /12
    monthlyUb = bl -(bl*monthlyPr)
    rm = monthlyUb + (monthlyUb * monthlyIr) #remaining
    if m == 1:
        return rm
    else:
         return maxub(rm, annualIr, monthlyPr, m - 1)
print("Remaining: ",maxub(balance,annualInterestRate,monthlyPaymentRate,12))
# print("Remaining: ",round(maxub(42,0.2,0.04,12)))
