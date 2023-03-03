import pyautogui as pag
import tkinter as tk


def Tkint(msg):
    root= tk.Tk()

    canvas1 = tk.Canvas(root, width = 300, height = 200)
    canvas1.pack()

    def hello (msg):  
        label1 = tk.Label(root, text=msg, fg='blue', font=('helvetica', 12, 'bold'))
        canvas1.create_window(150,100, window=label1)
    hello(msg)

    
    button1 = tk.Button(text='     Ok     ', command=root.destroy, bg='white',fg='black',justify='center')
    canvas1.create_window(150, 150, window=button1)

    root.mainloop()

def Cond1():
    pag.click(1251,10,button="PRIMARY",duration=0.5)
    pag.sleep(1)
    msg = "VS Code minimized"
    Tkint(msg)
    pag.sleep(1)
    pag.moveTo(88,750)
    pag.sleep(1)
    pag.click(88,750,button='PRIMARY',duration=0.5)
    pag.keyDown("c");pag.sleep(0.2);pag.keyDown("m");pag.sleep(0.2);pag.keyDown("d");pag.sleep(0.2);pag.keyDown("enter");pag.keyUp("enter")
    pag.sleep(1)
    pag.moveTo(690,370,duration=0.5)


def Cond2():
    pag.click(656,744)
    pag.sleep(2)
    pag.click(1251,10,button="PRIMARY",duration=0.5)
    pag.sleep(1)
    msg = "VS Code minimized"
    Tkint(msg)
    pag.sleep(1)
    pag.moveTo(88,750)
    pag.sleep(1)
    pag.click(88,750,button='PRIMARY',duration=0.5)
    pag.keyDown("c");pag.sleep(0.2);pag.keyDown("m");pag.sleep(0.2);pag.keyDown("d");pag.sleep(0.2);pag.keyDown("enter");pag.keyUp("enter")
    pag.sleep(1)
    pag.moveTo(690,370,duration=0.5)


def Cond3():
    pag.click(1251,10,button="PRIMARY",duration=0.5)
    pag.sleep(1)
    msg = "VS Code minimized"
    Tkint(msg)
    pag.sleep(1)
    pag.moveTo(690,370,duration=0.5)

def Cond4():
    pag.click(656,744)
    pag.sleep(2)
    pag.click(1251,10,button="PRIMARY",duration=0.5)
    pag.sleep(1)
    msg = "VS Code minimized"
    Tkint(msg)
    pag.sleep(1)
    pag.moveTo(690,370,duration=0.5)

def Cond5():
    pag.click(1342,10,button="PRIMARY",duration=0.5)
    pag.sleep(5)
    msg = "VS Code exited"
    Tkint(msg)
    pag.sleep()
    pag.moveTo(88,750)
    pag.sleep(1)
    pag.click(88,750,button='PRIMARY',duration=0.5)
    pag.keyDown("c");pag.sleep(0.2);pag.keyDown("m");pag.sleep(0.2);pag.keyDown("d");pag.sleep(0.2);pag.keyDown("enter");pag.keyUp("enter")
    pag.sleep(1)
    pag.moveTo(690,370,duration=0.5)

def Cond6():
    pag.click(656,744)
    pag.sleep(2)
    pag.click(1342,10,button="PRIMARY",duration=0.5)
    pag.sleep(5)
    msg = "VS Code exited"
    Tkint(msg)
    pag.sleep(1)
    pag.moveTo(88,750)
    pag.sleep(1)
    pag.click(88,750,button='PRIMARY',duration=0.5)
    pag.keyDown("c");pag.sleep(0.2);pag.keyDown("m");pag.sleep(0.2);pag.keyDown("d");pag.sleep(0.2);pag.keyDown("enter");pag.keyUp("enter")
    pag.sleep(1)
    pag.moveTo(690,370,duration=0.5)

def Cond7():
    pag.click(1342,10,button="PRIMARY",duration=0.5)
    pag.sleep(5)
    msg = "VS Code exited"
    Tkint(msg)
    pag.sleep(1)
    pag.moveTo(690,370,duration=0.5)

def Cond8():
    pag.click(656,744)
    pag.sleep(2)
    pag.click(1342,10,button="PRIMARY",duration=0.5)
    pag.sleep(5)
    msg = "VS Code exited"
    Tkint(msg)
    pag.sleep(1)
    pag.moveTo(690,370,duration=0.5)


