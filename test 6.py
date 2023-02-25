def oska():
    """
    words=["spam","egg","spam","sausage"]
print("spam" in words)
print('egg'in words)
print("tomato" in words)

nums=[1,2,3]
print(not 4 in nums)
print(4 not in  nums)

nums.append(4)
print(nums)
print(len(nums))

words=['Python','fun']
insert=1
words.insert(1,'is')
print(words)

letters=['p','q','r','s','p','u']
print(letters.index('p'))
print(letters.index('q'))
print(letters.index('u'))
print(letters.index('r'))
    
    i=1
    while i<=5:
        print(i)
        i+=1
    print("Done")

    print("0 is a number")
    n=1
    while n<=100:
        if n%2==0:
            print(str(n)+" is an even number")    
        elif (n%2!=0) and (n!=1 and n!=3 and n!=5 and n!=7) and (
            ((n%1==0 and n%2==0) or (n%1==0 and n%3==0) or(n%1==0 and n%5==0) or (n%1==0 and n%7==0)) or 
            ((n%2==0 and n%3==0) or (n%2==0 and n%5==0) or(n%2==0 and n%7==0)) or 
            ((n%3==0 and n%5==0) or (n%3==0 and n%7==0)) or 
            (n%5==0 and n%7==0) 
        ):
            print(str(n)+" is odd and is not a prime number") 
        else:
            print(str(n)+" is odd and is a prime number")
        n+=1  
        """
    print(list(range(10)))

oska()

#Fizzball

#Get the input

n = int(input())


#Use this:

for x in range(1, n,2):
    if x % 3 == 0 and x % 5 == 0:
        print("SoloLearn")
    elif x%3==0:
        print("Solo")
    elif x % 5 == 0:
        print("Learn")
    else:
        print(x)


#OR this:

for x in range(1, n):
    if x % 3 == 0 and x % 5 == 0:
        print("SoloLearn")
    elif x%2==0:
        print("This is an even number but we are skipping all even numbers")
        continue
    elif x%3==0:
        print("Solo:this number is divisible by 3")
    elif x % 5 == 0:
        print("Learn: this number is divisible by 5")
    else:
        print(x)

def multiply(x,y):
    return x*y
a=4
b=7
operation=multiply
print(operation(a,b))

def shout(word):
    return word+"!"
speak=shout
output=speak("shout")
print(output)

def add(c,d):
    return c + d

def do_twice(func,c,d):
    return func(func(c,d),func(c,d))

e=6
f=8

print(do_twice(add,e,f))


#madness
def square(x):
    return x*x

def test(func,x):
    print(func(x))

test(square,42)

