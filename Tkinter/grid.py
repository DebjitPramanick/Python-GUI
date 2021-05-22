from tkinter import *

root = Tk()


def getVals():
    print(userval.get(), passval.get())


root.geometry("600x600")
root.minsize(400, 400) # Defines minimum size of window
root.maxsize(900, 900) # Defines maximum size of window
root.title("My GUI")

user = Label(root, text="Username: ")
password = Label(root, text="Password: ")


user.grid()
password.grid(row=1)

# Variable classes in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar

userval = StringVar()
passval = StringVar()

userentry = Entry(root, textvariable=userval)
passentry = Entry(root, textvariable=passval)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

Button(text="Submit", command=getVals,padx=10, pady=5).grid()

root.mainloop() # It creates basic window