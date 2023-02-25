print(None)

print(None==None)
if None:
    print(True)
else:
    print(False)


def SomeFunc():
    print("Hi")
var = SomeFunc()
print(var)

foo=print()
if foo==None:
    print(1)
else:
    print(2)


ages={"Dave":24,"Mary":42,"John":58,"someNumbers":[3,9,0]}
print(ages["Dave"])
print(ages["Mary"])
print(ages["someNumbers"])
print(ages["someNumbers"][2])


squares={1:1,2:4,3:"error",4:16}
squares[8]=64
squares[3]=6
print(squares)

primes={1:2,2:3,4:7,7:17}
print(primes[primes[4]])
nums={
    1:"one",
    2:'two',
    3:'three'
}

print(1 in nums)
print(3 in nums)
print(4 not in nums)


pairs={1:"apple",
"orange":[2,3,4],
True:False,
0:"what",
None:"True"}
print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345,"not in the dicionary"))


words=("spam","eggs","sausages")
print(words[0])

myTuple="one","two","three"
print(myTuple[1])

cubes=[i**3 for i in range(5)]
print(cubes)

dicts={1:"One",2:"Two",3:"Three",4:"Four"}

keyList=[i for i in dicts]

valueList=[dicts[i] for i in dicts]

print(keyList)
print(valueList)

evens=[i**2 for i in range(10) if i%2==0]
print(evens)

j=3,5,7
m="Numbers {0} {1} {2} {0}".format(j[0],j[1],j[2])
print(m)

print("{0}{1}{0}, {2}".format("abra","cad","hmmn"))

print("{x} {y} {z}".format(x=2,y=5,z=6))

numz=[55,44,33,22,11]

if all([i>5 for i in numz]):
    print("All larger than 5")

if any([i%2 == 0 for i in numz]):
    print("At least one is even")

for v in enumerate(numz):
    print(v)