class StrategicForm:
	def __init__(self):
		self.matrix = {}

	def addEntry(self, pOneStrat, pTwoStrat, payoff):
		self.matrix[pOneStrat] = {pTwoStrat: payoff}

	def getPayoff(self, pOneStrat, pTwoStrat):
		return self.matrix[pOneStrat][pTwoStrat]

	def printMatrix(self):
		for key, value in self.matrix.items():
			for keyTwo, valueTwo in value.items():
				print("%s:%s --> %s" % (key, keyTwo, valueTwo))

	

prisonersDilemma = StrategicForm()
prisonersDilemma.addEntry("Testify", "Testify", [-2, -2])
print(prisonersDilemma.getPayoff("Testify", "Testify"))
prisonersDilemma.printMatrix()