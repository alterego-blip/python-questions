'''
A program to print all prime numbers of a range
'''

s, e = input("Enter the start and end of range (end excluded) : ").split()

s, e = int(s), int(e)

for i in range(s, e):
    if i < 2:
        continue
    elif i == 2:
        print(i)
    else:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i) # Executes only after the completion of for loop
