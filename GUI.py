import tkinter as tk
from tkinter import ttk
from tkinter import *

class Test(tk.Tk):

    def __init__(self):
        super().__init__()

        self.geometry("1600x900")
        self.title("GUI testing")
        label1=Label(self, text=("This is a Test"),background=("gray22"),font=("yu gothic ui", 20))
        label1.config(fg="white")
        label1.pack()
        self.iconbitmap("guitar.ico")
        self["bg"]="gray22"

        button=ttk.Button(self,text="Exit",command=self.quit)
        button.pack(expand=True)
        button.place(x=10,y=10)

        style=ttk.Style(self)
        style.configure("TButton",font=("yu gothic ui",20))
        style.map("TButton",
                foreground=[("pressed","green"),
                            ("active","green")])
        print(style.layout("TButton"))

app=Test()
app.mainloop()