def wow():
    val = str(input("Value: "))
    if(val!="-h" and val !="--help" and val!="--h" and val!="h" and val!="help" and val!="-help"):
        state = str(input("State: "))
        terminal = str(input("Terminal: "))

    if(val=="h" or val=="--h"):
        print("command not found, did you mean '-h'")
        print("type -h or --help to see guide.")

    if(val=="help" or val=="-help"):
        print("command not found, did you mean '--help'")
        print("type -h or --help to see guide.")

    if(val=="-h"):
        print("Value = ['min -vscode', 'cls -vscode'] , State = ['open', 'closed'] & '--r' , Terminal = ['vsct', 'cmdt']")
        print("type --help for more details.")

    if(val=="--help"):
        print("Value = ['min -vscode', 'cls -vscode'] , State = ['open', 'closed'] & '--r' , Terminal = ['vsct', 'cmdt']")
        print("min -vscode: Minimize Visual Studio Code Window, (if window is minimized first maximize then minimize).")
        print("exit -vscode: Terminate Visual Studio Code Window, (if window is minimized first maximize then exit).")
        print("--r: [<Val><" ">] & ['--r' | ''] Reinitialize Command Prompt after operation.")
        print("minimized: Indicate if Visual Studio Code Window is minimized in the background.")
        print("maximized: Indicate if Visual Studio Code Window is maximized in the background.")
        print("vsct: Visual Studio Code Terminal")
        print("cmdt: Command Prompt Terminal")

    if(val == "min -vscode --r"):
        if(state == "maximized"):
            if(terminal=="cmdt"):
                pag.sleep(0.5)
                pag.click(1330,50,button="PRIMARY",duration=0.5)
                pag.sleep(0.5)
                Cond1()
            if(terminal=="vsct"):
                pag.sleep(0.5)
                Cond1()

        if(state == "minimized"):
            if(terminal=="cmdt"):
                pag.sleep(0.5)
                pag.click(1330,50,button="PRIMARY",duration=0.5)
                pag.sleep(0.5)
                Cond2()
            if(terminal=="vsct"):
                print("VS Code terminal cannot be used in minimized window.")

        
    if(val == "min -vscode"):
        if(state == "maximized"):
            if(terminal=="cmdt"):
                pag.sleep(0.5)
                pag.click(1330,50,button="PRIMARY",duration=0.5)
                pag.sleep(0.5)
                Cond3()
            if(terminal=="vsct"):
                pag.sleep(0.5)
                Cond3()

        if(state == "minimized"):
            if(terminal=="cmdt"):
                pag.sleep(0.5)
                pag.click(1330,50,button="PRIMARY",duration=0.5)
                pag.sleep(0.5)
                Cond4()
            if(terminal=="vsct"):
                print("VS Code terminal cannot be used in minimized window.")



    if(val == "exit -vscode --r"):
        if(state == "maximized"):
            if(terminal=="cmdt"):
                pag.sleep(0.5)
                pag.click(1330,50,button="PRIMARY",duration=0.5)
                pag.sleep(0.5)
                Cond5()
            if(terminal=="vsct"):
                pag.sleep(0.5)
                Cond5()

        if(state == "minimized"):
            if(terminal=="cmdt"):
                pag.sleep(0.5)
                pag.click(1330,50,button="PRIMARY",duration=0.5)
                pag.sleep(0.5)
                Cond6()
            if(terminal=="vsct"):
                print("Vs Code terminal cannot be used in minimized window.")


    
    if(val == "exit -vscode"):
        if(state == "maximized"):
            if(terminal=="cmdt"):
                pag.sleep(0.5)
                pag.click(1330,50,button="PRIMARY",duration=0.5)
                pag.sleep(0.5)
                Cond7()
            if(terminal=="vsct"):
                pag.sleep(0.5)
                Cond7()

        if(state == "minimized"):
            if(terminal=="cmdt"):
                pag.sleep(0.5)
                pag.click(1330,50,button="PRIMARY",duration=0.5)
                pag.sleep(0.5)
                Cond8()
            if(terminal=="vsct"):
                print("Vs Code terminal cannot be used in minimized window.")

wow()




            

"""
minimize cmd - x:1240, y:52
close cmd -x:1330, y:50
Middle of screen - x:690, y:370
Visual studio code icon - x: 656, y:744
minimize vscode - x:1251, y:10
close vscode -x:1342, y:10
type in search - x:88, y:750
open cmd - x:750, 740

pag.click(x,y,2,0.1,1,0.05)
pag.isShiftCharacter()
pag.isValidKey()
"""






