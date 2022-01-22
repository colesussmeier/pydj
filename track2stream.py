#! python3
from pydub import AudioSegment
from pydub.playback import play
import pydj
import pickle
import pandas as pd

infile = open('soundFiles', 'rb')
files = pickle.load(infile)
infile.close()

infileQ = open('Q', 'rb')
Q = pickle.load(infileQ)
infileQ.close()

infileNum = open('num', 'rb')
num = pickle.load(infileNum)
infileNum.close()

df = pd.read_csv('Setlist.csv')
df = df.set_index('ID')

ID = Q[num]
song = df.iloc[ID]
nextSong = df.iloc[Q[num+1]]
start = song['Start'] * 1000
end = song['End'] * 1000
fade = nextSong['Fade_in'] * 1000
songFile = files[ID][start:end]

play(songFile.fade_in(fade).fade_out(fade))

quit()