'''
A program to print pascal's triangle
1
1 1
1 2 1
1 3 3 1

Input: Number of rows to print
'''

n = int(input('Enter number of rows to print: '))
triangle = [1]
temp = []

if n > 0:
    print([1])

for i in range(1, n):
    temp = []
    temp.append(1)
    for j in range(len(triangle) - 1):
        temp.append(triangle[j] + triangle[j + 1])
    temp.append(1)
    triangle = temp
    print(temp)
