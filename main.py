#Just testing text based games again

print("starting game")

import inventory as inv
print("Inventory loaded.")

def setLevel(level):
	global lvl
	lvl = __import__(level)

setLevel("spawnArea")	

action = raw_input("What do you want to do?")

lvl.act(action)


