import numpy as np
from scipy.signal import convolve

def helpres(he1,fs,Gd,speech_rate=1):

    framesize1 = int(5*fs/(1000*speech_rate))
    exccont_he = np.zeros(len(he1))

    for i in range(0,len(he1)-framesize1-1):

        mxvalue1 = max(he1[i: i+framesize1])
        exccont_he[i]=mxvalue1

    exccont_he1 = exccont_he/max(np.abs(exccont_he))
    n1 = convolve(exccont_he1, Gd,mode='full')
    #exccont_he11 = exccont_he1(ceil(401/Speech_Rate): length(n1)-ceil(400/Speech_Rate))
    # print(len(n1))
    n11 = n1[400-1:  len(n1)-400]
    n12 = n11/max(np.abs(n11))
    y1 = n12

    zeros_to_append = np.zeros(len(he1)-len(y1))
    y1 = np.append(y1, zeros_to_append)
    return y1
