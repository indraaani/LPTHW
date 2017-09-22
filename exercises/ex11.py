# Ex11: Asking Questions

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So you're %r old, %r tall and %r heavy." % (
    age, height, weight)

# Create another form to ask Questions

print "Where do you live?",
residence = raw_input()
print "How many years have you lived there?",
time = raw_input()
print "Who do you live with?",
people = raw_input()

print "So you've lived in %s for %s years with your %s." % (
    residence, time, people)

# Using raw input for numbers and calculation:

print "What's your favourite number?",
number1 = int(raw_input())
print "And what's your least favourite number?",
number2 = int(raw_input())

number3 = number1 + number2

print "So the total of your favourite and least favourite number is %s." % (
    number3)
