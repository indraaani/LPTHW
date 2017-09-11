# Ex16: Reading & Writing Files
#   Write a script that uses read and argv to read the file you just created.

from sys import argv

script, filename = argv

text = open(filename)

print "Here's your file %r:" % filename
print text.read()

#  -----------------------------------------

print "Type the name of your file below:"
file_2 = raw_input("> ")
target = open(file_2)

print "Here's your file %r:" % file_2
print target.read()
