# Ex19: Functions & Variables

def tourist_transport(number_of_people, car_space, number_of_cars):
    print "We have %s people." % number_of_people
    print "Each car can fit %s people." % car_space
    print "So we need %s car(s).\n" % number_of_cars


print "#1: Using numbers as parameters:"
tourist_transport(40, 4, 10)

print "#2: Using sums as parameters:"
tourist_transport(11 + 9, 5 - 1, 20.0 / 4.0) # why is the division incorrect

print "#3: User input:"
car_capacity = 4
total_people = int(raw_input("Total no. of people > "))
cars_required = total_people / car_capacity

tourist_transport(total_people, car_capacity, cars_required)

print "#4: Using strings as parameters:" # because I'm running out of ideas lol
tourist_transport("Valmik, Indrani, Shubham, which makes three", "four", "one")
