from tkinter import *

root = Tk()


def my_click():
    my_label = Label(root, text="I clicked a button")
    my_label.pack()


my_button = Button(root, text="Click Me", command=my_click, fg="blue", bg="Yellow")
my_button.pack()

root.mainloop()