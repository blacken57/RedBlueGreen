
# Python program to create a simple GUI 
# Simple Quiz using Tkinter 
  
#import everything from tkinter 
from tkinter import *
  
# and import messagebox as mb from tkinter 
from tkinter import messagebox as mb 
  
#import json to use json file for data 
import json
import subprocess


x,y = subprocess.Popen("RedBlueGreen.exe 3 3 3"  , stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True).communicate()
x = x.decode()

x = x.split('\n')
totals = x[0].split(" ")
totals[2] = totals[2][:-1]


gui = Tk() 
  
# set the size of the GUI Window 
gui.geometry("800x450")

gui.title("RedBlueGreen")

class Problem:
    def __init__(self):
        self.pres=0
        self.display_state()
        self.buttons()
    def buttons(self):
        next_button = Button(gui, text="Next",command=self.next_btn, 
        width=10,bg="blue",fg="white",font=("ariel",16,"bold"))
        next_button.place(x=350,y=380)
    def next_btn(self):
        if(self.pres<len(x)):
            self.pres+=1
            self.display_state()
        if(self.pres==len(x)):
            gui.destroy()
    def display_state(self):
        disp = "West bank \t\t East bank\n"
        
        h = x[self.pres].split(" ")
        print(h)
        disp+=h[0]+" \t\t "+str((int(totals[0])-int(h[0])))
        disp+=h[1]+" \t\t "+str((int(totals[1])-int(h[1])))
        disp+=h[2]+" \t\t "+str((int(totals[2])-int(h[2])))
        q_no = Label(gui, text=disp, width=60, 
        font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
        q_no.place(x=70,y=100)
prob = Problem()
gui.mainloop()
            
