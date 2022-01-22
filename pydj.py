from sys import executable
from subprocess import Popen
from threading import Timer
import pandas as pd
import pickle
import random
import subprocess


def playTrack1():
	global num

	infileQ = open('Q', 'rb')
	Q = pickle.load(infileQ)
	infileQ.close()

	Popen([executable, 'track1stream.py'])
	duration = setlist.iloc[Q[num+1]]['End'] - setlist.iloc[Q[num+1]]['Start'] - setlist.iloc[Q[num+1]]['Fade_in']
	print('\n\nduration of current song: ', duration, 'seconds\n')

	t1 = Timer(interval=duration, function=playTrack2)
	t1.start()

	
	num = num + 1

	out1 = open('num', 'wb')
	pickle.dump(num, out1)
	out1.close()


def playTrack2():
	global num

	infileQ = open('Q', 'rb')
	Q = pickle.load(infileQ)
	infileQ.close()

	Popen([executable, 'track2stream.py'])
	duration = setlist.iloc[Q[num+1]]['End'] - setlist.iloc[Q[num+1]]['Start'] - setlist.iloc[Q[num+1]]['Fade_in']
	print('\n\nduration of current song: ', duration, 'seconds\n')

	t2 = Timer(interval=duration, function=playTrack1)
	t2.start()

	num = num + 1

	out1 = open('num', 'wb')
	pickle.dump(num, out1)
	out1.close() 


if __name__ == "__main__":
	files = []
	setlist = pd.read_csv("Setlist.csv")

	Q = setlist['ID'].values
	random.shuffle(Q)

	out = open('Q', 'wb')
	pickle.dump(Q, out)
	out.close()

	infile = open('soundFiles', 'rb')
	files = pickle.load(infile)
	infile.close()

	out1 = open('num', 'wb')
	pickle.dump('0', out1)
	out1.close()

	global num
	num = 0

	while True:

		print('Welcome to pydj...')
		print('Enter "i" to import song files listed in setlist.csv, whose mp3 files are located in "Songs/"')
		print('Press s to start music and spawn the queue window')


		fromcmd = input("cmd: ")

		#start music and spawn queue window 
		if (fromcmd == "s"):
			infileQ = open('Q', 'rb')
			Q = pickle.load(infileQ)
			infileQ.close()


			Subprogram = Popen(['gnome-terminal', '-e', 'python ./pydjTerminal.py'], stdout=subprocess.PIPE)
			Popen([executable, 'track1stream.py'])
			duration = setlist.iloc[Q[0]]['End'] - setlist.iloc[Q[0]]['Start'] - setlist.iloc[Q[0]]['Fade_in']
			print('\n\nduration of current song: ', duration, 'seconds\n')
			t = Timer(interval=duration, function=playTrack2)
			t.start()

			fromcmd=''

		#spawn queue window 
		if (fromcmd == "q"):
			Subprogram = Popen(['gnome-terminal', '-e', 'python ./pydjTerminal.py'], stdout=subprocess.PIPE)

			fromcmd=''



		#import songs from setlist and load into pickle file
		if (fromcmd == "i"):
			from pydub import AudioSegment


			print('Importing files...')
			for ID in setlist['ID'].unique():
				print(str(ID), '/', str(len(setlist['ID'].unique())))
				file = str(setlist.loc[setlist['ID']==ID, 'File'].values[0])
				track = AudioSegment.from_file('Songs/'+ file, "mp3")
				files.append(track)
			print('Import complete')
	
			outfile = open('soundFiles', 'wb')
			pickle.dump(files, outfile)
			outfile.close()

			print('file dump complete')

			fromcmd=''

		if (fromcmd == "close"):
			quit()
