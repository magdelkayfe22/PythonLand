# sort a list

repeat_equal_sign_and_line_break = "\n" + ("=" * 60)

# create a List with numeric values
list1 = [6, 4, -5, 3.5]

print(repeat_equal_sign_and_line_break)
print("TEST 1: Values being sorted: ", list1)

# Sort the list items by value
# NOTE: This sort was done using the "less than" operator
list1.sort()

print("Sorted values: ", list1)
print("Max value: ", max(list1))
print("Min valueL ", min(list1))

# Create a list with string values
list2 = ["ha", "hi", 'B', '7']

print(repeat_equal_sign_and_line_break)
print("Test 2: Values being sorted: ", list2)

# NOTE: This sort was done using the "less than" operator and the ascii values for the characters.
list2.sort()

print("Sorted values: ", list2)
print("Max value: ", max(list2))
print("Min value: ", min(list2))