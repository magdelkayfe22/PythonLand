n = float(input("Enter a number: "))
answ = input("Enter yes or no: ").strip().lower()

print('Is ((n less than 6) AND (n equal to 10 + 5)) OR (answ not equal to \'no\'): ', ((n < 6) and (n == 10 + 5)) or (answ != 'no'))
print('Is ((6 not equal to n) AND (5 equal to n)) OR (answ equal to \'yes\'): ', ((6 != n) and (5 == n) or (answ == 'yes')))