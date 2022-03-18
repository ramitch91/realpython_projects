from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Test Image')
# root.iconbitmap('world.ico')

my_img = ImageTk.PhotoImage(Image, open('/home/ricky/Documents/code/tkgui/taffy5.jpg'))
my_label = Label(root, image=my_img)
my_label.pack()

root.mainloop()
