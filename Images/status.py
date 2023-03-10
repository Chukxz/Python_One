from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn Coding")
root.iconbitmap("C:/Users/USER/Downloads/mytkico.ico")

my_img1 = ImageTk.PhotoImage(Image.open("./Images/Quantum_mechanics_logo_1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("./Images/Quantum_mechanics_logo_2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("./Images/myimgs.png"))
my_img4 = ImageTk.PhotoImage(Image.open("./Images/the_green.jpg"))

image_list = [my_img1,my_img2,my_img3,my_img4]
image_list_len = len(image_list)

status = Label(root, text="Image 1 of " + str(image_list_len),bd=1,relief=SUNKEN,anchor=E)

my_label = Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)

def forward(image_number):
    global my_label, button_forward, button_back, image_list_len

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root,text=">>",command=lambda:forward(image_number+1))
    button_back = Button(root,text="<<",command=lambda:back(image_number-1))

    if(image_number == image_list_len):
        button_forward = Button(root,text=">>",state=DISABLED)
    #update status bar
    my_label.grid(row=0,column=0,columnspan=3)
    #update buttons
    button_back.grid(row=1,column=0)
    button_exit.grid(row=1,column=1)
    button_forward.grid(row=1,column=2)
    #Update status bar
    status = Label(root, text="Image " + str(image_number) + " of " + str(image_list_len),bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=E+W)


def back(image_number):
    global my_label, button_forward, button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root,text=">>",command=lambda:forward(image_number+1))
    button_back = Button(root,text="<<",command=lambda:back(image_number-1))

    if(image_number == 1):
        button_back = Button(root, text="<<", state=DISABLED)
    #update image
    my_label.grid(row=0,column=0,columnspan=3)
    #update buttons
    button_back.grid(row=1,column=0)
    button_exit.grid(row=1,column=1)
    button_forward.grid(row=1,column=2)
    #Update status bar
    status = Label(root, text="Image " + str(image_number) + " of " + str(image_list_len),bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=E+W)


button_back = Button(root, text="<<",command = back, state=DISABLED)
button_exit = Button(root, text="EXIT PROGRAM",command=root.quit)
button_forward = Button(root, text=">>",command=lambda:forward(2))

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2,pady=10)

status.grid(row=2,column=0,columnspan=3,sticky=E+W)

root.mainloop()