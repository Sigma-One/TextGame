#Spawn area
import stats
import util
import inventory as inv

curtainsOpen = False

print("\nYou are in your bedroom. You have been stuck here for two hours now because you lost the key to the door.")

def act(action):
        action = action.lower()
        
        global curtainsOpen
        
	if action == "look around":
		print("\nThere is a bed and a window" + (". " if curtainsOpen else " with curtains over it. ") + "There is also a door next to the window and another one on the opposite side of the room.")
                
	elif action.replace(" the", "") == "open curtains":
                if not curtainsOpen:
                	print("\nYou opened the curtains. You can see into your back yard.")
                	curtainsOpen = True
                else:
                        print("\nThe curtains are already open. You can see into your back yard.")

	elif action.replace(" the", "") == "close curtains":
                if curtainsOpen:
                	print("\nYou closed the curtains. You can no longer see through the window.")
                	curtainsOpen = False
                else:
                        print("\nThe curtains are already closed. You can't see through the window.")

        elif action.replace(" the", "") == "look through window":
                if curtainsOpen:
                        print("\nYou look through the window. You can see into your back yard.")
                else:
                        print("\nYou can't see anything trough the window because there are curtains in the way.")

        elif action.replace(" the", "") == "walk through door next to window":
                print("\nYou walked through the door next to the window.")
                util.setLevel(backYard)
                
        elif action.replace(" the", "") == "walk through door":
                print("\nPlease specify which door to walk through.")
