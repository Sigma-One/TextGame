#Just testing text based games again

print("starting game")

import inventory as inv
print("Inventory loaded.")

import stats
print("Stats loaded.")

def setLevel(level):
	global lvl
	lvl = __import__(level)

setLevel("spawnArea")

while 1 == 1:	
        
        action = raw_input("\nWhat do you want to do? ")
        
        lvl.act(action)
        
        if stats.getHealth() < 1:
                print("You died.")
                exit(0)
