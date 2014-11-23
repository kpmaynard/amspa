"""
	Input: 
		InputFile: the path to the wav file
	Output:
		The function should return a numpy array that
		contains 10 samples of the audio.
"""

import numpy

from scipy.io.wavfile import read

import sys


def readAudio(inputFile='../../sounds/piano.wav'):

	sys.path.append('/home/vagrant/sms-tools/software/models')
	import utilFunctions as UF

	print("Input File: ", inputFile)
	(fs, x) = UF.wavread(inputFile)	
	y = x[50000:50010]
        return y

if __name__ == "__main__":
	main()
