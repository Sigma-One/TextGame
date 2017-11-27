#base for levels

#import stats
#import util
#import inventory as inv

class levelBase():
	
        desc = "SAMPLE DESCRIPTION"
	def act(self, action):

# INSPECT <FOO> # ---------------------------------------------------------------------------------

		if action.startswith("inspect"):
                        try:
                		print("\n" + getattr(self, action.split(" ", 1)[1]).desc)
                        except AttributeError:
	                	print("\nCan't inspect nonexistent object.")
			


# LOOK AROUND # -----------------------------------------------------------------------------------

		if action == "look around":
			print("\n" + self.desc)



# PICK UP <BAR> # ---------------------------------------------------------------------------------

		if action.startswith("pick up"):
                        try:
                		inv.add("\n" + getattr(self, action.replace(" the", "").split(" ", 2)[1]))
                                del self.action.replace(" the", "").split(" ", 2)[1])
                        except AttributeError:
	                	print("\nCan't pick up nonexistent object.")


# GO TO <BAZ> # -----------------------------------------------------------------------------------
baz = levelBase()

bar = raw_input()
baz.act(bar)
