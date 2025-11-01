import os, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
out = ROOT / "code_golf_release.zip"
keep = ["src", "tasks", "reports", "solutions_auto"]
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for k in keep:
        for root,_,files in os.walk(ROOT/k):
            for f in files:
                full = Path(root)/f
                rel = full.relative_to(ROOT)
                # flatten top-level dir name to code_golf
                z.write(full, arcname=str(Path("code_golf")/rel.relative_to(k if k!="src" else "src/code_golf")))
print("Wrote", out)
