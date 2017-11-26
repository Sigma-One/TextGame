#Just testing text based games again
import util

print("starting game")

import stats

util.setLevel("spawnArea")

while 1 == 1:	
        
        action = raw_input("\nWhat do you want to do? ")
        
        util.lvl.act(action)
        
        if stats.getHealth() < 1:
                print("You died.")
                exit(0)
