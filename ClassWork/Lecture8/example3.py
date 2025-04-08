# If Statement (Decision Structure)

firstNumber = eval( input("Enter first number: ") )
secondNumber = eval( input("Enter second number: ") )
thirdNumber = eval( input("Enter third number: ") )

# Set the max as the firstNumber value and use it compare against.
max = firstNumber

# Check if the current set max number is greater than secondNumber value.
if secondNumber > max:
    max = secondNumber

# Check if the current set max number is greater than thirdNumber value.
if thirdNumber > max:
    max = thirdNumber

print("The largest number is", str(max) + ".")