# Ex26: Congratulations, Take a Test!

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

# bug: def print_first_word(words) [added a : at the end]
def print_first_word(word):
    """Prints the first word after popping it off."""
    # bug: word = words.poop(0) [fixed poop to pop]
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    # bug: word = words.pop(-1 [fixed (-1 to (-1)]
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

# bug: five = 10 - 2 + 3 - 6 [fixed the equation by changing 5 to 6]
five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    # bug: jars = jelly_beans \ 1000 [fixed \ 1000 to / 1000]
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
# bug: beans, jars, crates == secret_formula(start-point)
# [removed the extra =, changed start-point to start_point]
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
# bug: %d crabapples [changed crabapples to crates]
# bug: % secret_formula(start_pont [fixed (start_pont to (start_point)]
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)

# # bug: sentence = "All god\tthings come to those who weight."
# [corrected spelling of 'good' and 'wait', removed \t]
sentence = "All good things come to those who wait."

# bug: words = ex25.break_words(sentence) [removed references to ex25]
words = break_words(sentence)
# bug: sorted_words = ex25.sort_words(words) [removed references to ex25]
sorted_words = sort_words(words)

print_first_word(words)
print_last_word(words)
# bug: .print_first_word(sorted_words) [removed .]
print_first_word(sorted_words)
print_last_word(sorted_words)
# bug: sorted_words = ex25.sort_sentence(sentence) [removed references to ex25]
sorted_words = sort_sentence(sentence)
# bug: prin sorted_words [corrected spelling of print]
print sorted_words

# bug: print_irst_and_last(sentence) [fixed spelling of 'first']
print_first_and_last(sentence)

# # bug:   print_first_a_last_sorted(senence)
# [corrected the spelling of 'and' and 'sentence']
print_first_and_last_sorted(sentence)
