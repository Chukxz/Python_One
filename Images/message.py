from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Learn Coding")
root.iconbitmap("C:/Users/USER/Downloads/mytkico.ico")

#showinfo, showwarning, showerror, askquestion, askokcancel, askyesno, askretrycancel

def popup():
    # rep = messagebox.showinfo("Popup","Hello World!")#has notifiying sound
    # Label(root,text=rep).pack()
    # rep = messagebox.showerror("Popup","Hello World!")#has warning sound
    # Label(root,text=rep).pack()
    # rep = messagebox.showwarning("Popup","Hello World!")#has notifiying sound
    # Label(root,text=rep).pack()
    # rep = messagebox.askquestion("Popup","Hello World!")#has no sound
    # Label(root,text=rep).pack()
    # rep = messagebox.askokcancel("Popup","Hello World!")#has no sound
    # Label(root,text=rep).pack()
    # rep = messagebox.askyesno("Popup","Hello World!")#has no sound
    # Label(root,text=rep).pack()
    # rep = messagebox.askretrycancel("Popup","Hello World!")#has warning sound
    # Label(root,text=rep).pack()
    # rep = messagebox.askyesnocancel("Popup","Hello World!")#has no sound
    # Label(root,text=rep).pack()

    rep = messagebox.askyesnocancel("Popup","Choose")
    if(rep==1):# or if(rep==True)
        Label(root,text="You clicked yes.").pack()
    elif(rep==0):# or if(rep==False)
        Label(root,text="You clicked no.").pack()
    elif(rep==None):
        Label(root,text="You clicked cancel").pack()


    

Button(root,text="Popup",command=popup).pack()

root.mainloop()