#Just testing text based games again
import util
import levelLoader
import stats
import inventory as inv

while 1 == 1:
	currentLevel = util.getLevel()	
	#print(currentLevel)        

        action = raw_input("\nWhat do you want to do? ").lower()
	
	if action.replace("at", "in").replace(" your", "") == "look in inventory":
		inv.get()
	else:        
	        currentLevel.act(action)
        
        if stats.getHealth() < 1:
                print("You died.")
                exit(0)
