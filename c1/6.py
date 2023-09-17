'''
A program to calculate roots of a quadratic equation
b = (-b +- D) / 2a
'''

a, b, c = input("Enter the coefficients of the equation ax^2 + bx + c = 0 as a b c : ").split()
a, b, c = int(a), int(b), int(c) # Converting str to int
D = b**2 - 4 * a * c

if not D:
    print("The roots are equal to ", -b / 2 / a)
else: # Python supports complex numbers as built in
    print("The roots are equal to ", (-b + D ** 0.5) / 2 / a, "and", (-b - D ** 0.5) / 2 / a)
