from tkinter import *

root = Tk()

root.geometry("600x600")
root.minsize(400, 400) # Defines minimum size of window
root.maxsize(900, 900) # Defines maximum size of window
root.title("My GUI")

lb = Label(
    text=" Debjit Pramanick",
    bg="grey",
    fg="white",
    padx=10,
    pady=10,
    font=("arial",16,"italic"),
    borderwidth=3,
    relief=SUNKEN,
)
lb.pack(anchor="s", side="bottom",padx="20", pady="20", fill=X)

root.mainloop() # It creates basic window