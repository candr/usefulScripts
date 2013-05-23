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
		if (cursor == 0) and (dashedArray[0] != 0):
			dashedString += "3,3"
			dashedArray[0] -= 1
			value-= 1
		if (cursor == 1) and (dashedArray[1] != 1):
			dashedString += "5,3"
			dashedArray[1]-= 1
			value-= 1
		if (cursor == 2) and (dashedArray[2] != 2):
			dashedString += "10,3"
			dashedArray[2]-= 1
			value-= 1

		cursor = (cursor+1)%3
		if value != 0:
			dashedString += ","

	return dashedString
		
		
	  
	

if __name__ == "__main__":
	for i in range(15):
		print "{0} {1}".format(divideInto3Slots(5, i), dashedLines(divideInto3Slots(5, i), 5))
