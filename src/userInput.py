from equations import Equations
from random import randint
import subprocess, os, platform, sys

user_input = ''
args = []
print("Loading ...")
user_equation = Equations()

def printOptions():
    print("Please pass arguments a number/symbol at a time")
    print("Acceptable inputs are:")
    print("Any one digit number (0-9)")
    print("Addition, Subtraction, Multiplication and Division symbols (+, -, *, /)")
    print("If you would like to input numbers with multiple digits, place them one after another")
    print("If you want a negative number, then only make the first digit negative")
    print("Input 's' to have the program solve the inputted function")
    print("Input 'r' to reset the equation")
    print("Input 'd' to see a simple demo of the program")
    print("Input 'e' to solve a random equation")
    print("Input 'p' to print out your current list of arguments")
    print("Input 'q' to quit the program")
    print("Input 'c' to clear the terminal and list options again")


symbol_inputs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/',]

printOptions()

while True:
    user_input = input("Enter Symbol: ")
    if user_input == 's':
        args_length = len(args)
        if args_length == 0:
            print("Please enter your funtion arguments")
            continue
        print("Answer: " + str(user_equation.solveEquation(args)))
        args = []

    elif user_input == 'r':
        args = []

    elif user_input == 'd':
        user_equation.args = ['1', '0', '+', '5' ,'*', '2', '/', '5', '-', '1', '1']
        user_equation.setup()
        print("Answer :" + str(user_equation.solve()))

    elif user_input == 'e':
        num_of_operators = randint(1,4)
        for i in range(num_of_operators):
            digits = randint(1,3)
            for j in range(digits):
                args.append(str(randint(0,9)))
            symbol_index = randint(10,11)
            args.append(symbol_inputs[symbol_index])
        digits = randint(1,3)
        for j in range(digits):
            args.append(str(randint(0,9)))
        print("Answer: " + str(user_equation.solveEquation(args)))
        args = []

    elif user_input == 'p':
        print(args)

    elif user_input == 'q':
        print("Exitting Program ...")
        break

    elif user_input == 'c':
        output = subprocess.run("clear",shell=True)
        if output.returncode:
            subprocess.call("cls",shell=True)
        printOptions()

    elif user_input in symbol_inputs:
        args.append(user_input)

    else:
        print("Error: Invalid Input")
                
                