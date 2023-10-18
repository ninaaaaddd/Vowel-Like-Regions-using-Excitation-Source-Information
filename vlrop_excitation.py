from peakpicking import peakpickingVOP
from scipy.signal import find_peaks

import numpy as np

def VOP_exi(d,y1,y2,y3,y4,y5,y6,TH,flag):

    n31=y1+y2
    y=n31/max(np.abs(n31))
    # vlrop,pp3=peakpickingVOP(y,TH)
    pp3,vlrop=find_peaks(y,height=TH)
    total=len(vlrop)
    return y,vlrop,total,pp3