class KuhnTree:
	def __init__(self, player = None, possibleOptions = {}):
		self.currentPlayer = player
		self.possibleOptions = possibleOptions
	
	def addOption(self, name, newOption):
		self.possibleOptions[name] = newOption
		
	def printTree(self, currentNode = 0):
		for key, value in self.possibleOptions.items():
			if type(value) is KuhnTree:
				print("At node", currentNode, ", Player", self.currentPlayer, "can chose the option of", key,
				"leading to the following options:")
				value.printTree(currentNode + 1)
			else:
				print("At node", currentNode, ", Player", self.currentPlayer, "can chose the option of", key,
				"leading to a payoff of", value)
				
	def simplePrintTree(self, pastString="", level = 0):
		for key, value in self.possibleOptions.items():
			if type(value) is list:
				print("%s %s:%s --> %s" % (pastString, self.currentPlayer, key, value))
			else:
				value.simplePrintTree(pastString + "%s:%s --> " % (self.currentPlayer, key), level=level+1)

prisonersDilemma = KuhnTree(player = 1, 
						    possibleOptions = {
									"Testify": KuhnTree(player = 2,
														possibleOptions = {
																"Testify": [-2, -2],
																"Don't Testify": [0, -3]
																}), 
									"Don't Testify": KuhnTree(player = 2,
															possibleOptions = {
																	"Testify": [-3, 0],
																	"Don't Testify": [1, 1]
															})
									})
prisonersDilemma.printTree()
prisonersDilemma.simplePrintTree()
