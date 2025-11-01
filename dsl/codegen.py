def seq_to_code(seq):
    n=[f.__name__ for f in seq]
    expr="(".join(reversed(n))+"(g"+")"*len(n)
    return "def solve(g):return "+expr
