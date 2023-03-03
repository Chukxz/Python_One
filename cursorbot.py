import pyautogui as pag
import tkinter as tk

def tkint(msg):
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

def cond1():
    pag.click(1251,10,button="PRIMARY",duration=0.5)
    pag.sleep(1)
    msg = "VS Code minimized"
    pag.moveTo(795,745,duration=0.5)
    tkint(msg)
    pag.sleep(1)
    pag.moveTo(88,750,duration=0.5)
    pag.sleep(2)
    pag.click(88,750,button='PRIMARY',duration=0.5)
    pag.keyDown("c");pag.sleep(0.2);pag.keyDown("m");pag.sleep(0.2);pag.keyDown("d");pag.sleep(0.2);pag.keyDown("enter");pag.keyUp("enter")
    pag.sleep(2)
    pag.moveTo(690,370,duration=0.5)

def cond2():
    pag.click(656,745)
    pag.sleep(2)
    pag.click(1251,10,button="PRIMARY",duration=0.5)
    pag.sleep(1)
    msg = "VS Code minimized"
    pag.moveTo(795,745,duration=0.5)
    tkint(msg)
    pag.sleep(1)
    pag.moveTo(88,750,duration=0.5)
    pag.sleep(2)
    pag.click(88,750,button='PRIMARY',duration=0.5)
    pag.keyDown("c");pag.sleep(0.2);pag.keyDown("m");pag.sleep(0.2);pag.keyDown("d");pag.sleep(0.2);pag.keyDown("enter");pag.keyUp("enter")
    pag.sleep(2)
    pag.moveTo(690,370,duration=0.5)

def cond3():
    pag.click(1251,10,button="PRIMARY",duration=0.5)
    pag.sleep(1)
    msg = "VS Code minimized"
    pag.moveTo(795,745,duration=0.5)
    tkint(msg)
    pag.sleep(1)

def cond4():
    pag.click(656,745)
    pag.sleep(2)
    pag.click(1251,10,button="PRIMARY",duration=0.5)
    pag.sleep(1)
    msg = "VS Code minimized"
    pag.moveTo(795,745,duration=0.5)
    tkint(msg)
    pag.sleep(1)
    pag.click(748,745,button="PRIMARY",duration=0.5)
    pag.sleep(1)
    pag.moveTo(690,370,duration=0.5)

def cond5():
    pag.click(1342,10,button="PRIMARY",duration=0.5)
    pag.sleep(5)
    msg = "VS Code exited"
    pag.moveTo(795,745,duration=0.5)
    tkint(msg)
    pag.sleep(1)
    pag.moveTo(88,750,duration=0.5)
    pag.sleep(2)
    pag.click(88,750,button='PRIMARY',duration=0.5)
    pag.keyDown("c");pag.sleep(0.2);pag.keyDown("m");pag.sleep(0.2);pag.keyDown("d");pag.sleep(0.2);pag.keyDown("enter");pag.keyUp("enter")
    pag.sleep(2)
    pag.moveTo(690,370,duration=0.5)

def cond6():
    pag.click(656,745)
    pag.sleep(2)
    pag.click(1342,10,button="PRIMARY",duration=0.5)
    pag.sleep(5)
    msg = "VS Code exited"
    pag.moveTo(795,745,duration=0.5)
    tkint(msg)
    pag.sleep(1)
    pag.moveTo(88,750,duration=0.5)
    pag.sleep(2)
    pag.click(88,750,button='PRIMARY',duration=0.5)
    pag.keyDown("c");pag.sleep(0.2);pag.keyDown("m");pag.sleep(0.2);pag.keyDown("d");pag.sleep(0.2);pag.keyDown("enter");pag.keyUp("enter")
    pag.sleep(2)
    pag.moveTo(690,370,duration=0.5)

def cond7():
    pag.click(1342,10,button="PRIMARY",duration=0.5)
    pag.sleep(5)
    msg = "VS Code exited"
    pag.moveTo(795,745,duration=0.5)
    tkint(msg)
    pag.sleep(1)
    pag.click(748,745,button="PRIMARY",duration=0.5)
    pag.sleep(1)
    pag.moveTo(690,370,duration=0.5)

def cond8():
    pag.click(656,745)
    pag.sleep(2)
    pag.click(1342,10,button="PRIMARY",duration=0.5)
    pag.sleep(5)
    msg = "VS Code exited"
    pag.moveTo(795,745,duration=0.5)
    tkint(msg)
    pag.sleep(1)
    pag.click(748,745,button="PRIMARY",duration=0.5)
    pag.sleep(1)
    pag.moveTo(690,370,duration=0.5)

