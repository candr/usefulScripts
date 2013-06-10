def divideInto3Slots(value, key):
	start = key%3
	keyExp = 1
	k = key
	while k/3 != 0:
		keyExp += 1
		k = k/3

	slotted = [0,0,0]
	
	if keyExp == 1:
		slotted[start] = value
		return slotted
	elif (key/3 - keyExp) == 0:
		slotted[start] = value - (keyExp-1)
	else:
		slotted[start] = keyExp-1

	value -= slotted[start]
	
	if key < 9:
		slotted[(start+1)%3] = value
	else:
		sval = value/2
		slotted[(start+1)%3] = sval + (value%2)
		slotted[(start+2)%3] = sval
		
			
	return slotted

def dashedLines(dashedArray, value):
	dashedString = "" 
	cursor = 0
	while value != 0:
		if dashedArray[cursor] != 0:
			if (cursor == 0):
				dashedString += "3,3"
			elif (cursor == 1):
				dashedString += "5,3"
			elif (cursor == 2):
				dashedString += "10,3"

			dashedArray[cursor]-= 1
			value-= 1

			if value != 0:
				dashedString += ","

		cursor = (cursor+1)%3

	return dashedString
	

if __name__ == "__main__":
	print "2 space"
	for i in range(6):
		print "{0} {1}".format(divideInto3Slots(2, i), dashedLines(divideInto3Slots(2, i), 2))

	print "\n\n 3 space"
	for i in range(10):
		print "{0} {1}".format(divideInto3Slots(3, i), dashedLines(divideInto3Slots(3, i), 3))


	print "\n\n 4 space"
	for i in range(12):
		print "{0} {1}".format(divideInto3Slots(4, i), dashedLines(divideInto3Slots(4, i), 4))
