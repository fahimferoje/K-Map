from solvers import KMapSolver4
all_vars = 'A, B, C, D'
KMapSolver = KMapSolver4
##fahi = KMapSolver4
my_data=[[0,0,0,0],[2,1,0,0],[1,0,0,1],[0,0,2,1]]
print my_data
k = KMapSolver(my_data)
k.solve()
