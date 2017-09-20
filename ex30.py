# Ex30: Else and If

# assigns values to the respective variables
people = 30
cars = 40
buses = 40

# if cars are more than people, executes this block
if cars > people:
    # prints the string if the above statement is true
    print "We should take the cars."
# elif allows for an alternative true statement, executes this block if true
# if cars are less than people
elif cars < people:
    # prints the string if the above statement is true
    print "We should not take the cars."
# if all the above statements are false, executes this block
else:
    # prints the string if none of the above statements are true
    print "We can't decide."

# if buses are more than cars, executes this block
if buses > cars:
    # prints the string if the above statement is true
    print "That's too many buses."
# elif allows for an alternative true statement, executes this block if true
# if buses are less cars people
elif buses < cars:
    # prints the string if the above statement is true
    print "Maybe we could take the buses."
# if all the above statements are false, executes this block
else:
    # prints the string if none of the above statements are true
    print "We still can't decide."

# if people are more than buses, executes this block
if people > buses:
    # prints the string if the above statement is true
    print "Alright, let's just take the buses."
# if all the above statements are false, executes this block
else:
    # prints the string if none of the above statements are true
    print "Fine, let's just stay home then."
