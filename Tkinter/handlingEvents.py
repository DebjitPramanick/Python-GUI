from tkinter import *

root = Tk()

def debjit(event):
    print(event)

root.geometry("600x600")
root.title("My GUI")

lb = Button(root, text="Click Me")
lb.pack()

lb.bind('<Button-1>', debjit)
lb.bind('<Double-1>', quit)

root.mainloop() # It creates basic window