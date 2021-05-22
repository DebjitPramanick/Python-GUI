from tkinter import *

root = Tk()
root.geometry("600x600")

def getVals():
    print(name.get(), age.get())


Label(root, text="User Input", font="arial 26 bold").grid(row=0, column=3)
Label(root, text="Name").grid(row=1,column=0)
Label(root, text="Age").grid(row=2,column=0)

name = StringVar()
age = IntVar()

nameentry = Entry(root, textvariable=name)
ageentry = Entry(root, textvariable=age)

nameentry.grid(row=1, column=1)
ageentry.grid(row=2, column=1)

Button(text="Submit", command=getVals,padx=10, pady=5).grid(row=4, column=3)


root.mainloop()