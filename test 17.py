#some common paradigms in programming
#1-imperative(using statements, loops and functions as subroutines)
#2-functional(using pure functions, higher-order functions, and recursion)
#3-object-oriented programming(OOP)(using classes to describe an object)

#classes

class Cat:
    def __init__(self,color,legs):
        self.color=color
        self.legs=legs
        
felix=Cat("ginger",4)
ginger=Cat("dog-colored",4)
stumpy=Cat("brown",3)

print(felix.color)
print(ginger.legs)
print(stumpy.legs)


class Dog:
    legs=4#class attribute
    def __init__(self,name,color):
        self.names=name
        self.colors=color

    def bark(self):
        print("Woof!")

fido=Dog("Fido","brown")
print(fido.bark())
print(fido.names)
print(fido.legs)#class attributes "legs" can be called from instances of the class, in this case "fido"
print(Dog.legs)#class attributes can also be called from the class itself 

class Student:
    def __init__(self,name):
        self.name=name    
    def sayHi(self):
        print("Hi "+self.name)

    @classmethod
    def sayHI(cls):
        print("Hi there")

Student.sayHI()
Student("Amy").sayHi()
#or 
s1=Student("Bob")
s1.sayHi()

class Students:
    def __init__(self):
        self=self   
    def sayHi(self):
        print("Hi ")

Students().sayHi()
#or 
s1s=Students()
s1s.sayHi()