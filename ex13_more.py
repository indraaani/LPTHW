# Ex13: Paramenters, Unpacking, Variables
# Study Drill: Script that has more arguments

from sys import argv

script, water, mud, air, fire, earth = argv

print "The script is called:", script
print "The first element is:", water
print "The second element is:", mud
print "The third element is:", air
print "The fourth element is:", fire
print "These four elements make up the:", earth
print "How many elements are there? %d" % int(raw_input("Total elements "))
