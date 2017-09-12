# Ex19: Functions & Variables

# uses the *args function definition, applying
#   two variables cheese_count, boxes_of_crackers to cheese_and_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # stores the strings that will be printed when cheese_and_crackers is used
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


# gives two numerical values to cheese_count and boxes_of_crackers respectively
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


# assigns values to variables and uses them in cheese_and_crackers
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# gives a sum which will be added up once printed
print "We can even do the math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


# gives the fuction def a combination of variables and numbers
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
