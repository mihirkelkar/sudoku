#Getting python constraint, the ./python-constraint-1.1 contains constraint.py file
import sys, math
import subprocess 
#Importing constraint
try:
	sys.path.append("./constraints")
	from constraint import *
except ImportError:
	print "You do not have the Python Constraint module. You need to run the following command to install it. I have included the setup file with the source code. Please run \nsudo python constraints/setup.py install. You will then be able to use the code."
	sys.exit()
 
def solver_Sudoku(size = 9, sudogame = None):
    """ Solving Sudoku of any size """
    chunk, chunksize = len(sudogame), len(sudogame) / 9
    temp = [(sudogame[i:i + chunksize]) for i in range(0, chunk, chunksize)]
    temp2 = [list(i) for i in temp]
    game = []
    for key1 in temp2:
	temp3 = []
	for key2 in key1:
		temp3.append(int(key2))
	game.append(temp3)
    sudoku = Problem()
    lineSum = sum([1,2,3,4,5,6,7,8,9])
    #Defining size of row/col
    rows = [0,1,2,3,4,5,6,7,8]
    cols = [0,1,2,3,4,5,6,7,8]
    #Creating board
    board = []
    for row in rows:
	for col in cols:
		temp = (row, col)
		board.append(temp)
    #Defining game variable, a single range will be enough
    sudoku.addVariables(board, range(1, size * size + 1))
 
    #Row set
    rowSet = [zip([el] * len(cols), cols) for el in rows]
    colSet = [zip(rows, [el] * len(rows)) for el in cols]
 
    #The original board is not empty, we add that constraint to the list of constraint
    if game is not None:
        for i in range(0, size):
            for j in range(0, size):
                #Getting the value of the current game
                o = game[i][j]
                #We apply constraint when the number is set only
                if o > 0:
                    #We get the associated tuple
                    t = (rows[i],cols[j])
                    #We set a basic equal constraint rule to force the system to keep that variable at that place
                    sudoku.addConstraint(lambda var, val=o: var == val, (t,))
 
    #The constraint are like that : and each row, and each columns, got same final compute value, and are all unique
    for row in rowSet:
        sudoku.addConstraint(ExactSumConstraint(lineSum), row)
        sudoku.addConstraint(AllDifferentConstraint(), row)
    for col in colSet:
        sudoku.addConstraint(ExactSumConstraint(lineSum), col)
        sudoku.addConstraint(AllDifferentConstraint(), col)
 
    #Every sqrt(size) (3x3 box constraint) got same sum
    sqSize = int(math.floor(math.sqrt(size)))
 
    #xrange allow to define a step, here sq (wich is sq = 3 in 9x9 sudoku)
    for i in xrange(0,size,sqSize):
        for j in xrange(0,size,sqSize):
            #Computing the list of tuple linked to that box
            box = []
            for k in range(0, sqSize):
                for l in range(0, sqSize):
                    #The tuple i+k, j+l is inside that box
                    box.append( (i+k, j+l) )
            #Compute is done, now we can add the constraint for that box
            sudoku.addConstraint(ExactSumConstraint(lineSum), box)
            sudoku.addConstraint(AllDifferentConstraint(), box)
 
    #Computing and returning final result
    return sudoku.getSolution()

 
rg = 9
game =  "000083400300004821700000000009401083000000000460507100000000007125300009007240000"
test1 = "000083400300004821700000000009401083000000000460507100000000007125300009007240000"
test2 = "500802007409513000080000000900001700360090021005200004000000070000937208800104006"
test3 = "000000070090504003000002560003000810001739400059000600087200000900803050020000000"
def printer(res):
        for i in range(0, rg):
                for j in range(0, rg):
                        print res[i, j],
                print
        print

print "\t------------------------------------------------------------------\n"
print "Solve Sudokus where the constraints have been explicitly coded using the constraint module of python\n"
choice = input ("1.Press 1 to solve the First case in HW\n2.Press 2 to solve the Second case in HW\n3.Press 3 to solvethe Third case in the Homework\n4.Press 4 to enter your own input grid\n")
if choice == 1:
	res = solver_Sudoku(rg, test1)
	printer(res)
	print "-------------------------------------------------------------------------\n"
	print "CASE 1 HAS BEEN SOLVED\n"
elif choice == 2:
	res = solver_Sudoku(rg, test2)
	printer(res)
	print "-------------------------------------------------------------------------\n"
	print "Solved the second case\n"
elif choice == 3:
	res = solver_Sudoku(rg, test3)
	printer(res)
	print "------------------------------------------------------------------------\n"
	print "Solved Case 3\n"
elif choice == 4:
	print "You have chosen to provide your own input grid\n"
	print "The acceptable form of an input is a single string of 81 charecters with 0 representing a balnk spot\n"
	print "An example of a acceptable input is shown below\n000083400300004821700000000009401083000000000460507100000000007125300009007240000\n"
	grid = raw_input("Enter your input")
	res = solver_Sudoku(rg, grid)
	printer(res)
