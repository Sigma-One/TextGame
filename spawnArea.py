#Spawn area

print("you are standing in a pile of crappy debug sample text.")

def act(action):
	if action.lower() == "look around":
		print("There are a bunch of debug texts.")
		act(action)
	elif action.lower() == "suicide":
		print("You stabbed yourself with a debug text")
