# https://www.codewars.com/kata/5f70c883e10f9e0001c89673 "Gravity Flip | Codewars" 
# +---+                                       +---+
# |   |                                       |   |
# +---+                                       +---+
# +---++---+     +---+              +---++---++---+
# |   ||   |     |   |   -->        |   ||   ||   |
# +---++---+     +---+              +---++---++---+
# +---++---++---++---+         +---++---++---++---+
# |   ||   ||   ||   |         |   ||   ||   ||   |
# +---++---++---++---+         +---++---++---++---+
# Given the initial configuration of the cubes in the box, find out how many cubes are in each of the n columns after Bob switches the gravity.
# 
# Examples (input -> output:
# * 'R', [3, 2, 1, 2]      ->  [1, 2, 2, 3]
# * 'L', [1, 4, 5, 3, 5 ]  ->  [5, 5, 4, 3, 1]

def flip(d, a):
	'''
		1. old columnCntList -> floorCntList
		2. floorCntList -> new columnCntList
	'''
	height=max(a)
	# folor number: [0, height-1]
	floorCntList=[0 for i in range(height)]

	for columnCnt in a:
		for floorIndex in range(columnCnt):
			floorCntList[floorIndex]+=1
	
	columnCntList=[0 for i in range(len(a))]
	if d=='R':
		for columnIndex in range(len(columnCntList))[::-1]:
			columnCntList[columnIndex]=len(floorCntList)
			floorCntList=[x-1 for x in floorCntList if x>1]
	else:
		for columnIndex in range(len(columnCntList)):
			columnCntList[columnIndex]=len(floorCntList)
			floorCntList=[x-1 for x in floorCntList if x>1]
	
	return columnCntList

if __name__ == '__main__':
	assert flip('R', [3, 2, 1, 2]) == [1, 2, 2, 3]
	assert flip('L', [1, 4, 5, 3, 5 ]) == [5, 5, 4, 3, 1]















