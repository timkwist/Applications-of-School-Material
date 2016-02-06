class StrategicForm:
	def __init__(self):
		self.matrix = {}

	def addEntry(self, pOneStrat, pTwoStrat, payoff):
		self.matrix[pOneStrat] = {pTwoStrat: payoff}

	def getPayoff(self, pOneStrat, pTwoStrat):
		return self.matrix[pOneStrat][pTwoStrat]

prisonersDilemma = StrategicForm()
prisonersDilemma.addEntry("Testify", "Testify", [-2, -2])
print(prisonersDilemma.getPayoff("Testify", "Testify"))