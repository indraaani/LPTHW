# Ex17: More Files
# Make the core code one line long

from sys import argv
from os.path import exists

script, from_file, to_file = argv

open(to_file, 'w').write(open(from_file).read())

print "Copied."
