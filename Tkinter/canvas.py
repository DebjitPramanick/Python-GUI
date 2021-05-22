from tkinter import *

root = Tk()
root.geometry("600x600")


can_widget = Canvas(root, width = 600, height = 600)
can_widget.pack()

can_widget.create_line(0, 0, 600, 100, fill="red")
can_widget.create_rectangle(40, 100, 560, 300, fill="blue") # First two are top left co-ordinates and second two are bottom right co-ordinates
can_widget.create_text(400,400, text="Python")
can_widget.create_oval(60,200,540,400,fill="green")

root.mainloop()