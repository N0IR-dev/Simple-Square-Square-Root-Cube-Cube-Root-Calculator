def square(num): #This is a function called "square" the "num" is a place holder value.
    return num ** 2 #This multiplies the number by it self

def squareroot(num):
    return num ** 0.5 #This finds the square root of the number by powering it to 0.5.

def cube(num):
    return num ** 3 #This finds the cube of the number by powering it to 3 times.

def cuberoot(num):
    return num ** (1/3) #This finds the cuberoot of the number by powering it down to one-third.

calculation_type = input("Enter the type of calculation (1) square, 2) squareroot, 3) cube, 4) cuberoot): ")
number = float(input("Enter a number: ")) #This basic imput asks the user what calculation they want to execute.

if calculation_type == "1": #If they chose one, the code will run the square function.
    result = square(number)
    print(f"The square of {number} is {result}.") 
elif calculation_type == "2": #If they chose two, the code will run the squareroot function.
    result = squareroot(number)
    print(f"The square root of {number} is {result}.")
elif calculation_type == "3": #If they chose three, the code will run the cube function.
    result = cube(number)
    print(f"The cube of {number} is {result}.")
elif calculation_type == "4": #If they chose four, the code will run the cuberoot function.
    result = cuberoot(number) 
    print(f"The cube root of {number} is {result}.")
else: #If they chose an invalid input, the code will return an error.
    print("Invalid calculation type. Please enter a number between 1 and 4.")
