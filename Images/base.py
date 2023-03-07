from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title("Learn Coding")
root.iconbitmap("./Images/mytkico.ico")

def open1():
    global my_img_1
    top = Toplevel()
    top.title("Second Widget")
    top.iconbitmap("./Images/mytkico.ico")
    my_img_1 = ImageTk.PhotoImage(Image.open("./Images/the_green.jpg"))
    my_label_1 = Label(top,image=my_img_1).pack()
    my_btn_1 = Button(top,text="Close Window",command=top.destroy).pack()


my_button_1 = Button(root,text="Open Second Window",command=open1).pack()


def open2():
    global my_img_2
    top = Toplevel()
    top.title("Second Widget")
    top.iconbitmap("./Images/mytkico.ico")
    my_img_2 = ImageTk.PhotoImage(Image.open("./Images/the_green.jpg"))
    my_label_2 = Label(top,image=my_img_2).pack()
    my_btn_2 = Button(top,text="Close Window",command=top.destroy).pack()


my_button_1 = Button(root,text="Open Second Window",command=open2).pack()

root.mainloop()


