#Magic Methods or dunders

#e.g __init__(passing arguments to classes), __add__(for adding + in classes)

class Vector2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return Vector2D(self.x + other.x , self.y + other.y)

first=Vector2D(5,7)
second=Vector2D(3,9)
result=first + second
print(result.x)
print(result.y)


class SpecialString:
    def __init__(self,cont):
        self.cont=cont
    
    def __truediv__(self,other):
        line="="*len(other.cont)
        return "\n".join([self.cont,line,other.cont])

spam=SpecialString("spam")
hello=SpecialString("Hello World!")
print(spam/hello)

class Magic:
    def __init__(self,conts):
        self.conts=conts
        
    def __gt__(self,others):
        for index in range(len(others.conts)+1):
            result=others.conts[:index] + ">"+ self.conts
            result += ">" + others.conts[:index]
            print(result)

spams=Magic("spams")
eggs=Magic("eggs")
spams > eggs


import random

class VagueList:
    def __init__(self,cont):
        self.cont=cont

    def __getitem__(self,index):
        return self.cont[index+random.randint(-1,1)]

    def __len__(self):
        return random.randint(0,len(self.cont)*2)

vague_list = VagueList(["A","B","C","D","E"])

print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])

class Queue:
    def __init__(self,contents):
        self._hiddenlist = list(contents)

    def push(self,value):
        self._hiddenlist.insert(0,value)

    def pop(self):
        return self._hiddenlist.pop(-1)

    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)

queue = Queue([1,2,3])
print(queue)
print(queue._hiddenlist)
queue.push(0)
print(queue._hiddenlist)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)


class Spam:
    __egg=7
    def print_egg(self):
        print(self.__egg)

s = Spam()
s.print_egg()
print(s._Spam__egg)
#print(s.__egg) will throw an AttributeError


