from tkinter import *
from random import *

root=Tk()
col=133
row=55
num=[randint(0,9) for i in range(col*row)]
st=""
chTime=[100*randint(1,10) for i in range (col*row)]
counter=0

for k in range(0,col*row,col):
	st=st + ('  '.join(str(e) for e in num[k:k+col])) + '\n'

theLabel= Label(root,text=st)
theLabel.pack()

def ch():
	st1=""
	global counter
	counter+=1000
	for j in range(row*col):
		if counter%chTime[j]==0:
			num[j]=(num[j]+1)%9
	for g in range(0,col*row,col):
		st1=st1 + ('  '.join(str(e) for e in num[g:g+col])) + '\n'
	theLabel.config(text=st1)
	theLabel.pack()
	root.after(1000,ch)

root.after(1000,ch)
root.mainloop()