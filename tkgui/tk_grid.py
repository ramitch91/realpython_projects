from tkinter import *

root = Tk()

my_label1 = Label(root, text="Hello World")
my_label2 = Label(root, text="This is a grid test")
my_label3 = Label(root, text="My name is Ricky")

my_label1.grid(row=0, column=0)
my_label2.grid(row=1, column=1)
my_label3.grid(row=2, column=2)

root.mainloop()
