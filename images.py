from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn Coding")
root.iconbitmap("C:/Users/USER/Downloads/mytkico.ico")

my_img = ImageTk.PhotoImage(Image.open("C:/Users/USER/Documents/My Homepage files/Quantum_gravity.png"))
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()


root.mainloop()