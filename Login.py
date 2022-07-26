from html import entities
import os
from tkinter import *
from tkinter import messagebox

def register():
    root.withdraw()
    os.system("python C:/Programming'/Project/register.py")
    root.deiconify()

def login():
    username=entry1.get()
    password=entry2.get()

    try:
        if(username=="Bhejjaa" and password == "admin"):
            messagebox.showinfo("","Login Successful")
            root.withdraw()
            os.system("python C:/Programming'/Project/game.py")
            root.deiconify()
        else:
            raise ValueError
    except(ValueError):
            messagebox.showerror("warning!!","Donot Leave Empty or Incorrect info")
    


root = Tk()
root.title("Login")
root.geometry("400x300")

global entry1
global entry2

Label(root,text= "Enter your login info",font=("Calibri",17)).place(x=100,y=20)
Label(root,text= "Username").place(x=20,y=70)
Label(root,text= "Password").place(x=20,y=120)
Label(text= "OR",font=("Calibri",20)).place(x=140,y=210)

entry1 = Entry(root,bd=5)
entry1.place(x=140,y=70)

entry2 = Entry(root,bd=5)
entry2.place(x=140,y=120)

Button(root,text="Login",command=login,height=1,width=9,bd=6).place(x=120,y=170)
Button(root,text="Register",command=register,height=1,width=9,bd=6).place(x=120,y=250)

root.mainloop()