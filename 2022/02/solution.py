inputFile = open("input.txt", "r")


winningTable = {
	"A": {"X": 3, "Y": 6, "Z": 0},
	"B": {"X": 0, "Y": 3, "Z": 6},
	"C": {"X": 6, "Y": 0, "Z": 3}
}

moveScoreTable = {
	"X": 1,
	"Y": 2,
	"Z": 3
}

outcomeTable = {
	"X": 0,
	"Y": 3,
	"Z": 6
}

correctMoveTable = {
	"A": {"X": 3, "Y": 1, "Z": 2},
	"B": {"X": 1, "Y": 2, "Z": 3},
	"C": {"X": 2, "Y": 3, "Z": 1}
}

def GetWinningScore(oppaonent, me):
	return winningTable[opponent][me]

def GetMoveScore(move):
	return moveScoreTable[move]

def GetResultFromOutcome(outcome):
	return outcomeTable[outcome]

def GetScoreFromCorrectMove(opponent, outcome):
	return correctMoveTable[opponent][me]

score = 0
realScore = 0
for line in inputFile:
	opponent = line[0]
	me = line[2]

	score += GetWinningScore(opponent, me)
	score += GetMoveScore(me)

	realScore += GetResultFromOutcome(me)
	realScore += GetScoreFromCorrectMove(opponent, me)


print("My score would be " + str(score))
print("My real score will be " + str(realScore))