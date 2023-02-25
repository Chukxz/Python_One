
def apply_thrice(func,arg):
    return func(func(func(arg)))

def add_five(x):
    return x+5

print(apply_thrice(add_five,10))

def cubeFunc(func,arg):
    return func(func(arg))

def mult(x):
    return x*x

print(cubeFunc(mult,10))

def pure_function(x,y):
    temp=x+2*y
    return temp/(2*x+y)

some_list=[]

def impure(arg):
    some_list.append(arg)

def myFunc(f,arg):
    return(f(arg))

print(myFunc(lambda x:2*x*x,5))

def poly(x):
    return x**2+5*x+4
print(poly(-4))

print((lambda x:x**2+5*x+4)(-4))

#double=lambda x:x*2 there is rarely a reason to do this.
#print(double(7))

triple=lambda x:x*3
add=lambda x,y:x+y
print(add(triple(3),4))
print(triple(add(3,3)))

print((lambda x,y:x+y)((lambda x:x*3) (3),4))


nums=[55,44,33,22,11]

def add_five(x):
    return x+5

result=list(map(add_five,nums))
print(result)

result=list(map(lambda x:x+5,nums))
print(result)

result=[x+5 for x in nums]
print(result)

res=list(filter(lambda x:x%2==0,nums))
print(res)

def even(x):
    return x%2==0
res=list(filter(even,nums))
print(res)    

i=5
def countdown(i):
    while i>0:
        yield i
        i-=1
    
for i in countdown(i):
    print(i)

k=15
def demo(k):
    while k>0:
        yield k
        k-=1

for k in demo(k):
    print(k)

for k in demo(k):
    print(list(demo(17)))

for k in demo(2):
    print(list(demo(12)))

for k in demo(6):
    print(list(demo(k)))

for k in demo(k):
    print(list(demo(k)))

#a=0
#def unending(a):
#    while True:
#        yield a
#        a=a+1

#for  a in unending(a):
#    print(a)

def numbers(x):
    for i in range(x):
        if i%2==0:
            yield i

print(list(numbers(111)))

def stammer():
    stammers=""
    for ch in "spam":
        stammers+=ch
        yield stammers

print(list(stammer()))

def decors(func):
    def wrap():
        print("======")
        func()
        print("======")
    return wrap

def text():
    print("Hello world!")

text=decors(text)
text()

@decors
def texts():
    print("Hello")



    
decorates=decors(text)
decorates()




