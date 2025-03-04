coins = input("Enter amount of change: ")
coins = int(coins)

quarters = coins // 25
coins = coins % 25 
print("Quarters: {}".format(quarters) )

dimes = coins // 10
coins = coins % 10
print("Dimes: {}".format(dimes) )

nickels = coins // 5
coins = coins % 5 
print("Nickles: {}".format(nickels) )

cents = coins // 1 
print("Cents: {}".format(cents) )