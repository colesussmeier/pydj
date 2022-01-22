import pickle
import pandas as pd
import numpy as np

infileQ = open('Q', 'rb')
Q = pickle.load(infileQ)
infileQ.close()

df = pd.read_csv('Setlist.csv')
df = df.set_index('ID')

while True:

	print('\n')
	print('Enter "q" to see the randomized queue')
	print('To change the queue, type "rq [song id] [position of desired position in queue]" example: rq 2 1')

	fromcmd = input("cmd: ")

	if fromcmd == 'q':

		infileNum = open('num', 'rb')
		num = pickle.load(infileNum)
		num = int(num)
		infileNum.close()
		print('\n\n')
		print(df.iloc[Q]['Song'].reset_index().iloc[num:])
		fromcmd = ''

	if fromcmd[0:2] == 'rq':
		rq = fromcmd[2:].split()
		sid = int(rq[0])
		pos = int(rq[1])

		# work with Q array
		Q = np.delete(Q,np.where(Q==sid)[0][0])
		Q = np.insert(Q, pos, sid)

		# update global 
		out = open('Q', 'wb')
		pickle.dump(Q, out)
		out.close() 
		fromcmd= ''