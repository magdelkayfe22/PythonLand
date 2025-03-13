metro = ("Brooklyn", "Queens", "Bronx", "Manhattan", "Long Island")

joinedList = ", ".join(metro)
print(f"List of Boroughs: {joinedList}", end="\n\n")

# Get the index for Bronx
print("Index for Bronx:",metro.index("Bronx"))

# Add additional boroughs using concantenation
metro = metro + ("Staten Island", "Queens")
joinedList = ", ".join(metro)
print(f"Updated list of Boroughs: {joinedList}")

matches = metro.count("Queens")
print(f"Occurrences of Queens in Tuple: {matches}")

# Return a new tuple 
metro = metro[0:-1]
joinedList = ", ".join(metro)

print(f"Corrected list of Boroughs: {joinedList}")