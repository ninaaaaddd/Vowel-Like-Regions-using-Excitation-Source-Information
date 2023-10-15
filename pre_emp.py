import numpy as np

def preemphasize(sig):
  """ Returns preemphasized signal
  
  :param sig: signal
  :type sig: np.array
  :return: preemphasized speech
  :rtype: np.array
  """
  dspeech=np.diff(sig)
  dspeech=dspeech.tolist()
  dspeech.append(dspeech[len(dspeech)-1])
  return np.array(dspeech)
