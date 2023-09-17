'''
A program to calculate sum and average of an array
input format : 1, 2, 3, 4
'''

sum = 0

array = eval(input("Enter an array: "))

for i in array:
    sum += i

print("The sum is : ", sum, "\nThe average is ", sum / len(array))
