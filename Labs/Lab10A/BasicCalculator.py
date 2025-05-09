import math
import operator

# Basic Math Calculator

# Named Constant 
OPTION_EXIT = -1

# Global variable 
menu_options = {
    "Addition": 1,
    "Subtraction": 2,
    "Multiplication": 3,
    "Division": 4,
    "Square Root": 5,
    "Power": 6
}

def addition(arg1, arg2):
    output = operator.add(arg1, arg2)
    return 'num1 + num2 = ' + str(output) + '\n'

def subtraction(arg1, arg2):
    output = operator.sub(arg1, arg2)
    return 'num1 - num2 = ' + str(output) + '\n'\

def multiplication(arg1, arg2):
    output = operator.mul(arg1, arg2)
    return 'num1 * num2 = ' + str(output) + '\n'

def division(arg1, arg2):   
    output = operator.truediv(arg1, arg2)
    return 'num1 / num2 = ' + str(output) + '\n'

def square_root(arg1, arg2):
    output1 = math.sqrt(arg1)
    output2 = math.sqrt(arg2)
    return 'Square root of num1 = ' + str(output1) + '\n' + 'Square root of num2 = ' + str(output2) + '\n' 

def power(arg1, arg2):
    output = math.pow(arg1, arg2)
    return 'num1 to the power of num2 = ' + str(output) + '\n'



def menu():
    # Local variable
    selection = 0

    # Keep Looping while the selection is not one of the options.
    while selection not in menu_options.values() and selection != OPTION_EXIT:

        for option in menu_options:
            print(f"{menu_options[option]}) {option}")

        print("\n(Enter -1 to exit application)\n")

        selection = eval(input("Please select an option from the menu above: "))

    return selection

def main():
    option = menu()
    while option != OPTION_EXIT:
        num1 = eval(input("Enter your first number: "))
        num2 = eval(input("Enter your second number: "))

        if option == 1:
            print(addition(num1, num2))

        elif option == 2:
            print(subtraction(num1, num2))

        elif option == 3:
            print(multiplication(num1, num2))

        elif option == 4:
            print(division(num1, num2))

        elif option == 5:
            print(square_root(num1, num2))

        elif option == 6:
            print(power(num1, num2))


        option = menu()

    print("\nHave a great day!")

    # End of while loop
if __name__ == '__main__':

    main()
    
