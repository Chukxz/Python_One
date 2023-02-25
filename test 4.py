
text=input()
word=input()

def search(text,word):
        if word in text:
            return("Word Found")
        else:
            return("Word not found")
        
print(search(text,word))

def pi(x):
    for i in range(x):
        print(i)
        return #only 0 will be printed because all numbers after 0 will be returned as a result of the indentation.
pi(10)


def sumxy(x,y):
    return x+y

res=sumxy(2,3)
print(res)

def foo(x,y):
    if x>=y:
        return x
    else:
        return y

x=foo(4,7)
print(x)

def max(x,y):
    if x>=y:
        return x
    else:
        return y
if(max(6,4)>10):
    print("Yes")
else:
    print("Nope")

def my_func():
    print('spam')
    print("spam")
    print("spam")

my_func()


def exclamation(word):
    print(word+"!")

exclamation('spam')
exclamation('eggs')

def print_sum_twice(x,y):
    print(x + y)
    print(x + y)

print_sum_twice(5,8)

def calc(x,y):
    return[x+y,x*y]
res=calc(3,4)
print(res[1])

def sums(x):
    """
    This creates a range of numbers from 0 to one less than 4, that is from 0 to 3.
    And then creates a variable res which increments by the value of the numbers between 0 and 4
    the number of times that there are numbers between 0 and 3. That is there are 4 numbers: 0,1,2,3.
    And res which is 0+0=0, then =+1=1, then 1+2=3, then 3+3=6. Therefore the final value of res is 6 and this
    value is printed or outputted by the print function 'print()'.
    """
    res=0
    for i in range(x):
        res+=i
    return res
print(sums(4))

def area(length,width):
    return length*width
length=int(input())
width=int(input())
rect=area(length,width)
print(rect)

def printBill(text):
    print("======")
    print(text)
    print("======")

text=str(input())
printBill(text)

def welcome():
    user=input()
    print("Welcome, "+str(user))

welcome()