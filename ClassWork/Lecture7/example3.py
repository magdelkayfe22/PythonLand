# Logical Operator

n = 4
answ = 'Y'

print(f"CHECK 1: Values being compared: {n} and {answ}", end="\n\n")

print( "Is (2 less than 4) AND ( 4 less than 6): ", (2 < n) and (n < 6) )
print( "Is (2 less than 4) OR (4 equal to 6): ", (2 < n) or (n == 6) )
print( "Is not (4 less than 6): ", not (n < 6) )

# Only one side needs to be true in order for the condition to evaluate to true
print( "Is ('y' equal to 'Y') OR ('y' equal to 'y'): ", (answ == 'Y') or (answ == 'y') )

# Both sides need to be true in order for the condition to evalute to true.
print( "Is ('y' equal to 'Y') AND ('y' equal to 'y'): ", (answ == 'Y') and (answ == 'y') )

print( "Is ('Y' equal to 'y'): ", (answ =='y'))

# The condition is looking for the opposite outcome when using  NOT logical operator. 
print( "Is not ('Y' equal to 'y'): ", not (answ == 'y') )