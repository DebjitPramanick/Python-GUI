from tkinter import *

def add():
    global i
    i += 1
    lbx.insert(END, f"Item{i}")
    

i = 1

root = Tk()

root.geometry("600x600")
root.title("My GUI")

lbx = Listbox(root)
lbx.pack()

lbx.insert(END, "Item 1")
Button(root,text="Add Item", command=add).pack()

root.mainloop() # It creates basic window