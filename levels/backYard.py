#Spawn area
import stats
import util
import inventory as inv

class main():
	global hasKey
	hasKey = True

	#prints quick location info
	def info(self):
		print("\nYou are in your back yard.")

	#if statements for all the actions
	def act(self, action):
        	global hasKey


		#player looks around	        
		if action == "look around":
			print("\nThere is a forest on the edge of your back yard. There are also some flowers and grass, a small porch, and some garden furniture. On your house there is a window and a door into your bedroom." + (" You can also see a small key on the porch." if hasKey else ""))
             

		#player picks up key        
		elif action.replace(" the", "") == "pick up key":
        	        if hasKey:
        	                print("\nYou pick up the key on the ground.")
				hasKey = False
				inv.add("Bedroom key")
        	        else:
        	                print("\nYou already picked up the key.")
	
        	        
		#player goes to their bedroom
		elif action.replace(" the", "") == "go to bedroom" or action.replace(" back", "") == "go inside":
			print("\nYou walk back inside through the door leading to your bedroom.")
			util.setLevel("spawn")
