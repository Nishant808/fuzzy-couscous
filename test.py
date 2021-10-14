import tkinter 
import random
from tkinter import *
    #main program
s = "qwertyuiopasdfghjklzxcvbnm,./;'[]\=-1234567890_+{}|:?><"

win = Tk()
win.geometry("400x250")
passlen = Label(win,text ="Input:" ).place(x = 30,y = 50)
entry_1 = Entry(win).place(x =80, y = 50)
entry_1 = int()
p = "".join(random.sample(s,entry_1))
def click():
    win = Tk()
    win.geometry("400x250")
    w = Label(win, text ='Password', font = "90",fg="Navyblue") 
    w.pack() 
    x = print(p)
    msg = Message(win, command = print(x)) 
	
    msg.pack() 
    
processbtn = Button(win, text = "process",command = click).place(x = 30, y = 200)
 
