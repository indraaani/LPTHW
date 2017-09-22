# Ex31: Making Decisions
# Study Drill: Make new parts of the game.

print """
You enter a dark room with three doors.
Do you go through door #1, #2 or #3?
"""

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
        print "You stare into the endless abyss at Cthulu's retina."
        print "1. Blueberries."
        print "2. Yellow jacket clothespins."
        print "3. Understanding revolvers yelling melodies."

        insanity = raw_input("> ")

        if insanity == "1" or insanity == "2":
            print "Your body survives powered by a mind of jello. Good job!"
        else:
            print "The insanity rots your eyes into a pool of muck. Good job!"

elif door == "3":
    print """
    You come across a group of four strange-looking adventurers, fighting a monster.
    What do you do?
    """
    print "1. Run forward to fight the monster."
    print "2. Scream to get the monster's attention."
    print "3. Stand and watch."

    aid = raw_input("> ")

    if aid == "1":
        print "The five of you successfully slay the monster!"
        print "What do you do next?"
        print "1. Introduce yourself."
        print "2. Ask them who they are."
        print "3. Ask them for a way out."

        talk = raw_input("> ")

        if talk == "1" or talk == "2":
            print 'They respond, "Our names are Marn, Viggo, Liarel and Dorn! Thank you for your aid!"'

        else:
            print 'They respond, "We too are looking for a way out. Come join us."'

    elif aid == "2" or aid == "3":
        print "The monster leaps towards you and bites your head off. Rest in peace!"


else:
    print "You stumble around and fall on a knife and die. Good job!"
