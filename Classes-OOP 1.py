class Vector2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(itself,otherself):
        return Vector2D(itself.x - otherself.x, itself.y - otherself.y)

    def __mul__(a,b):
        return Vector2D(a.x * b.x, a.y * b.y)

    def __truediv__(c,d):
        return Vector2D(c.x / d.x, c.y / d.y)

    def __floordiv__(e,f):
        return Vector2D(e.x // f.x, e.y // f.y)

    def __mod__(g,h):
        return Vector2D(g.x % h.x, g.y % h.y)

    def __pow__(i,j):
        return Vector2D(i.x ** j.x, i.y ** j.y)
    
    # def __and__(k,l):
    #     return Vector2D(k.x & l.x, k.y & l.y)

    # def __xor__(m,n):
    #     return Vector2D(m.x ^ n.x, m.y ^ n.y)

    # def __or__(o,p):
    #     return Vector2D(o.x | p.x, o.y | p.y)


case1 = Vector2D(32,98)
case2 = Vector2D(89,23) 
result = case1 + case2
res = case1 - case2
r = case1 * case2
re = case1 / case2
resu = case1 // case2
resul = case1 % case2
results = case1 ** case2
# resulti = case1 & case2
# resultin = case1 ^ case2
# resulting = case1 | case2

print(result.x)
print(result.y)
print(res.x)
print(res.y)
print(r.x)
print(r.y)
print(re.x)
print(re.y)
print(resu.x)
print(resu.y)
print(resul.x)
print(resul.y)
print(results.x)
print(results.y)
# print(resulti.x)
# print(resulti.y)
# print(resultin.x)
# print(resultin.y)
# print(resulting.x)
# print(resulting.y)



class SpecialString:
    def __init__(self, cont):
        self.cont = cont
    
    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])

spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam / hello)

# Note: Magic methods also exist for
# < __lt__ and __len__ for len()
# > __gt__ and __getitem__ for indexing
# <= __le__ and __setitem__ for assigning to indexed values
# >= __ge__ and __delitem__ for deleting indexed values
# == __eq__ and __iter__ for iteration over objects (e.g., in for loops)
# != __ne__ and __contains__ for in 
# __call for calling objects as functions and __int__ and __str__ for converting objects to built-in types

class Special:
    def __init__(self,cont):
        self.cont = cont

    def __gt__(self, other):
        for index in range(len(other.cont)+1):
            result = other.cont[:index] + ">" + self.cont
            result += '>' + other.cont[index:]
            print(result)

spam = Special("spam")
eggs = Special("eggs")

spam > eggs