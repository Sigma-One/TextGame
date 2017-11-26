#Spawn area
import stats
import util
import inventory as inv

class main():
	global curtainsOpen
	global livingRoomLocked
	curtainsOpen = False
	livingRoomLocked = True	

	#prints quick location info
	def info(self):
		print("\nYou are in your bedroom.")

	#if statements for all the actions
	def act(self, action):
        	global curtainsOpen
        
		
		#player looks around
		if action == "look around":
			print("\nThere is a bed and a window" + (". " if curtainsOpen else " with curtains over it. ") + "There is also a door leading to your back yard next to the window and another one leading to your living room on the opposite side of the room.")
        

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

		#player tries to go to their living room
		elif action.replace(" the", "") == "go to living room":
			if inv.hasItem("living room key") and livingRoomLocked:
				print("\nYou unlock the door and walk through it into your living room.")
				util.setLevel("livingroom")
				inv.remove("living room key")
			elif not livingRoomLocked:
				print("\nYou walk through the door into your living room.")
				util.setLevel("livingroom")
			else:
				print("The door is locked. Maybe there is a key somewhere?")
