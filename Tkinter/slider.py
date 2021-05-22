from tkinter import *

root = Tk()

root.geometry("600x600")
root.title("My GUI")

slider = Scale(root, from_ = 0, to = 100)
slider.pack()

slider2 = Scale(root, from_ = 0, to = 100, orient = HORIZONTAL, tickinterval=50)
slider2.pack()


slider2.set(50)

root.mainloop() # It creates basic window