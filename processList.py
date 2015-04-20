def processList(inputList = ''):
	# Determine the length of the list
	nItems = len(inputList)
	# Order the list
	inputList.sort()
	# Create a list dictionary framework
	processDictionary = {}

	# Now loop through each item in the list and count entries
	for i in range(nItems):
		if(i == 0):
			processDictionary[inputList[i]] = 1
		else:
			# Check if the entry is in the dictionary already and
			# increment if so
			if(processDictionary.has_key(inputList[i])):
				currentCount = processDictionary[inputList[i]] + 1
				processDictionary[inputList[i]] = currentCount
			# It doesn't, so add a fresh entry
			else:
				processDictionary[inputList[i]] = 1

	return processDictionary


def main():
	# Define a test list
	testList = ['a', 'b', 'a', 'a', 'c', 'c', 'q', 'q']
	# Submit it to the 'processList function'
	dList = processList(testList)
	# Sort the dictionary and print for user
	print sorted(dList.iteritems(), key=lambda key_value: key_value[0])

if __name__ == "__main__":
	main()