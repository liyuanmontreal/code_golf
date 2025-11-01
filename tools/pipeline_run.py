import os,json,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pandas as pd,matplotlib.pyplot as plt
from pathlib import Path

ROOT=Path(__file__).parent.parent
REP=ROOT/"reports"/"auto_summary.csv"
CH=ROOT/"reports"/"charts"; TASKS=ROOT/"tasks"
CH.mkdir(exist_ok=True)

def run_solver():
    os.system(f"python {ROOT/'tools'/'auto_arc_solver.py'}")

def charts():
    df=pd.read_csv(REP)
    df["solved"]=df["solved"].astype(bool)
    df["code_length"]=pd.to_numeric(df["code_length"],errors="coerce").fillna(0)
    # pie
    plt.figure(figsize=(4,4))
    s=df["solved"].sum();u=len(df)-s
    plt.pie([s,u],labels=["Solved","Unsolved"],autopct="%1.1f%%")
    plt.title("Success Rate");plt.savefig(CH/"success.png");plt.close()
    # hist
    plt.figure(figsize=(5,4))
    vals=df[df["solved"]==True]["code_length"].values
    if len(vals)>0: plt.hist(vals,bins=min(10,len(vals)))
    plt.title("Code Length");plt.savefig(CH/"length.png");plt.close()
    # example
    st=df[df["solved"]==True]["task"].tolist()
    if st:
        t=st[0]; data=json.load(open(TASKS/t))
        inp=data["train"][0]["input"];out=data["train"][0]["output"]
        fig,ax=plt.subplots(1,2,figsize=(4,2))
        ax[0].imshow(inp);ax[0].set_title("Input")
        ax[1].imshow(out);ax[1].set_title("Output")
        for a in ax: a.set_xticks([]);a.set_yticks([])
        plt.tight_layout();plt.savefig(CH/f"example_{t}.png");plt.close()

def main(): run_solver();charts();print("✅ pipeline done")
if __name__=="__main__":main()
