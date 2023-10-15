from peakpicking import peakpickingVOP

import numpy as np

def VOP_exi(d,y1,y2,y3,y4,y5,y6,TH,flag):

    n31=1*y1+1*y2+y3+y5+(0.4*y6)
    y=n31/max(np.abs(n31))
    vlrop,pp3=peakpickingVOP(y,TH)
    total=len(vlrop)
    return y,vlrop,total,pp3