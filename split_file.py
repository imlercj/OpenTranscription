from config import *

from pydub import AudioSegment

t1 = 0 * 1000 #Works in milliseconds
t2 = 300 * 1000
newAudio = AudioSegment.from_wav(WAVE_OUTPUT_FILENAME)
newAudio = newAudio[t1:t2]
newAudio.export('data/frac.wav', format="wav") #Exports to a wav file in the current path.