'''
A menu driven calculator program using switch statement
switch statements are called match in python

case _: corresponds to default in C programming
as _ matches all values
No break statements are required
'''

print("The calculator program (input 0 0 0 to exit)")

a = b = operation = result = ''
while(True):
    a, operation, b = input("Enter the operation : ").split()
    a, b = float(a), float(b)

    match operation:
        case '+':
            result = a + b
        case '-':
            result = a - b
        case '*':
            result = a * b
        case '/':
            result = a / b
        case '**':
            result =  a ** b
        case '0':
            print("Bye")
            exit(0)
        case _:
            print("Invalid Operation")
            continue

    print("The result is ", result)

