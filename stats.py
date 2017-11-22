#Stats script

health = 100

def heal(hp):
    global health
    health += hp
    print("\nYou gained " + str(hp) + " health.")
    print("You now have " + str(health) + " health.\n")

def damage(hp):
    global health
    health -= hp
    print("\nYou lost " + str(hp) + " health.")
    print("You now have " + str(health) + " health.")

def getHealth():
    global health
    return health
