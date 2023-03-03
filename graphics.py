import tkinter as tk
import pyautogui as pag
import time

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def hello ():  
    label1 = tk.Label(root, text= 'Hello World!', fg='blue', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150,100, window=label1)

    
button1 = tk.Button(text='Click Me', command=hello, bg='brown',fg='white')
canvas1.create_window(150, 200, window=button1)

root.mainloop()



# def move():
#     while True:
#         curorigx, curorigy = pag.position()
#         print(curorigx,curorigy)
#         time.sleep(0.5)

# move()

"""398 116 -- Hello World!"""
"""424 147 -- Vs code minimized successfully"""
""" 305 37 -- Vs code closed successfully"""