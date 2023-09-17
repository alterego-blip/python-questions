import math
'''
A program to print the values of sine and cosine series
based on Taylor series,
cosx = 1 - x^2 / 2! + x^4 / 4! - x^6 / 6! ...
sinx = x - x^3 / 3! + x^5 / 5! - x^7 / 7! ...

it's physically impossible to calculate infinite terms
hence we'll stop after some iterations
'''
def cosine(x):
    output = 0
    sign = 1
    for i in range(0, 7, 2):
        output += sign * x ** i / fact(i)
        sign *= -1
    print("The required output is : ", output)

def sine(x):
    output = 0
    sign = 1
    for i in range(1, 8, 2):
        output += sign * x ** i / fact(i)
        sign *= -1
    print("The required output is : ", output)

def fact(i):
    output = 1
    if i == 0:
        return 1
    else:
        return i * fact(i - 1)
print("Sine, Cosine program. press 0 to exit")

op, x = '', 0

while True:
    op, x = input("Enter the operation and value as 'op x' : ").split()
    x = (float(x) % 360 ) * math.pi / 180
    match op:
        case 's':
            sine(x)
        case 'c':
            cosine(x)
        case '0':
            exit()
        case _:
            print("Invalid input")
            

