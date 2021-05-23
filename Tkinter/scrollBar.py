from tkinter import *

root = Tk()

root.geometry("600x600")
root.title("My GUI")

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)

lbx = Listbox(root, yscrollcommand=scrollbar.set)
for i in range(344):
    lbx.insert(END, f"Item{i}")

lbx.pack(fill=BOTH, padx=4, pady=4)
scrollbar.config(command=lbx.yview)

root.mainloop() # It creates basic window