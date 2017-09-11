# Ex16: Reading & Writing Files

# imports argv from sys module
from sys import argv

# assigns variables to argv
script, filename = argv

# prints the following strings, where %r is the name of the file
print "We're going to erase %r." % filename
print "If you don't want to do that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

# allows you to either continue the process by pressing enter or
#    stopping by pressing CTRL+C and returning to the working directory
raw_input("?")

# prints a string after pressing enter
print "Opening the file..."
# assigns the variable 'target' and opens a file object for the file
#   'w' paramater indicates there's data being written into the file
target = open(filename, 'w')

# prints a string
print "Truncating the file. Goodbye!"
# truncate erases the contents of a given file, in this case, the file object
#   DON'T NEED TRUNCATE IF OPENING FILE WITH THE 'w' (write) parameter
# target.truncate()

# prints a string
print "Now I'm going to ask you for three lines."

# assigns variables and allows the user to input data
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

# prints a string
print "I'm going to write these to the file."

# writes line1 into the file that opened
target.write(line1)
# uses an escape sequence to move the next line down
target.write("\n")
# writes line2 into the file that opened
target.write(line2)
# uses an escape sequence to move the next line down
target.write("\n")
# writes line3 into the file that opened
target.write(line3)
# uses an escape sequence to move the next line down
target.write("\n")

# prints a string
print "And finally, we close it."
# closes the file
target.close()
