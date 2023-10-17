import numpy as np
from scipy.signal import convolve
from svlzfsig2 import zfsig2

def zerofrequency(out1,winsize,fs,Gd,Speech_Rate):

    zffo,gclocssp1,epssp1,f0sp1=zfsig2(out1,fs,winsize)
    zffo=zffo/max(np.abs(zffo))
    Firstdiffzffo=np.diff(zffo)   
    #To calculate the strength
    Seconddiffzffo=np.diff(Firstdiffzffo)

    Seconddiffzffo=Seconddiffzffo/max(np.abs(Seconddiffzffo))
    excfeat_2d1=np.abs(Seconddiffzffo)
    excfeat_2d=excfeat_2d1/max(np.abs(excfeat_2d1))
    exccont_2d=np.zeros(len(zffo))
    framesize2=int(np.ceil(5*fs/(1000*Speech_Rate)))

    for i in range(len(excfeat_2d)-20*framesize2 - 1):
    
        mxvalue2=max(excfeat_2d[i:i+framesize2])
        
        exccont_2d[i]=mxvalue2
    
    exccont_2d1=exccont_2d/max(np.abs(exccont_2d))

    n2=convolve(exccont_2d1, Gd)
    #exccont_2d11=exccont_2d1(ceil(401/Speech_Rate):length(n2)-ceil(400/Speech_Rate));
    n21=n2[400:len(n2)-400-1]

    y2=n21/max(np.abs(n21))

    return y2,zffo, gclocssp1,exccont_2d1