# Logical Operators
a = 8
b = 6
c = "hello"
d = "bye"

print('Is (((a minus b) plus 4) multiplied by 8) greater than ((4 plus a) multiplied by 2): ', ((a - b + 4) * 8) > (4 + a) * 2 )
print('Is (length of c - b) equal to (a divided by 4): ', (len (c) - b) == (a / 4) )
print('Is length of "good-bye" greater than length of ("good" plus d): ', (len("good-bye") > (len("good") + len(d)) ) )
print('Is length of c greater than length of ("good" plus d): ', (len(c) > (len("good") + len(d))))
print('Is length of c less than or equal to length of ("good" plus d): ', (len(c) <= (len("good") + len(d))))