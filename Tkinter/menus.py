from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()

def myFunc():
    print("I am Debjit.")

def myFunc2():
    a = tmsg.showinfo("I am Debjit2.")

root.geometry("600x600")
root.title("My GUI")

myMenu = Menu(root)
myMenu.add_command(label="File", command=myFunc)
myMenu.add_command(label="Exit", command=quit)
m1 = Menu(myMenu ,tearoff=0)
m1.add_command(label="File", command=myFunc)
m1.add_command(label="Exit", command=quit)
m1.add_separator()
m1.add_command(label="File2", command=myFunc2)

root.config(menu=myMenu)
myMenu.add_cascade(label="DropDown", menu=m1)

root.mainloop() # It creates basic window