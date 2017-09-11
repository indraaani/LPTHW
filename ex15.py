# Ex15: Reading Files

# imports argv from sys package
from sys import argv

# assigns variables to argv
script, filename = argv

# opens file object
txt = open(filename)

# prints the file you opened earlier
print "Here's your file %r:" % filename
print txt.read()

# prints a string
print "Type the filename again:"
# allows user to input the file
file_again = raw_input("> ")

# opens previously entered file object
txt_again = open(file_again)

# prints the file you opened earlier
print txt_again.read()
