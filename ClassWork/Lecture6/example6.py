# Create a dictionary with two key/value pairs.
# NOTE: There are only color and speed keys. 
alien_0 = {'color': 'green', 'speed': 'slow'}

#attempt tp get the value for points using the "get" method.
point_value = alien_0.get('points', 'No point value assigned')
print(point_value)

print(f"\nLength: {len(alien_0)}")

print(f"\nHas color key: {'color' in alien_0}")
print(f"\nHas colors key: {'colors' in alien_0 }")

print(f"\nValues: {list(alien_0.values())}")

tuple_keys = tuple(alien_0)
print(f"\nTuple: {tuple_keys}")

list_keys = list(alien_0)
print(f"\nList: {list_keys}")