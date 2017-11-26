import levelLoader
def setLevel(level):
	global currentLevel
	currentLevel = getattr(levelLoader, level)
	#print(currentLevel)
	currentLevel.info()
	return currentLevel

def getLevel():
	global currentLevel
	#print(currentLevel)
	return currentLevel
