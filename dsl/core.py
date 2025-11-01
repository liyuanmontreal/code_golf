import numpy as np

def flip_h(g): return [r[::-1] for r in g]
def flip_v(g): return g[::-1]

def rotate90(g):
    a=np.array(g);return a.T[:,::-1].tolist()
def rotate180(g):
    return [r[::-1] for r in g[::-1]]
def rotate270(g):
    a=np.array(g);return a[::-1].T.tolist()

def flip_diag(g):
    a=np.array(g);return a.T.tolist()
def flip_antidiag(g):
    a=np.array(g);return np.fliplr(np.flipud(a)).T.tolist()

def shift(g,dx=0,dy=0,fill=0):
    a=np.array(g);h,w=a.shape;res=np.full_like(a,fill)
    xs,ys=max(0,dx),max(0,dy);xe,ye=min(w,w+dx),min(h,h+dy)
    res[ys:ye, xs:xe]=a[ys-dy:ye-dy, xs-dx:xe-dx]
    return res.tolist()

def roll(g,dx=0,dy=0):
    a=np.array(g);return np.roll(np.roll(a,dy,0),dx,1).tolist()

def pad(g,p=1,val=0):
    a=np.array(g);return np.pad(a,p,constant_values=val).tolist()

def recolor(g,s,d):
    a=np.array(g);a[a==s]=d;return a.tolist()

PRIMITIVES=[flip_h,flip_v,rotate90,rotate180,rotate270,flip_diag,flip_antidiag]
