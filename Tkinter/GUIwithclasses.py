from tkinter import *


class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x600")

    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.sbar = Label(self, textvariable=self.var, relief="sunken")
        self.sbar.pack(side="bottom", fill="x")
    
    def click(self):
        print("Clicked")

    def createBtn(self):
        Button(self, text="Change Status", command=self.click).pack()

if __name__ == '__main__':
    window = GUI()
    window.status()
    window.createBtn()
    window.mainloop()