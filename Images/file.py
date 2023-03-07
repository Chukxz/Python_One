from tkinter import *
from PIL import ImageTk,Image
root = Tk()
from tkinter import filedialog


root.title("Learn Coding")
root.iconbitmap("./Images/mytkico.ico")


def open():
    global my_btn
    global my_image, my_label, my_image_label
    root.filename = filedialog.askopenfilename(initialdir="/Images",title="Select A File",filetypes=(("png files","*.png"),("all files" ,"*.*"),))
    my_label = Label(root,text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()

    
my_btn = Button(root,text="Open File",command=open).pack()

root.mainloop()

