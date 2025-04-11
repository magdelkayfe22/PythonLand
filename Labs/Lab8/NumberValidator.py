print("** ENTER ONLY WHOLE NUMBERS **", end="\n\n")

num1 = (input("Enter first number: "))
num2 = (input("Enter second number: "))

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    print("The product of both numbers is: ", num1 * num2)

elif not num1.isdigit() and not num2.isdigit():
    print("Both numbers need to be a whole numbers.")
elif not num1.isdigit():
    print("The first number needs to be whole number.")
elif not num2.isdigit():
    print("The second number needs to be a whole number.")
else:
    print("Invalid input!")