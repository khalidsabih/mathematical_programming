from scipy.optimize import linprog

# coeficients of the objective function
obj = [1, 2]
# left side coeficients of the inequity constraints
lhs_ineq = [
    [1, 0],
    [-1, 1],
    [1, -1],
    [1, 2]
]
# right sides of the inequity constraints
rhs_ineq = [
    3,
    2,
    1,
    10
]

# minimize the objective function
opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, method="revised simplex")
print("Minimization of the objective function:\n", opt)

# maximize the objective function
nobj = [-1, -2] # the objective function multiplied by (-1)
opt = linprog(c=nobj, A_ub=lhs_ineq, b_ub=rhs_ineq, method="revised simplex")
print("Maximization of the objective function:\n", opt)