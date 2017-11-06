# Ex39: Dictionaries, Oh Lovely Dictionaries
# Study Drill: Map cities and states/regions in your country or in some other country.

# mapping of state to abbreviation
states = {
    'Maharashtra': 'MH',
    'West Bengal': 'WB',
    'Delhi': 'DEL',
    'Tamil Nadu': 'TN',
    'Rajasthan': 'RJ'
}

# set of states and some cities in them
cities = {
    'MH': 'Mumbai',
    'TN': 'Chennai',
    'RJ': 'Jaipur',
}

# add some more cities
cities['DEL'] = 'New Delhi'
cities['WB'] = 'Kolkata'

# print out some cities
print '-' * 10
print "DEL State has: ", cities['DEL']
print "MH State has: ", cities['MH']

# print out some states
print '-' * 10
print "Tamil Nadu's abbreviation is: ", states['Tamil Nadu']
print "West Bengal's abbreviation is: ", states['West Bengal']

# do it by using the state then cities dict
print '-' * 10
print "Rajasthan has: ", cities[states['Rajasthan']]
print "Maharashtra has: ", cities[states['Maharashtra']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# both at the same time
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])
