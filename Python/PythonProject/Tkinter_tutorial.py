"""Tkinter,wxPython and PyQy  are GUI interface,"""
from cProfile import label
from cgitb import text
from struct import pack
from tkinter import *
# import tkinter as tk


#start make window
# root, master,win
root=Tk() #tk is toolkit
# root=tk.Tk()  #second way if we import Tkinter as tk

# make Title
root.title("Tkinter Tutorial")

#Size of window
root.geometry("500x500+0+0")

#change icon
root.wm_iconbitmap("document\\instagram.ico")

#Resizeable
root.resizable(False,False)

#pack(),grid() and place()

# l1=Label(root,text="List of Fruits",font=("times new roman",30,'bold'))
# l1.pack(side=TOP)
 #side=TOP,LEFT,RIGHT,BOTTOM


# l1=Label(root,text="List of Fruits",font=("times new roman",30,'bold'))
# l1.grid(row=0,column=0)
# l1=Label(root,text="List of Fruits",font=("times new roman",30,'bold'))
# l1.grid(row=1,column=0)

def click():
    l1=Label(root,text="List of Fruits",font=("times new roman",30,'bold'))
    l1.pack(side=TOP)

b1=Button(root,text='click me',font=("times new roman",20),fg='black',bg='gold',command=click)
b1.pack(padx=50,pady=50)

l1=Label(root,text="List of Fruits",font=("times new roman",30,'bold'))
l1.place(x=100,y=200)
#end make window
root.mainloop()