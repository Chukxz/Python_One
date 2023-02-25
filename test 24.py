# import this

# print(this)

def function(named_arg, *args,material="plastic",**kwargs):
    print(named_arg)
    print(args)
    print(material)
    print(kwargs)
    print(args[2])
    print(kwargs.get("a","not defined"))

function(1,2,3,4,2,material="metal",a=4,b=7)


# nums = (1,2,3)
# a,b,c = nums
# print(a)
# print(b)
# print(c)
# print(a,b)
# print(b,c)
# print(a,c)
# print(a,b,c)


# a,b,c=c,b,a
# print(a)
# print(b)
# print(c)
# print(a,b)
# print(b,c)
# print(a,c)
# print(a,b,c)

# x,y=[1,2]
# y,x=x,y
# print(x,y)
# print(y,x)

# a,b,*c,d,e=[1,2,3,4,5,6,7,8,9]
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

# a,b,c,d,e=e,d,c,b,a
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

a = 7
b = 1 if a>=5 else 42
print(b)

status = False
msg = "Logout" if status == 1 else "Login"
print(msg)

status = True
msg = "Login" if status == 0 else "Logout"
print(msg)


for i in range(10):
    if i == 999:
        break

else:
    print("Unbroken 1")

for i in range(10):
    if i == 5:
        break

else:
    print("Unbroken 2")

for i in range(10):
    if i>5:
        print(i)
        break

else:
    print("7")




try:
    print(1)
except ZeroDivisionError:
    print(2)
else:
    print(3)


try:
    print(1/0)
except ZeroDivisionError:
    print(4)
else:
    print(5)


print(13%26+5)


import sololearn

sololearn.function()
 

for i in range(10):
    try:
        if 10/i == 2.0:
            break
    except ZeroDivisionError:
        print(1)
    else:
        print(2)