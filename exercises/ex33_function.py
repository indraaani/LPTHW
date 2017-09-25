def make_number(max, add):
    i = 0
    numbers = []
    for i in range(0, max, add):
        print "At the top i is %d" % i
        numbers.append(i)

        print "Numbers now: ", numbers
        print "At the bottom, i is %d" % i
    return numbers

numbers = make_number(7, 1)

print "The numbers:"

for num in numbers:
    print num
