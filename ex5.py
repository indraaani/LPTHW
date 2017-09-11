# Ex5: Variables & Printing

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth


# this line is tricky, try to get it exactly right
print "If I add %d, %d and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)


# ---------------------------------------------------------------

# Instructions: Change all the variables so there is no my_ in front of each
#   one. Make sure you change the name everywhere,
#   not just where you used = to set them.

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth


# this line is tricky, try to get it exactly right
print "If I add %d, %d and %d I get %d." % (
    age, height, weight, age + height + weight)

# ---------------------------------------------------------------

# Instructions: Try to write some variables that convert the inches and pounds
#   to centimeters and kilograms. Do not just type in the measurements.
#   Work out the math in Python.

inches = 20.0
centimeters = inches * 2.54
pounds = 35.0
kilograms = pounds / 2.2

print "%d inches is equal to %d centimeters." % (inches, centimeters)
print "%d pounds is equal to %d kilograms." % (pounds, kilograms)
