import numpy as np
from pre_emp import preemphasize
import librosa
from scipy.signal.windows import hann
from scipy.signal import hamming, hilbert


def LPres(speech, fs, framesize, frameshift, lporder, preemp=False):
    if (framesize > 50):
        print("Warning!")
    else:
        Nframesize = round(framesize * fs / 1000)
        Nframeshift = round(frameshift * fs / 1000)
        Nspeech = len(speech)

    speech = speech.reshape(Nspeech, 1)

    if preemp:
        speech = preemphasize(speech)
    res = np.asarray(np.zeros((Nspeech, 1)))[:, 0]

    lporder = int(lporder)
    j = 1

    for i in range(0, Nspeech-Nframesize, Nframeshift):
        SpFrm = speech[i: i+Nframesize]

        winHann = np.asmatrix(hann(Nframesize))
        y_frame = np.asarray(np.multiply(winHann, SpFrm.T))

        lpcoef = librosa.lpc(y=y_frame[0, :], order=lporder)

        if (i <= lporder):
            PrevFrm = np.zeros((1, lporder))
        else:
            PrevFrm = speech[(i-lporder):(i)]
        ResFrm = ResFilter_v2(np.real(PrevFrm), np.real(
            SpFrm), np.real(lpcoef), lporder, Nframesize)

        res[i: i+Nframeshift] = ResFrm[: Nframeshift]
        j = j+1

    res[i+Nframeshift:i+Nframesize] = ResFrm[Nframeshift:Nframesize]

    # PROCESSING LASTFRAME SAMPLES,
    if (i < Nspeech):
        SpFrm = speech[i:Nspeech]
        winHann = np.asmatrix(hamming(len(SpFrm)))
        y_frame = np.asarray(np.multiply(winHann, SpFrm.T))
        lpcoef = librosa.lpc(y=y_frame[0, :], order=lporder)
        PrevFrm = speech[(i-lporder):(i)]
        ResFrm = ResFilter_v2(np.real(PrevFrm), np.real(
            SpFrm), np.real(lpcoef), lporder, Nframesize)
        res[i:i+len(ResFrm)] = ResFrm[:len(ResFrm)]
        j = j+1
    hm = hamming(2*lporder)
    for i in range(1, round(len(hm)/2)):
        res[i] = res[i] * hm[i]  # attenuating first lporder samples
    return res


def ResFilter_v2(PrevSpFrm, SpFrm, FrmLPC, LPorder, FrmSize):

    ResFrm = np.asarray(np.zeros((1, FrmSize)))
    ResFrm = ResFrm[0, :]
    tempfrm = np.zeros((1, FrmSize+LPorder))

    temp_PrevSpFrm = np.asmatrix(PrevSpFrm)
    temp_SpFrm = np.asmatrix(SpFrm[:FrmSize])
    if (np.shape(temp_PrevSpFrm)[0] == 1):
        temp_PrevSpFrm = temp_PrevSpFrm.T
    if (np.shape(temp_SpFrm)[0] == 1):
        temp_SpFrm = temp_SpFrm.T

    tempfrm = np.concatenate((temp_PrevSpFrm, temp_SpFrm))
    tempfrm = np.asarray(tempfrm)[:, 0]

    for i in range(FrmSize):
        t = 0
        for j in range(LPorder):
            t = t+FrmLPC[j+1]*tempfrm[-j+i+LPorder-1]

        ResFrm[i] = SpFrm[i]-(-t)

    return ResFrm


def excitation(sample, fs, preemp=False):
    """For genrating the residual signal

    :param sample: Numpy array of the original audio signal
    :type sample: np.array
    :param fs: Frequency of the signal
    :type fs: int

    :return: residual signal hilbert envenlope, phase
    :rtype: np.array, float, float
    """
    lporder = 10
    residual = LPres(sample, fs, 20, 10, lporder, preemp)
    henv = np.abs(hilbert(residual))
    henv = henv/(max(np.abs(henv)))
    # resPhase = np.divide(residual, henv)
    return residual, henv
