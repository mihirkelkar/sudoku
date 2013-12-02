The first program called AI_q2.py is the code which contains implicit constraints and solves the code by propogating the constraints using AC3. It initlially assigns all possible to values to a cell in the grid and knocks out all impossible values based on its negihbours and propagates this forward till the entire puzzle is solved.

In the second program, I have used a python module called constraints used specifically for constraints programming in python. Here I use the commands in the module to very explicitly mention all three constraints in solving the sudoku and propagate these all throughout the grid. I have included the module called constraints in the tarball. All that is required to run this code is to execute the command, python AI_q3.py

Mihir Kelkar 
