#Spawn area

class main(levelBase):

	#prints quick location info
	def info(self):
		print("\nYou are in your living room.")

	#if statements for all the actions
	def act(self, action):
    
		
		#player looks around
		if action == "look around":
			print("\nThere is a sofa in front of a small fireplace and a wide window. On the fireplace there is a photo and some matches. There is also a door leading to your bedroom opposite to the window, another door leading to a short hallway, and an opening leading to your kitchen opposite of the hallway door.")
        

        	#player opens curtains"
		elif action.replace(" the", "") == "inspect fireplace":
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
