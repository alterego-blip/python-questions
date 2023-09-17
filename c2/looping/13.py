'''
A program to sort numbers using bubble sort
input format : 2, 4, 5, 2
'''

array = list(eval(input("Enter the array of numbers " )))

for i in range(len(array) - 1):
    for j in range(0, len(array) - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

print("The sorted array is : ", array)
