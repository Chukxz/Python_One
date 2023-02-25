with open("Book Titles.txt","w") as f:
    f.write("Some book\nAnother book")

f=open("Book Titles.txt","r")
t=f.readlines()
for i in range(0,len(t)):
    if len(t) !=i+1:
        print(t[i][0]+str(len(t[i])-1))
    else:
        print(t[i][0]+str(len(t[i])))

f.close();

f=open("Book Titles.txt",'r')
s=f.readlines()
for c in s:
    if s[-1] != c:
        print(c[0]+str(len(c)-1))
    else:
        print(c[0]+str(len(c)))
f.close();

f=open("Book Titles.txt","r")
r=f.read().splitlines(keepends=False)
print(r)
for p in r:
    print(p[0]+str(len(p)))
f.close();

ff=open("Book Titles.txt","r")
ss=ff.readlines()
for i in ss:
    if i!=ss[-1]:
        print(i[0].upper()+str(len(i)-1))
    else:
        print(i[0].upper()+str(len(i)))

f.close()