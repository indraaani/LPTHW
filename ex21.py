def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b


print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here's a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

# convert it into a numerical equation
what_numerical =  35 + (74 - (180 * (50 / 2)))

print "The answer is:", what_numerical

# write a simple formula and use functions
num1 = 49
num2 = 74
num3 = 53

formula_numerical = 49 - (- 74 + 53)

print "The answer is:", formula_numerical

formula_variable = subtract(num1, add(- num2, num3))

print "The answer is:", formula_variable
