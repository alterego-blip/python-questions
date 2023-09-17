while (True):
    choice = input("Area of rectangle or triangle ? r / t  (or) 0 to exit : ")
    match choice:
        case 'r':
            l = float(input("Enter the length: "))
            b = float(input("Enter the breadth: "))
            print("The area of the rectangle is : ", l * b)
        case 't':
            h = float(input("Enter the height of the triangle : "))
            b = float(input("Enter the breadth of the triangle : "))
            print("The area of the triangle is : ", h * b * 0.5)
        case '0':
            exit(0)
        case _:
            print("Invalid option")
