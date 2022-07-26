from html import entities
import os
from tkinter import *
from tkinter import messagebox

def register():
    username=entry1.get()
    password=entry2.get()


root = Tk()
root.title("Register")
root.geometry("500x300")

global entry1
global entry2


Label(root,text= "Enter your registration info",font=("Calibri",17)).place(x=100,y=20)
Label(root,text= "Username").place(x=20,y=70)
Label(root,text= "Password").place(x=20,y=120)
Label(root,text= "Email").place(x=20,y=170)

entry1 = Entry(root,bd=5)
entry1.place(x=140,y=70)

entry2 = Entry(root,bd=5)
entry2.place(x=140,y=120)

entry3 = Entry(root,bd=5)
entry3.place(x=140,y=170)



Button(root,text="Register",command=register,height=2,width=13,bd=6).place(x=130,y=230)

root.mainloop()