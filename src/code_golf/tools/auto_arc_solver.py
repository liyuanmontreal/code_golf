import json,csv
from pathlib import Path
from code_golf.dsl.search import search_solution
from code_golf.dsl.codegen import seq_to_code

ROOT=Path(__file__).parent.parent.parent
TASKS=ROOT/'tasks'; SOL=ROOT/'solutions_auto'; REP=ROOT/'reports'
SOL.mkdir(exist_ok=True); REP.mkdir(exist_ok=True)

def run_task(path):
    d=json.load(open(path))
    inp=d['train'][0]['input']; out=d['train'][0]['output']
    seq=search_solution(inp,out,3)
    if seq:
        code=seq_to_code(seq)
        (SOL/(path.stem+'.py')).write_text(code+'\n')
        return True,[f.__name__ for f in seq],len(code)
    return False,None,None

def main():
    rows=[]; tasks=sorted(TASKS.glob('*.json'))
    print(f'Found {len(tasks)} tasks')
    for t in tasks:
        ok,seq,cl=run_task(t)
        print('✅' if ok else '❌',t.name,seq)
        rows.append([t.name,ok,','.join(seq) if seq else '',cl or ''])
    out=REP/'auto_summary.csv'
    import csv
    with open(out,'w',newline='',encoding='utf-8') as f:
        csv.writer(f).writerows([['task','solved','sequence','code_length'],*rows])
    print('Report:',out)

if __name__=='__main__':main()
