def manticore():
    print "You come across a sleeping manticore."
    print "Do you try to sneak or run past it?"

    next = raw_input("> ")

    if next == "sneak":
        "You successfully make your way across! Phew."
        oasis()

    elif next == "run":
        dead("You wake the manticore up, who rips you apart with its claws.")
