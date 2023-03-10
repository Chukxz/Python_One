from tkinter import *

root = Tk()
root.title("Learn Coding")
root.iconbitmap("C:/Users/USER/Downloads/mytkico.ico")

frame = LabelFrame(root,padx=50,pady=50)
frame.pack(padx=20,pady=20)

b1 = Button(frame,text="Don't Click Here!")
b1.grid(row=0,column=0)
b2 = Button(frame,text="Or Here!")
b2.grid(row=1,column=1)

root.mainloop()