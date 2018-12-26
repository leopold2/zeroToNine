from tkinter import *
import random

root=Tk() #Initiating the frame
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))
col=153 #you know what this is
row=60
num=[random.randint(0,9) for i in range(col*row)] #Creating the first set of numbers to be displayed
st=""
chTime=[100*random.randint(1,10) for i in range(col*row)] #Creating the changing time of each number(i.e. chTime[0]==200 would imply that num[0] would update every 0.2 seconds)
counter=0
fore=["red", "blue", "green", "cyan", "yellow", "white", "purple", "orange", "magenta", "indigo", "midnight blue", "navy", "maroon", "navajo white", "azure", "lawn green", "medium violet red",
        "steel blue", "lime green", "coral", "dark orange", "spring green", "dark orchid"]
fcolor=random.choice(fore)

for k in range(0,col*row,col): #Putting all the numbers in a string so that they can be put into a label
	st=st + ('  '.join(str(e) for e in num[k:k+col])) + '\n'

theLabel= Label(root,text=st,bg="black",fg=fcolor) #Creating the label
theLabel.pack() #Displaying it

def ch(): #Function to change the numbers in num[]
	st1=""
	global counter
	counter+=100 #Counting how much time has passed (in milliseconds)
	for j in range(row*col):
		if counter%chTime[j]==0: #If it is a multiple of the chosen number's changing time
			num[j]=(num[j]+1)%9 #Increments that number in mod(9) since the numbers should stay in (0,9)
	for g in range(0,col*row,col):
		st1=st1 + ('  '.join(str(e) for e in num[g:g+col])) + '\n'
	fcolor=random.choice(fore)
	theLabel.config(text=st1,fg=fcolor)
	theLabel.pack()
	root.after(100,ch) #Using recursion so that the code goes on non-stop

root.after(100,ch)
root.mainloop()
