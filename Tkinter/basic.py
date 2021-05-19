from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.geometry("600x600")
root.minsize(400, 400) # Defines minimum size of window
root.maxsize(900, 900) # Defines maximum size of window
root.title("My GUI")

image = Image.open("sample.png")
photo = ImageTk.PhotoImage(image)
lb = Label(image=photo)
lb.pack()

root.mainloop() # It creates basic window
