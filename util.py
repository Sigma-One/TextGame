import levelLoader
def setLevel(level):
	try:
		global currentLevel
		currentLevel = getattr(levelLoader, level)
		#print(currentLevel)
		currentLevel.info()
		return currentLevel
	except AttributeError:
		print("ERROR: No level named " + level + ". Please inform the developer if you are a player or fix the issue if you are a developer.")
def getLevel():
	global currentLevel
	#print(currentLevel)
	return currentLevel
