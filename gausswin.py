import numpy as np
import scipy.stats

def gaussian(L,sigma):
    if L%2==0:
        L=L-1
    
    G=[]

    for i in range(-L//2,L//2):
        G.append(scipy.stats.norm.pdf(i, loc=0, scale=sigma))
    
    Gd=np.diff(G)
    return G,Gd
