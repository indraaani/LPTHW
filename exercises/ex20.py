# Ex20: Functions & Files

# imports argv function from the sys module
from sys import argv

# assigns arguments to the two variables
script, input_file = argv

# defines a function called print_all to print all the content within
# a file, with one file object as the formal parameter
def print_all(f):
    # prints the entire file
    print f.read()

# defines a function called rewind to make the file reader go back to
# the beginning of the file, with one file object as the formal parameter
def rewind(f):
    # makes the fiie reader go back to the first byte of the file
    f.seek(0)

# defines a function named print_a_line which prints a single line of the
# file, with an integer counter and file object as formal parameters
def print_a_line(line_count, f):
    # print out the number and contents of a line
    print line_count, f.readline()

# assigns variable 'current_file' to the input file
current_file = open(input_file)

# prints a string
print "First let's print the whole file:\n"

# prints the entire file
print_all(current_file)

# prints a string
print "Now let's rewind, kind of like a tape."

# goes back to the first byte of the file calling the rewind function
rewind(current_file)

# prints a string
print "Let's print three lines:"

# sets current line to 1
current_line = 1
print "current_line = %d" % current_line
# prints the first line calling the print_a_line function
print_a_line(current_line, current_file)

# adds one to current_line, to print line 2
current_line += 1
print "current_line = %d" % current_line
# prints the second line calling the print_a_line function
print_a_line(current_line, current_file)

# adds one to current_line, to print line 3
current_line += 1
print "current_line = %d" % current_line
# prints the third line calling the print_a_line function
print_a_line(current_line, current_file)
