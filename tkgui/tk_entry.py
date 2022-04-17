from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter your name: ")


def my_click() -> None:
    """
    Runs code after button is clicke

    parameters: None

    return: None
    """

    hello = "Hello " + e.get()
    my_label = Label(root, text=hello)
    my_label.pack()


my_button = Button(root, text="Submit", command=my_click)
my_button.pack()

root.mainloop()
