from itertools import product
from .core import PRIMITIVES

def apply_ops(g,ops):
    for op in ops: g=op(g)
    return g

def search_solution(inp,out,max_depth=3):
    for d in range(1,max_depth+1):
        for seq in product(PRIMITIVES,repeat=d):
            try:
                if apply_ops(inp,seq)==out: return seq
            except: pass
    return None
