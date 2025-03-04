miles = input("Enter number of miles: ")
miles = float(miles)

yards = input("Enter number of yards: ")
yards = float(yards)

feet = input("Enter number of feet: ")
feet= float(feet)
inches = input("Enter number of inches: ")
inches = float(inches)
print()

totalInches = (63360 * miles) + (36 * yards) + (12 * feet) + inches

totalMeters = totalInches / 39.37

kilometers = int(totalMeters / 1000)

meters = int(totalMeters % 1000)

centimeters = round((totalMeters % 1) * 100, 1)

print()
print("{0:^21s}".format("QCC METERIC SYSTEM") )
print("{0:s}".format("=" * 21) )
print("{0:<15s}{1:<6s}".format("Name", "Amount") )
print("{0:<15s}{1:>6n}".format("Kilometers", kilometers) )
print("{0:<15s}{1:>6n}".format("Meters", meters) )
print("{0:<15s}{1:>6n}".format("Centimeters", centimeters) )
print()
