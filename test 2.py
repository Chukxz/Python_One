
#dt=str(input())
#td=len(dt)
#print(dt[td-1])

#ds=input()
#print(ds[-1])

#nums=[1,2,3,4,5]
#print(nums)
#print(len(nums))
#nums.append(6)
#print(nums)
#print(len(nums))

string='some text'
x=len(string)
print(string)
print(x)

words=['Python', "fun"]
words.insert(1,'is')
print(words)
print(words[0]+' '+words[1]+" "+words[2])

#a = int(input())
#b = int(input())
#print(list(range(a,b)))
#or list=list(range(a,b))
#print(list)

x=[42,8,7,1,0,124,8897,555,3,67,99]

indexes=0
for index in x:
    indexes+=index
print(indexes)

#num=int(input())
#if num in x:
#   print("bingo")



#inputValue=str(input())
#print(inputValue[2])

#or inputValue=input()
#print(str(inputValue[2]))

words=['Hello','world',"!"]
print(words[0])

matrix=[
    [1,2,3],
    [4,5,6]
]

print(matrix)

string='Hello World!'
print(string[7]) 

x="Python"
print((x[1]+x[4]+"\n")*2)

nums=[5,8,2]
nums[1]=42
print(nums)

num=[2,9,1,8]
num[3]=num[1]
print(num)

numz=[1,2,3]
print(numz+[4,5,6])

o=[2,4]
o+=[6,8]
print(o[2]//o[0])

words=["spam", "eggs",'spam','sausage']
print('spam' in words)
print('eggs' in words)
print('tomato' in words)


nums=[10,9,8,7,6,5]
nums[0]=nums[1]-5
if 4 in nums:
    print(nums[3])
else:
    print(nums[4])

x="Hello World"
if "World" in x:
    print("yes")
else:
    print("no")

txt=input()
if("spam" in txt):
    print("Yes")
else:
    print("No")

nums=[1,2,3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)

names=['John','James','Henry',"Wilberforce"]
name=input("Please input your first name with the first letter in uppercase and the rest in lowercase. \n")
if name in names:
    print("Name found")
else:
    print("Name not found")

words=['hello','world','eggs','spam']
for word in words:
    print(word + " !")
    
listss=[4,7,3,1.2]
for x in listss:
    print(x*2);

stringz='testing for loops'
count=0
for char in stringz:
    if(char=='t'):
        count+=1
print(count)

text='some text'
for a in text:
    if a == 'e':
        break
    print(a)


lists=[2,3,4,5,6,7]

for x in lists:
    if(x % 2==1 and x>4):
        print(x)
        break

number = list(range(5,10))
print(number)

ksjd=list(range(5))
print(ksjd)
print(ksjd[4])

numbs=list(range(5,20,2))
print(numbs)

numberz=list(range(7,3,-1))
print(numberz)

for i in range(5):
    print('Hello')

for j in range(50):
    if j==0:
        print("1st Hello")
    if j==1:
        print("2nd Hello")
    if j==2:
        print("3rd Hello")
    if j>2:
        print(str(j+1)+"th Hello")

squares=[0,1,4,9,16,25,36,49,64,81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])
print(squares[:7])
print(squares[7:])
print(squares[::-1])
print(squares[:])
print(squares[::2])
print(squares[2:8:3])
print(squares[8:2:-3])
print(squares[:2:-2])

asc=[0,1,2,3,4,5,6,7,8,9]
des=asc[::-1]
print(asc)
print(des)

named=[3,2,7,9,6]
named=named[1:-1]
print(named)

list=[1,1,2,3,5,8,13]
print(list[list[4]])