from cgi import print_arguments
from lib2to3.pytree import type_repr
import random 
from math import pi
from math import ceil,floor,exp,radians
import math
# import math* imports all elements from module math but it is generally discouraged as it confuses variables in code with variables in the external module
from math import cos as cosine
from traceback import print_tb




for i in range(5):
    value = random.randint(1,6)
    print(value)


num=10
print(math.sqrt(num))

print(math.pi)
print(pi)

print(exp(1))
print(floor(2.83))
print(ceil(3.37))
print(radians(360))

print(cosine(2*pi))

try:
    num1=7
    num2=0
    print(num1/num2);
except ZeroDivisionError:
    print("An error occured due to zero division")
 

try: 
    variable=10
    print(variable + "hello")
    print(variable/2)
except ZeroDivisionError:
    print("Divided by zero")
except (ValueError,TypeError):
    print("Error occured")
print("Done")

try:
    print("Hello")
    print(1/0)
except ZeroDivisionError:
    print("Division by zero")
finally:
    print("This code will run no matter what")

def fk():
    '''
    
num=input(":")
if float(num)<0:
    raise ValueError("Negative")

print(1)
assert 2+2==4
print(2)
assert 1+1==3
print(3)

try:
    num=5/0
except:
    print("An error occured")
    raise

temp=-10
assert(temp>=0),"Colder tha absolute zero!"

'''

fk()

