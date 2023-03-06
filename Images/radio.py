from tkinter import *

root = Tk()
root.title("Learn Coding")
root.iconbitmap("../Images/mytkico.ico")

r=IntVar()
r.set(2)

def clicked(value):
    global myLabel
    myLabel.forget()
    myLabel=Label(root,text=value)
    myLabel.pack()

Radiobutton(root,text="Option 1",variable=r,value=1,command=lambda:clicked(r.get())).pack()
Radiobutton(root,text="Option 2",variable=r,value=2,command=lambda:clicked(r.get())).pack()
myLabel=Label(root,text=r.get())
myLabel.pack()


root.mainloop()