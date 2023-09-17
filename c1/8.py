'''
A program to find sum of digits of a number
'''

num = int(input("Enter the number : "))

sum = 0
while num:
    sum += num % 10
    num //= 10 # Remember that python division is floating point by default

print("The sum of digits is :", sum)
