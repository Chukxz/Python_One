import re

password = str(input())

def num():
    pattern = r"[0-9]"
    match = re.findall(pattern,password)
    
    if match:
        if len(match) >= 2:
            pass
        else:raise ValueError
    else:raise ValueError

def char():
    pattern = r"[!@#$%&*]"
    match = re.findall(pattern, password)
    if match:
        if len(match) >= 2:
            pass
        else:raise ValueError
    else: raise ValueError


def length():
    if len(password) >= 7:
        for i in password:
            if i != chr(32):
                pass
            else:raise ValueError
    else:raise ValueError


def validates():
    try:
        length()
        num()
        char()
    except ValueError:
        return print("Weak")
    else:return print("Strong")

validates()



