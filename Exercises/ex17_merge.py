# Ex17: More Files
# Merge lines 12, 13 into one line

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
# in_file = open(from_file)
# indata = in_file.read()

in_file = open(from_file).read()

print "The input file is %d bytes long" % len(in_file)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(in_file)

print "Alright, all done."

out_file.close()
