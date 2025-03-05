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
print("QCC METERIC SYSTEM".center(30), sep="")
print("=" * 30)
print("Name".ljust(15), "Amount".rjust(15), sep= "")
print("Kilometers".ljust(15) + str(kilometers).rjust(15), sep= "")
print("Meters".ljust(15) + str(meters).rjust(15), sep= "")
print("Centimeters".ljust(15) + str(centimeters).rjust(15), sep="")
print()