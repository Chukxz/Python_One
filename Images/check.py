from tkinter import *

root = Tk()
root.iconbitmap("./Images/mytkico.ico")
root.geometry("500x500")


def show():
    global myLabel
    myLabel = Label(text=var.get()).pack()


var = StringVar()

c = Checkbutton(root,text="Check It!",onvalue="on",offvalue="off",variable=var)
c.select()
c.pack()

myLabel = Label(text=var.get()).pack()

myBtn = Button(root,text="Show Check Value",command=show).pack()

root.mainloop()