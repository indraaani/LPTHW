# Ex6: String & Text

# Assigns the string with 10 instead of the
#   formatting character to variable 'x'
x = "There are %d types of people." % 10

# Assigns the string with "binary" instead of the
#   formatting character to variable  'binary'
binary = "binary"

# Assigns the string with "don't" to variable 'do_not'
do_not = "don't"

# Assigns the string with 'binary' and 'do_not',
#   replacing the formatting character to variable 'y'
y = "Those who know %s and those who %s." % (binary, do_not) # 2 strings inside string

# print "There are 10 types of people."
print x

# print "Those who know binary and those who don't."
print y

# Print "I said 'There are 10 types of people.'"
print "I said %r." % x # string inside string

# Print "I also said 'Those who know binary and those who don't.'"
print "I also said '%s'." % y # string inside string

# Assign boolean False to variable 'hilarious'
hilarious = False

# Assign string "Isn't that joke so funny?" with an unevaluated formatting
#   character to variable 'joke_evaluation'
joke_evaluation = "Isn't that joke so funny? %r" # string inside string

# Print 'Isn't that joke so funny? False'
print joke_evaluation % hilarious

# Assign string "This is the left side of..." to variable 'w'
w = "This is the left side of..."

# Assign string "a string with a right side." to variable e
e = "a string with a right side."

# Print "This is the left side of...a string with a right side." using
#   the + operator
print w + e

# ---------------------------------------------------------------------

hilarious = False
joke_evaluation = "Isn't that joke so funny? %s"

print joke_evaluation % hilarious
