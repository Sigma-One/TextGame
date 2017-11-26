#Spawn area
import stats
import util
import inventory as inv

class main():
	global curtainsOpen
	curtainsOpen = False
	
	#prints quick location info
	def info(self):
		print("\nYou are in your bedroom.")

	#if statements for all the actions
	def act(self, action):
        	global curtainsOpen
        
		
		#player looks around
		if action == "look around":
			print("\nThere is a bed and a window" + (". " if curtainsOpen else " with curtains over it. ") + "There is also a door leading to your back yard next to the window and another one on the opposite side of the room.")
        

        	#player opens curtains"
		elif action.replace(" the", "") == "open curtains":
        	        if not curtainsOpen:
        	        	print("\nYou opened the curtains. You can see into your back yard.")
        	        	curtainsOpen = True
        	        else:
        	                print("\nThe curtains are already open. You can see into your back yard.")


		#player closes curtains
		elif action.replace(" the", "") == "close curtains":
        	        if curtainsOpen:
        	        	print("\nYou closed the curtains. You can no longer see through the window.")
        	        	curtainsOpen = False
        	        else:
        	                print("\nThe curtains are already closed. You can't see through the window.")


		#player looks through window
        	elif action.replace(" the", "") == "look through window":
        	        if curtainsOpen:
        	                print("\nYou look through the window. You can see into your back yard.")
        	        else:
        	                print("\nYou can't see anything trough the window because there are curtains in the way.")


		#player goes to their back yard
		elif action.replace(" the", "") == "go to backyard" or action == "go outside":
			print("\nYou walk through the door leading to your back yard.")
			util.setLevel("backyard")
