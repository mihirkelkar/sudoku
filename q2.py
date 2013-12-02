#!/usr/bin/python

def cross(A, B):
	temp = []
	#print A
	#print "\n"
	#print B
	#print "\n"
	for i in A:
		for j in B:
			temp.append(i + j)

	#print temp
	return temp

digits = '123456789'
rows = 'ABCDEFGHI'
cols = digits
squares = cross(rows, cols)
unit_list = ([cross(rows, c) for c in cols] + [cross(r, cols) for r in rows] + [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')])
units = dict((s, [u for u in unit_list if s in u]) for s in squares)
peers = dict((s, set(sum(units[s], []))- set([s]))for s in squares)

#print units
#print peers

def parse_grid(grid):
	val = dict((s,digits) for s in squares)
	#print val
	grid_val_tuplist =  grid_vals(grid).items()
	for ele in grid_val_tuplist:
		if ele[1] in digits and not setval(val, ele[0], ele[1]):
			return False
	return val

def grid_vals(grid):
	"""Simply convert a grid into a dict"""
	letters = list(grid)
	#print "---------------------------------\n-------------------"
	#print letters
	#print "----------------------------------\n-------------------"
	assert len(letters) == 81
	tempdict = zip(squares, letters)
	return dict(tempdict)

def setval(val, s, n):
	other_val = val[s].replace(n, '')
	if all(remove(val, s, n2) for n2 in other_val):
		return val
	else:
		return False

def remove(val, s, n):
	if n not in val[s]:
		return val
	val[s] = val[s].replace(n, '')
	if len(val[s]) == 0:
		return False
	elif len(val[s]) == 1:
		n2 = val[s]
		if not all(remove(val, s2, n2) for s2 in peers[s]):
			return False
	for u in units[s]:
		dplaces = [s for s in u if n in val[s]]
		if len(dplaces) == 0:
			return False
		elif len(dplaces) == 1:
			if not setval(val, dplaces[0], n):
				return False
	return val

def show(val):
	for i in 'ABCDEFGHI':
		for j in '123456789':
			temp = i + j
			print val[temp] + ' |',
		print "\n"
def displaygridip(grid):
	temp = [grid[i : i + 9] for i in range(0, len(grid), 9)]
	dgrid = []
	for i in temp:
		templist = []
		templist = list(i)
		dgrid.append(templist)
	for i in dgrid:
		for j in i:
			print j + "|",
		print "\n"
grid1 = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'
grid2 = "000083400300004821700000000009401083000000000460507100000000007125300009007240000"
grid3 = "500802007409513000080000000900001700360090021005200004000000070000937208800104006"
grid4 = "000000070090504003000002560003000810001739400059000600087200000900803050020000000"
count = 0
while(1):
	if count != 0:
		print "^^^^ THE OUTPUT FOR THE LAST CASE YOU SOLVE HAS BEEN PRINTED ABOVE ^^^^"

		print 
		print
	print "-----------------------------------------------------------------------------------------"
	print "\tSolve the following sudokus or enter your own input\n"
	choice = input("1.Press 1 to solve the first input in the HW Question\n2.Press 2 to solve the second input in the HW Question\n3.Press 3 to solve the third input in the HW.\n4.Press 4 to enter your own input")
	#displaygridip(grid1)
	#show(parse_grid(grid1))
	print "-------------\n--------------\n---------------\n"
	if choice == 1:
		print "Test case 1\n"
		show(parse_grid(grid2))
		print "-------------\n--------------\n---------------\n"
		print "Case 1 has been solved"
		count = count + 1
	elif choice == 2:
		print "Test case 2\n"
		show(parse_grid(grid3))
		print "-------------\n--------------\n---------------\n"
		print "Solved the grid for Case 2"
		count = count + 1
	elif choice == 3:
		print "Test case 3\n"
		show(parse_grid(grid4))
		print "-------------\n--------------\n---------------\n"
		print "CASE 3 DONE"
		count = count + 1
	elif choice == 4:
		print "You have chosen to input your own grid.\n the acceptable form of input is a single string of length 81 charecters where 0 represents a blank spot\n"
		print "As an example \n a grid input looks like\n 003020600900305001001806400008102900700000008006708200002609500800203009005010300"
		grid = raw_input("Enter your grid")
		if len(grid) == 81:
			show(parse_grid(grid))
			count = count + 1
		else:
			print "Wrong grid input, length not 81\n"
			count = count + 1
	elif choice not in [1,2,3,4]:
		print "You did not select a proper menu option\n"
