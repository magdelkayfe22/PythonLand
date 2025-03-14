states = []
states_inputted = input("Enter a list of states comma separated without spaces:")
states = states_inputted.split(",")
print(states)

# need to print colorado (middle index) len= 2
middleIndex = int(len(states) / 2 )
print("Middle state: ", states[middleIndex])

#Now remove middle Index
del states[middleIndex]
print("After removing middle state: {}".format(", ".join(states)))

# Add NY again to the end of the list
states.append(states[0])
print(f"Appended first state to end of the list: {states}")

#remove ny from the first list
del states[0]
print("Removed first state from the list: {}".format(", ".join(states)))