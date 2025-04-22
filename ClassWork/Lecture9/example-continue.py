# Continue Loop
import random
import time

number = 0
while number >= 0:
    number = random.randrange(-1, 9)

    if number in [4,5,9]:
        print(f"** Number {number} skipped because it is on the list omitted numbers")
        continue

    print(f"The random number picked was {number}")

    # Sleep for 3 seconds
    time.sleep(3)

print("Good-bye!")