def construct():
    
    """
        --- Properties ------ Coordintates (x,y) ----\n
        Minimize Cmd - x : 1240, y : 50;\n
        Close Cmd - x : 1330, y : 50;\n
        Middle Of Screen - x : 690, y : 370;\n
        Visual Studio Code Icon - x : 656, y : 745;\n
        Command Prompt Icon - x : 748, y : 745;\n
        Minimize VSCode - x : 1251, y : 10;\n
        Close VSCcode -x : 1342, y : 10;\n
        Type In Windows Search Bar - x : 88, y : 750;\n
        Open Cmd - x : 750, y : 740;\n
        Tkinter Icon - x : 795, y : 740;\n
    """

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
        print("Value = ['min -vscode', 'exit -vscode'] & '--n' | '' , State = ['open', 'closed'] , Terminal = ['vsct', 'cmdt']")
        print("type --help for more details.")

    if(val=="--help"):
        print("Value = ['min -vscode', 'exit -vscode'] & '--n' | '' , State = ['open', 'closed']  , Terminal = ['vsct', 'cmdt']")
        print("min -vscode: Minimize Visual Studio Code Window, (if window is minimized first maximize then minimize).")
        print("exit -vscode: Terminate Visual Studio Code Window, (if window is minimized first maximize then exit).")
        print("--n: [<Val><" ">] & ['--n' | ''] Reinitialize new Command Prompt after operation.")
        print("minimized: Indicate if Visual Studio Code Window is minimized in the background.")
        print("maximized: Indicate if Visual Studio Code Window is maximized in the background.")
        print("vsct: Visual Studio Code Terminal.")
        print("cmdt: Command Prompt Terminal.")

    if(val == "min -vscode --n"):
        if(state == "maximized"):
            if(terminal=="cmdt"):
                pag.sleep(0.5)
                pag.click(1240,50,button="PRIMARY",duration=0.5)
                pag.sleep(0.5)
                cond1()
            if(terminal=="vsct"):
                pag.sleep(0.5)
                cond1()

        if(state == "minimized"):
            if(terminal=="cmdt"):
                pag.sleep(0.5)
                pag.click(1240,50,button="PRIMARY",duration=0.5)
                pag.sleep(0.5)
                cond2()
            if(terminal=="vsct"):
                print("VS Code terminal cannot be used in minimized window.")
        
    if(val == "min -vscode"):
        if(state == "maximized"):
            if(terminal=="cmdt"):
                pag.sleep(0.5)
                pag.click(1240,50,button="PRIMARY",duration=0.5)
                pag.sleep(0.5)
                cond3()
                pag.click(748,745,button="PRIMARY",duration=0.5)
                pag.sleep(1)
                pag.moveTo(690,370,duration=0.5)                
            if(terminal=="vsct"):
                pag.sleep(0.5)
                cond3()
                pag.moveTo(690,370,duration=0.5)                

        if(state == "minimized"):
            if(terminal=="cmdt"):
                pag.sleep(0.5)
                pag.click(1240,50,button="PRIMARY",duration=0.5)
                pag.sleep(0.5)
                cond4()
            if(terminal=="vsct"):
                print("VS Code terminal cannot be used in minimized window.")

    if(val == "exit -vscode --n"):
        if(state == "maximized"):
            if(terminal=="cmdt"):
                pag.sleep(0.5)
                pag.click(1240,50,button="PRIMARY",duration=0.5)
                pag.sleep(0.5)
                cond5()
            if(terminal=="vsct"):
                pag.sleep(0.5)
                pag.moveTo(88,750,duration=0.5)
                pag.sleep(2)
                pag.click(88,750,button='PRIMARY',duration=0.5)
                pag.keyDown("c");pag.sleep(0.2);pag.keyDown("m");pag.sleep(0.2);pag.keyDown("d");pag.sleep(0.2);pag.keyDown("enter");pag.keyUp("enter")
                pag.sleep(2)
                pag.click(656,745,button="PRIMARY",duration=0.5)
                pag.sleep(2)
                pag.click(1342,10,button="PRIMARY",duration=0.5)

        if(state == "minimized"):
            if(terminal=="cmdt"):
                pag.sleep(0.5)
                pag.click(1240,50,button="PRIMARY",duration=0.5)
                pag.sleep(0.5)
                cond6()
            if(terminal=="vsct"):
                print("Vs Code terminal cannot be used in minimized window.")
  
    if(val == "exit -vscode"):
        if(state == "maximized"):
            if(terminal=="cmdt"):
                pag.sleep(0.5)
                pag.click(1240,50,button="PRIMARY",duration=0.5)
                pag.sleep(0.5)
                cond7()
            if(terminal=="vsct"):
                pag.sleep(0.5)
                pag.click(1342,10,button="PRIMARY",duration=0.5)

        if(state == "minimized"):
            if(terminal=="cmdt"):
                pag.sleep(0.5)
                pag.click(1240,50,button="PRIMARY",duration=0.5)
                pag.sleep(0.5)
                cond8()
            if(terminal=="vsct"):
                print("Vs Code terminal cannot be used in minimized window.")

construct()






