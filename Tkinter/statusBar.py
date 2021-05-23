from tkinter import *


def upload():
    statusVar.set("Busy")
    sbar.update()
    import time
    time.sleep(2)
    statusVar.set("Ready")


root = Tk()

root.geometry("600x600")
root.title("My GUI")

statusVar = StringVar()
statusVar.set("Ready")
sbar = Label(root, textvariable=statusVar, relief="sunken")
sbar.pack(side="bottom", fill="x")

Button(root, text="Change Status", command=upload).pack()

root.mainloop() # It creates basic window