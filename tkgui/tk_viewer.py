from ast import Lambda
from cProfile import label
from tkinter import *
from PIL import ImageTk, Image
from pyparsing import col

root = Tk()
root.title("Test Image Viewer")
# root.iconbitmap("/home/ricky/Documents/code/tkgui/world.ico")


def button_back():
    """
    
    """
    r
    eturn


def button_forward():
    """
    
    """
    
    return


my_img_1= ImageTk.PhotoImage(Image.open("/home/ricky/Documents/code/tkgui/images/taffy1.jpg"))
my_img_2= ImageTk.PhotoImage(Image.open("/home/ricky/Documents/code/tkgui/images/taffy2.jpg"))
my_img_3= ImageTk.PhotoImage(Image.open("/home/ricky/Documents/code/tkgui/images/taffy3.jpg"))
my_img_4= ImageTk.PhotoImage(Image.open("/home/ricky/Documents/code/tkgui/images/taffy4.jpg"))
my_img_5= ImageTk.PhotoImage(Image.open("/home/ricky/Documents/code/tkgui/images/taffy5.jpg"))

image_list = [my_img_1, my_img_2, my_img_3, my_img_4, my_img_5]

my_label = Label(root, image=my_img)
my_label.grid(row=0, column=0, columnspan=3)

back_button = Button(root, text="<<", command=Lambda: button_back())
forward_button = Button(root, text=">>", command=Lambda: button_forward())
button_quit = Button(root, text="Exit Program", command=root.quit)

back_button.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
forward_button.grid(row=1, column=2)


root.mainloop()
