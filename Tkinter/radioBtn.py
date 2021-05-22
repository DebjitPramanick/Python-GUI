from tkinter import *

root = Tk()

root.geometry("600x600")
root.title("My GUI")

var = IntVar()

radio = Radiobutton(root, text="Dosa", padx=14, variable= var, value=1).pack()

root.mainloop() # It creates basic window