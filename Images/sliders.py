from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.iconbitmap("C:/Users/USER/Downloads/mytkico.ico")
root.geometry("400x400")

def update():
    my_label_v = Label(root,text=horizontal.get()).pack()
    my_label_h = Label(root,text=vertical.get()).pack()
    root.geometry(str(horizontal.get())+"x"+str(vertical.get()))

vertical = Scale(root,from_=100, to=500)
vertical.pack()

horizontal = Scale(root,from_=100, to=500, orient=HORIZONTAL)
horizontal.pack()

my_label_v = Label(root,text=horizontal.get()).pack()
my_label_h = Label(root,text=vertical.get()).pack()


my_btn = Button(root,text="Update",command=update).pack()

  


root.mainloop()