# A factorial function

def factorial_func(x):
    assert x>=0,"Please enter 0 or a positive number"
    assert round(x)==x, "Please enter an integer"

    if x==1 or x==0:
        return 1
    else:
        return x*factorial_func(x-1)
        

print(factorial_func(5))

def is_even(x):
    if x==0:
        return True
    else:
        return is_odd(x-1)

def is_odd(x):
    return not is_even(x)

print(is_odd(35))
print(is_even(36))


#The fibonacci sequence
def fib(a):
    if a==0 or a==1:
        return 1
    else:
        return fib(a-1) + fib(a-2)
print(fib(10))

num_set={1,2,3,4,5}
word_set=set(["spam","eggs","sausage"])

print(3 in num_set)
print("spam" not in word_set)
print(len(num_set))
print(len(word_set))

nums={1,2,1,3,1,4,5,6}#number cannot be repeated in sets
print(nums)#so the output is {1,2,3,4,5,6}
print(len(nums))#and the length is 6

nums.add(-7)
print(nums)#{1,2,3,4,5,6,-7}
nums.remove(3)
print(nums)#{1,2,4,5,6,-7}


set1=set(["This is a set"])
print(set1)

set2=set("This is a set")
print(set2)

set3=set([8,9,1,9,"2",8])
print(set3)

set4=set("8 2 8 q0 19 93 29")
print(set4)


set5=set(["8 2 8 q0 19 93 29"])
print(set5)

first={1,2,3,4,5,6}
second={4,5,6,7,8,9}

print(first | second)#The union operator "|" combines two sets to form a new one containing items in either
print(first & second)#The intersection operator "&" gets items only in both
print(first - second)#The difference operator "-" get items in the first(in this case "first") but not in the second(in this case "second")
print(second - first)#The difference operator "-" get items in the first(in this case "second") but not in the second(in this case "first")
print(first ^ second)#The symmetric operator "^" gets itmes in either set but not both
