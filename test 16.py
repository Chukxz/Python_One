from itertools import count,cycle,repeat,accumulate,takewhile,product,permutations,combinations

for i in count(3):
    print(i)
    if i>100:
        break

c=0
for a in cycle("python"):
    c+=1
    if c<=12:
        print(a)
    else:
        break

for e in repeat("repeat it",4):
    print(e)

nums=list(accumulate(range(8)))
print(nums)

print(list(takewhile(lambda x: x<=6,nums)))

letters=("A","B","C","D")
print(list(product(letters,range(4))))
print(list(permutations(letters)))
print(list(combinations(letters,2)))

a={1,2}
print(list(product(range(3),a)))
print(len(list(product(range(3),a))))


num=int(input())

def fibonacci(n):
    if n<=1:
        return 1
    else:
       return fibonacci(n-1) + fibonacci(n-2)

for i in range(num):
    print(fibonacci(i))
