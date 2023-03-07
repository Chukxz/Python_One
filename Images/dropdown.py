from tkinter import *

root = Tk()
root.iconbitmap("./Images/mytkico.ico")
root.geometry("500x500")

#Dropdown menu

def show():
    myLabel = Label(text=clicked.get()).pack()

options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
]

clicked = StringVar()
clicked.set(options[0])

drop1 = OptionMenu(root,clicked,*options)
drop1.pack()

myBtn = Button(root,text="Show selection",command=show).pack()

root.mainloop()