from tkinter import *
root = Tk()


def hellloworld():
    print("Hello World")

root.geometry("600x600")
root.minsize(400, 400) # Defines minimum size of window
root.maxsize(900, 900) # Defines maximum size of window
root.title("My GUI")

f1 = Frame(root, bg="grey", borderwidth=4, relief="solid")
f1.pack( side=LEFT ,fill=Y)

f2 = Frame(root, bg="grey", borderwidth=4, relief="solid")
f2.pack( side=TOP ,fill=X)

l1 = Label(f1, text="Project Tkinter")
l1.pack(pady=4, padx=4)

l2 = Label(f2, text="Welcome TO Tkinter", pady=20)
l2.pack()

b1 = Button(f1, bg="orange", text="Click Me", padx=10, pady=10, command=hellloworld)
b1.pack(fill=X,pady=4, padx=4)

root.mainloop() # It creates basic window