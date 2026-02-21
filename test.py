def square(num):
    return num ** 2

def squareroot(num):
    return num ** 0.5

def cube(num):
    return num ** 3

def cuberoot(num):
    return num ** (1/3)

calculation_type = input("Enter the type of calculation (1) square, 2) squareroot, 3) cube, 4) cuberoot): ")
number = float(input("Enter a number: "))

if calculation_type == "1":
    result = square(number)
    print(f"The square of {number} is {result}.")
elif calculation_type == "2":
    result = squareroot(number)
    print(f"The square root of {number} is {result}.")
elif calculation_type == "3":
    result = cube(number)
    print(f"The cube of {number} is {result}.")
elif calculation_type == "4":
    result = cuberoot(number)
    print(f"The cube root of {number} is {result}.")
else:
    print("Invalid calculation type. Please enter a number between 1 and 4.")