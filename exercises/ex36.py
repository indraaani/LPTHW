# Ex36: Designing and Debugging

from sys import exit

inventory = ['knife', 'waterskin', 'bedding', 'rations', 'firewood']

def manticore():
    print "You come across a sleeping manticore."
    print "Do you try to sneak or run past it?"

    next = raw_input("> ")

    if next == "sneak":
        "You successfully make your way across! Phew."
        oasis()

    elif next == "run":
        dead("You wake the manticore up, who rips you apart with its claws.")

    else:
        dead("As you wait around, the manticore awakens and devours you into pieces.")


def adventurers():
    print "You come across a group of adventurers."
    print "Do you eavesdrop or talk to them?"

    next = raw_input("> ")

    if next == "eavesdrop":
        print "You hear them talk about a manticore they wish to fight."
        print "The dragonborn notices your presence, walking over to you."
        print "He grabs you by your collar, yelling, 'What do you think you're doing?!'"
        dead("Lowering his mask, he uses chill-breath on you, freezing you to death.")

    elif next == "talk":
        print '"Our names are Marn, Dorn, Liarel and Viggo," says a graceful, lean elf.'
        print '"We\'re here to defeat the evil Cthulu," chimes in Viggo the dwarf.'
        print '"Join us, and you will be heavily rewarded for your efforts." Nods the gruff-sounding Marn.'
        print '"And who are you?" asks Dorn.',
        name = raw_input("You nervously say...")
        print '"It is an honour to make your acquaintance, %s" says Liarel the elf.' % name

    else:
        dead("As you're stumbling around, you're stung by a deadly wasp! Rest in pieces.")


def oasis():
    print "You walk towards a beautiful lake, surrounded by trees and foilage."
    print "What do you wish to do? Rest or continue to walk?"

    next = raw_input("> ")

    if next == "rest":
        print "You fall into a deep slumber. zzZzzzZZzzz"
        print "You awaken when you hear loud, thudding sounds around you."
        print "Groggily rubbing your eyes, you notice a troll heading towards you!"
        print "What do you do? Intimidate or fight the troll?"
        troll_intimidated = False

        while True:
            next = raw_input("> ")

            if next == "fight":
                dead("The troll steps on you and squashes you to mush. Rest in pieces!")
            elif next == "intimidate" and not troll_intimidated:
                print "The dumb troll, afraid of you, gives you his spiked club and leaves."
                troll_intimidated = True
                item1 = 'spiked club'
                inventory.append(item1)
                print "Your current inventory is:", inventory
                print "You make your way through the oasis and come across some adventurers."
                adventurers()
            elif next == 'intimidate' and troll_intimidated:
                dead("The troll, unfazed, swings his club at you and breaks your neck.")
            else:
                dead("The troll notices you and throws rocks at you.")

    elif next == "walk":
        adventurers()

    else:
        dead("As you stumble around, a venomous pixie bites you! Rest in pieces!")


def check_inventory():
    print "Check your inventory to see what the bag contains."

    next = raw_input("> ")

    if next == "check inventory":
        print "Here's your inventory:"
        print "\n".join(inventory)

    else:
        "Fine, don't."

def dead(reason):
    print reason, "Try again!"
    exit(0)

def start():
    print "You're standing in a dim-lit clearing, with a small bag of items."
    check_inventory()
    print "There are two roads; one to your right, the other to your left."
    print "Which road do you take?"

    next = raw_input("> ")

    if next == "right":
        oasis()

    elif next == "left":
        manticore()

    else:
        dead("You stumble around until you fall into a pit. Rest in pieces!")

start()
