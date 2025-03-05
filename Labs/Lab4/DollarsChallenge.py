coins = input("Enter amount of change: ")
coins = int(coins)

dollars = coins // 100 
coins = coins % 100
print("Dollars: {}".format(dollars))

quarters = coins // 25
coins = coins % 25 
print("Quarters: {}".format(quarters) )

dimes = coins // 10
coins = coins % 10
print("Dimes: {}".format(dimes) )

nickles = coins // 5
coins = coins % 5 
print("Nickles: {}".format(nickles) )

cents = coins 
print("Cents: {}".format(cents) )