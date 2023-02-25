
#inheritance
class Animal:#animal is the superclass here
    def __init__(self,name,color):
        self.name=name
        self.color=color

class Cat(Animal):#subclass
    def purr(self):
        print("Purr...")

class Dog(Animal):#subclass
    def bark(self):
        print("Woof!")

fido = Dog("Fido","brown")
print(fido.color)
print(fido.name)
fido.bark()

memes=Cat("memes","black")
print(memes.name)
print(memes.color)
memes.purr()


class Wolf:#the superclass
    def __init__(self,name,color):#__init__ defines the base function for the class
        self.name=name
        self.color=color
    
    def bark(self):
        print("Grr...")#method for class....A method is a basically function in a class

class Dog2(Wolf):#the subclass
    def bark(self):#bark function of Dog overrides the bark function of Wolf when Dog2 is being called. This is true when a class inherits from another with the same attributes or methods as it overrides them.
        print("Woof!")

husk=Wolf("Husk","white")
husky=Dog2("Max","grey")

husk.bark()
husky.bark()

#indirect inheritance
class A:
    def method(self):
        print("A method")

class B(A):
    def another_method(self):
        print("B method")

class C(B):
    def third_method(self):
        print("C method")

a=A()
a.method()
b=B()
b.method()
b.another_method()
c=C()
c.method()
c.another_method()
c.third_method()


class D:
    def spam(self):
        print(1)

class E(D):
    def spam(self):
        print(2)
        super().spam()

D().spam()
E().spam()