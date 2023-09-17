'''
A program to compute electricity bill based on slabs
units   unit price
<100    1
<200    5
<400    8
<600    12
>=600   15
'''

amount = units = 0
while (True):
    units = float(input("Enter the number of units consumed (0 to exit) : "))

    if not units: # Like C, non-zero is true and zero/null values are false
        exit(0)
    elif units < 100:
        amount = units * 1
    elif units < 200:
        amount = units * 5
    elif units < 400:
        amount = units * 8
    elif units < 600:
        amount = units * 12
    else:
        amount = units * 15

    print("The total amount is :", amount)
        
