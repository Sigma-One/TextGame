#Spawn area
import stats

print("\nyou are standing in a pile of crappy debug sample text.")

def act(action):
	if action.lower() == "look around":
		print("\nThere are a bunch of debug texts.")
	elif action.lower() == "damage":
                print("\nYou stabbed yourself with a debug text.")
                stats.damage(10)
