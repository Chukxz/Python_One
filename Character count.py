# word = input()
# letters=['a','e','i','o','u']
# list = [ x for x in word if x not in letters]
# print(list)

# print([i for i in str(input()) if i not in ["a","e","i","o","u"]])

#text = input()

# dict = {}


# for y in text:
#     dict[y] = text.count(y)
    

#print(dict)


def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(numbers(11)))
print(len(list(numbers(11))))

def stutters():
    word = ""
    for ch in "spam":
        word += ch
        yield word

print(list(stutters()))

num = int(input())

lists = []

dict = {}

def fib(n):

    if n<=1:
        return n 
    else:
        return (fib(n-1)+fib(n-2))
    
for i in range(num):
    print(fib(i))
    dict["Pos: " + str(i)] = fib(i)
    lists.append(fib(i))

print(dict)
print(lists)


def fibs(x):
    if x ==0 or x==1:
        return x
    elif x>1:
        return fibs(x-1) + fibs(x-2)
    else: return "Negative numbers are not allowed"

x = int(input())

print(fibs(x))

def isPrime(a):
    if a<2:
        return False
    elif a==2:
        return True
    for b in range(2,a):
        if a%b == 0:
            return False
    return True

def primeGenerator(c,d):
    for x in range(c,d):
        if isPrime(x):
            yield x

f = int(input())
t = int(input())

print(list(primeGenerator(f,t)))

