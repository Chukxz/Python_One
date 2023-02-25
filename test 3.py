
txt='hello'
print(max(txt))

msg=input()
print(msg.replace('#'," "))

Str='some text goes here'
x=Str.split(" ")
print(x)
sec=x[1]
print(sec)

h=", ".join(["spam",'eggs','ham'])
print(h)

nums=[4,5,6]
msg='Numbers: {0} {1} {2}'.format(nums[0],nums[1],nums[2])
print(msg)

print("{0}{1}{0}".format("abra",'cad'))

print("{x},{y}".format(x=5,y=12))


letters=['p','q','r','s','p','u']
print(letters.index('p'))
print(letters.index('q'))

#in rows
i=-1
for a in letters:
    i+=1
    if a=='p':
       print(i)

#as a list
t=-1
find=[]
for b in letters:
    t+=1
    if b=='p':
        find.append(t)
print(find)

let = ['a','b','c','d','e','f','g']

for s in let:
    print(let.index(s),s)
    
x=[2,4,5,7,4]
y=x.index(4)
print(y)

x=[1,8,42,3]
print(min(x),max(x))

x=[2,4,6,2,7,2,9]
print(x.count(2))

x.remove(4)
print(x)

x.reverse()
print(x)
x.clear()
print(x)

y='Hello ME'
print(y.replace("ME", 'world'))

z='extremities'
print(z.replace('e','i',2))

print("this is a sentence".upper())
print('AN ALL CAPS SENTENCE'.lower())


queue=['John',"Amy",'Bob',"Adam"]
queue.append(str(input()))
print(queue)


N=int(input())
sums=0
for i in range(1,N+1):
    sums+=i
print(sums)

N=int(input())
C=(N+1)
X=range(1,C)
U=sum(X)
print(U)

print(sum(range(int(input())+1)))
