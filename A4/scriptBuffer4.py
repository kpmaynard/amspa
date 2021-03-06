import numpy as np
from scipy.signal import get_window
from scipy.fftpack import fft
import math
import matplotlib.pyplot as plt
eps = np.finfo(float).eps
## only works for scipy >.11 
from scipy.signal import argrelextrema

def gensineN(A, phi, f, N, fs):
    f = A * np.cos(2*np.pi*f*np.arange(N)/fs)
    return f

def createFFTBuffer( anArr ):
    sz=np.size(anArr)
    hM1 = int(math.floor((sz+1)/2))
    hM2 = int(math.floor(sz/2))
    fftBuffer=np.zeros(sz)
    fftBuffer[:hM1]=anArr[hM1:]
    fftBuffer[hM2:] = anArr[:hM2]
    return fftBuffer

def createZeropadFFTBuffer( anArr,  width):
    sz=np.size(anArr)
    hM1 = int(math.floor((sz+1)/2))
    hM2 = int(math.floor(sz/2))
    fftBuffer=np.zeros(width)
    fftBuffer[:hM1]=anArr[hM2:]
    fftBuffer[width-hM2:] = anArr[:hM2]
    return fftBuffer



## x
##def test():

x=get_window('blackmanharris', 100)

y= createZeropadFFTBuffer(x, 8*np.size(x))
X=fft(y)

mX=abs(X)

idx=np.where(mX==np.max(mX))

#x = np.random.random(12)

## for scipy >.11
# for local maxima
max_mX=argrelextrema(mX, np.greater)

# for local minima
min_mX=argrelextrema(mX, np.less)


