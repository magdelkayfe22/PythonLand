print('Python')
print('Python'[1], 'Python'[5])

message = 'Hello World!'

print( message. find('W') )

print( message. find('x') )

print( message. find('l') )

print( message.rfind('l') )

# IndexError: string index out of range
#print( 'Python'[7] )

# Will not throw an error for going out of range
print( 'Python'[ 2 : 7 ])

print('Python'[ 2 : 4 ] )