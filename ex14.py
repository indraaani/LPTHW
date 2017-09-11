from sys import argv

# Add another argument
script, Indrani, movie = argv
# Change the prompt variable, use double quotes
prompt = "Answer: "

print "Hi %s, I'm the %s script." % (Indrani, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % Indrani
likes = raw_input(prompt)

print "Where do you live %s?" % Indrani
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "What was the last %s you watched?" % movie
film = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
You have a %r computer. Nice.
The last movie you watched was %r.
""" % (likes, lives, computer, film)
