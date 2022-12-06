inputFile = open("input.txt", "r")
currentCalories = 0
allCalories = []
for line in inputFile:
	if (not line.strip()):
		allCalories.append(currentCalories)
		currentCalories = 0
		continue

	currentCalories += int(line)

allCalories.append(currentCalories)
allCalories.sort(reverse=True)

print("Top calories is: " + str(allCalories[0]))

sumCalories = 0
for i in range(3):
	sumCalories += allCalories[i]

print("Top 3 calories sum is: " + str(sumCalories))