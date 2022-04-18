from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Test Image Viewer")
# TODO: Fix this iconbitmap line
# root.iconbitmap("/home/ricky/Documents/code/tkgui/world.ico")

my_img1 = Image.open("/home/ricky/Documents/code/tkgui/images/taffy1.jpg")
resized_1 = my_img1.resize((800, 600), Image.ANTIALIAS)
my_img_1 = ImageTk.PhotoImage(resized_1)

my_img2 = Image.open("/home/ricky/Documents/code/tkgui/images/taffy2.JPG")
resized_2 = my_img2.resize((800, 600), Image.ANTIALIAS)
my_img_2 = ImageTk.PhotoImage(resized_2)

my_img3 = Image.open("/home/ricky/Documents/code/tkgui/images/taffy3.JPG")
resized_3 = my_img3.resize((800, 600), Image.ANTIALIAS)
my_img_3 = ImageTk.PhotoImage(resized_3)

my_img4 = Image.open("/home/ricky/Documents/code/tkgui/images/taffy4.JPG")
resized_4 = my_img4.resize((800, 600), Image.ANTIALIAS)
my_img_4 = ImageTk.PhotoImage(resized_4)

my_img5 = Image.open("/home/ricky/Documents/code/tkgui/images/taffy5.jpg")
resized_5 = my_img5.resize((800, 600), Image.ANTIALIAS)
my_img_5 = ImageTk.PhotoImage(resized_5)

image_list = [my_img_1, my_img_2, my_img_3, my_img_4, my_img_5]

my_label = Label(image=image_list[0])
my_label.grid(row=0, column=0, columnspan=3)


def back(image_number: int) -> None:
    """
    Define what happens when the back button is clicked.
    - if there are more previous images, back button will cycle to the previous image
    - if there are no more previous images, back button will be disabled

    parameters: image_number as int

    return: None
    """

    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


def forward(image_number: int) -> None:
    """
    Define what happens when the forward button is clicked.
    - if there are more images, forward button will cycle to the next image
    - if there are no more images, forward button is disabled

    parameters: image_number as int

    return: None
    """

    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 5:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


button_back = Button(root, text="<<", state=DISABLED)
button_forward = Button(root, text=">>", command=lambda: forward(2))
button_quit = Button(root, text="Exit Program", command=root.quit)

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)


root.mainloop()
