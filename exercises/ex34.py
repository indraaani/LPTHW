# Ex34: Accessing Elements of Lists

animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

def print_animal(index):
    if index == 1:
        ordinal_num = "1st"
    elif index == 2:
        ordinal_num = "2nd"
    elif index == 3:
        ordinal_num = "3rd"
    else:
        ordinal_num = str(index)+"th"

    print "The animal at %d is the %s animal and is a %s." % (index-1, ordinal_num, animals[index-1])

for i in range(1, 7):
    print_animal(i)
