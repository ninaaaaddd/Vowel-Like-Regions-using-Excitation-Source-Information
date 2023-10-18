import numpy as np
from scipy.signal import convolve

def remTrend(sig,winsize):
    window=np.ones(winsize)
    rm=convolve(sig,window,mode='full')
    rm=rm[int((winsize/2) - 1) : int(len(rm) - (winsize/2))]

    norm = convolve(np.ones(len(sig)),window,mode='full')
    norm = norm[int((winsize/2) - 1): int(len(norm) - (winsize/2))]

    rm=rm/norm
    # rm=np.append(rm,0)
    # print(rm)
    out=sig-rm
    return out


def zeroFreqFilter(wav, fs, winlength):

    dwav = np.diff(wav)
    dwav = np.append(dwav,dwav[-1])
    dwav = dwav/max(np.abs(dwav))
    N = len(dwav)

	# zfSig = filter(1, [1 - 4 6 - 4 1], dwav);
    zfSig = np.cumsum(np.cumsum(np.cumsum(np.cumsum(dwav))))

    winLength = round(winlength*fs/1000)
    zfSig = np.array(remTrend(zfSig, winlength))
    zfSig = np.array(remTrend(zfSig, winlength))
    zfSig = np.array(remTrend(zfSig, winlength))


    # zfSig = remTrend(zfSig, winLength);
    zfSig[N-1-winLength*2: N] = 0
    zfSig[0:winLength*2]=0

    return zfSig


def zfsig2(wav,fs,winlength):
    
    zf = np.array(zeroFreqFilter(wav, fs, winlength))
    gci = np.where(np.diff(zf>0)==1)[0]
    #  +ve zero crossings
    # gci=gci[gci not in [0,len(zf)-1]]
    es=abs(zf[gci+1]-zf[gci-1])
    T0=np.diff(gci)
    T0=T0/fs
    f0=1/T0
    f0=np.append(f0,f0[-1])

    return zf,gci,es,f0

