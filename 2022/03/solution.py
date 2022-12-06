inputFile = open("input.txt", "r")

def LowerToNumber(ch):
	return ord(ch)-ord('a')+1

def UpperToNumber(ch):
	return (ord(ch)-ord('A') + 1) + 26

def CharToNumber(ch):
	if (ch.isupper()):
		return UpperToNumber(ch)

	return LowerToNumber(ch)

totalPriority = 0
linesArray = []
for line in inputFile:
	linesArray.append(line)
	div = len(line)/2
	left = line[0:div].strip()
	right = line[div:].strip()

	for ch in left:
		if (right.find(ch) != -1):
			totalPriority += CharToNumber(ch)
			break

print("Priority is " + str(totalPriority))

badgeSum = 0
content = inputFile.readlines()
for i in range(0, len(linesArray), 3):
	one = linesArray[i].strip()
	two = linesArray[i+1].strip()
	three = linesArray[i+2].strip()

	for ch in one:
		if (two.find(ch) != -1 and three.find(ch) != -1):
			badgeSum += CharToNumber(ch)
			break

print("Badge sum is " + str(badgeSum))