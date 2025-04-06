# Relational operators
a = 20
b = 10

print('Is (a less than b) AND (4 greater than a): ', (a < b) and (4 > a) )
print('Is (b greater than 25) OR ((10 equal to b) AND (10 less than or equal to a)): ', ((b > 25) or (10 == b)) and (10 <= a) )
print('Is not (b greater than or equal to 25) OR (not (15 equal to b) AND (10 equal to b)): ', not (b > 25) or ((10 == b) and (10 <= a)))
print('Is ((a multiplied by 2) greater than b) AND ((b plus 5) less than 8): ', ((a * 2) > b) and ((b + 5) < 8))
print('Is ((6 less than b) AND (b equal to (9 + 1))) AND (a not equal to 20): ', ((6 < b) and (b == (9 + 1)) and (a != 20)))
print('Is ((b not equal to 2) AND (a equal to 7)) OR ((a minus 10) equal to b): ', ((b != 2) and (1 == 7)) or ((a - 10) == b))
print('Is (6 less than or equal to b) OR ((b equal to (9+1))) AND not (a equal to 20): ', (6 <= b) or (b == (9+1)) and not (a == 20))