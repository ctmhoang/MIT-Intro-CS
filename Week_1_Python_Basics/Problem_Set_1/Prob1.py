# Problem 1
# (10/10 points)
# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
# For example, if s = 'azcbobobegghakl', your program should print:
# Number of vowels: 5

# Paste your code into this box

s = 'azcbobobegghakl'
countVow = 0
for char in s:
    if char == 'a' or char == 'e' or char == 'o' or char == 'u':
        countVow += 1
print("Number of vowvels: " + str(countVow))
