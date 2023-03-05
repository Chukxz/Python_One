#Intro to Tkinter
from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root,text="Created label on button click!")
    myLabel.pack()

myButton = Button(root, text="Click Me!",command=myClick)
myButton.pack()


root.mainloop()