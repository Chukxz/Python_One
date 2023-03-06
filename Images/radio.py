from tkinter import *

root = Tk()
root.title("Learn Coding")
root.iconbitmap("./Images/mytkico.ico")

# r=IntVar()
# r.set(2)

#Radiobutton(root,text="Option 1",variable=r,value=1,command=lambda:clicked(r.get())).pack()
#Radiobutton(root,text="Option 2",variable=r,value=2,command=lambda:clicked(r.get())).pack()

myFrame = LabelFrame(root,padx=10,pady=10)
myFrame.pack(pady=20,padx=5)

MODES_TOPPINGS = [
    ("Pepperoni", "Pepperonin"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion")
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES_TOPPINGS:
    Radiobutton(myFrame,text=text,variable=pizza,value=mode).pack(anchor=W)

def clicked(value):
    myLabel = Label(myFrame,text=value)
    myLabel.pack()

myButton = Button(myFrame,text="Click Me!",command=lambda:clicked(pizza.get())).pack(anchor=W)

button_exit = Button(root, text="EXIT PROGRAM",command=root.quit).pack()


root.mainloop()