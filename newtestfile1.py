
def spell(txt):
    if len(txt)==1:
        print(txt)
    else:
        spell(txt[1:])
        print(txt[0])
        rev = txt[::-1]
        for c in rev:
            print(c)
    


txt = input()
spell(txt)

def decor(func):
    def wrap():
        print("==========")
        func()
        print("==========")
    return wrap()

def print_text():
    print("Hello World!")


decor(print_text)

@decor
def print_texts():
    print("Hi World!")



def factorial(x):
    if x == 1 or x == 0:
        return 1
    else:
        return x * factorial(x-1)

num = int(input())

print(factorial(num))


def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x-1)

def is_odd(x):
    return not is_even(x)

print(is_odd(17))
print(is_odd(18))
print(is_even(17))
print(is_even(18))

t = []
u = []
def function(named_arg, *args,**kwargs):
    print(named_arg)
    print(args)
    print(list(args))
    x = list(args)
    for i in range(len(args)):
        t.append(x[i])
        print(t)
    print(kwargs)
    print(list(kwargs))
    y = list(kwargs)
    for k in range(len(kwargs)):
        u.append(y[k])
        print(u)
        print(kwargs.get(chr(97+10-k)))

function(1,2,3,4,5,6,7,k=2,j=9)


def power(x,y):
    if y == 0:
        return 1
    else:
        return x*power(x,y-1)
        
print(power((int(input())),(int(input()))))
