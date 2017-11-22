#Spawn area
import stats

print("\nYou are in your bedroom. You have been stuck here for two hours now because you lost the key to the door.")

def act(action):
	if action.lower() == "look aroundy":
		print("\nThere is a bed and a window with curtains over it. There is also a door next to the window and another one on the opposite side of the room.")
	elif action.lower() == "open the curtains":
                print("\nYou opened the curtains. You can see into your back yard.")
