## Finding the minumum, maximum, and average of a sequence of numbers.
## Obtain the list of numbers 
list1 = []
print("Requirements: ")
print("- Enter -1 to terminate entering numbers.")
print("- You have to enter 3, or more, nonnegative numbers.")
print()

num = eval(input("Enter a number: "))

while num != -1:
    if (num < 0):
        print("Sorry, invalid number entered. Numbers must be nonnegative values.")
    else: 
        list1.append(num)

    num = eval(input("Enter another number: "))

if len(list1) == 0:
        print("You ended the application without adding any valid numbers. Good-bye!")

elif len(list1) <= 2:
     print("Sorry, you didn't enter the required nonnegative numbers for processing.")
     print("Good-bye!")
else:
    lowest = min(list1)
    print("Lowest: ", lowest)
    highest = max(list1)
    print("Highest: ", highest)
    average = sum(list1) / len(list1)
    print("Average: ", average)
    print("All numbers entered:", sorted(list1))
    print("Good-bye!")

