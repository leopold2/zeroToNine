from tkinter import *
from random import *

root=Tk() #Initiating the frame
col=133
row=55
num=[randint(0,9) for i in range(col*row)] #Creating the first set of numbers to be displayed
st=""
chTime=[100*randint(1,10) for i in range (col*row)] #Creating the changing time of each number(i.e. chTime[0]==200 would imply that num[0] would update every 0.2 seconds)
counter=0

for k in range(0,col*row,col): #Putting all the numbers in a string so that they can be put into a label
	st=st + ('  '.join(str(e) for e in num[k:k+col])) + '\n'

theLabel= Label(root,text=st) #Creating the label
theLabel.pack() #Displaying it

def ch(): #Function to change the numbers in num[]
	st1=""
	global counter
	counter+=1000 #Counting how much time has passed (in milliseconds)
	for j in range(row*col):
		if counter%chTime[j]==0: #If it is a multiple of the chosen number's changing time
			num[j]=(num[j]+1)%9 #Increments that number in mod(9) since the numbers should stay in (0,9)
	for g in range(0,col*row,col):
		st1=st1 + ('  '.join(str(e) for e in num[g:g+col])) + '\n'
	theLabel.config(text=st1)
	theLabel.pack()
	root.after(1000,ch) #Using recursion so that the code goes on non-stop

root.after(1000,ch)
root.mainloop()
