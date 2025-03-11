team = ["Giants", 2014, "Bears", "Eagles"]
nums = [5, 10, 4, 5]
words = ["bacon", "eggs"]

team.reverse()

print(team)

del team[2]

print(team)

team.append("49ers")

print(team)
print()
print(words)

words.remove("eggs")

print(words)
print()

print( "Sum of numbers: {} ".format( sum(nums) ) )
print( "Length of team: {}".format( len(team) ) )
print( "Max number: {}".format( max(nums) )) 