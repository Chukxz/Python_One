
txt=input()
a=txt.split(" ")
b=[len(word) for word in a]
c=b.index(max(b))
print(a[c])

filename=input("Enter a filename: ")#Afile.txt ------recommended
# file=open(filename,'w')
# file.write("lsjdj833*w8fk sf\nsfj83298ksfk sfsjfsdkjfsd\nsfdwfjfsdjsjfsf928494josidofjiwksd\nlsjf sf sdfjnsdv nsfjsdfu28f*J8*2LK8J*23KLKWF S F SDIJFS F akljskfajskjf2482jds'fdsljasdfjdkfasj:jf;ksjf;sjfs\najf8wefjajf28*/#9 SDJSJF2JF83 WJSDJJSKDFS skjd@8s *ksjdkal(lsjsfl)lsjkfsfsl!jldflk2iejjdfjsfdj8a4j.fkgjkdds skdjfal.slfk:aljsl's;fk;s; lsfdj9ffjwlfSD: 'LJlfsdkfl@3oiskdl@lkK#kdsjkfjs89kK#ksdkj!ksjfjjf-ijfkw*fslfkLJ:Ljf)LKfkjjj\nJKdlkj7lJJLJ&KJkJjKlfjsljkjd^lJDjds8o4jw\n28ljksjfkjks0ksdfflkds8sflksjfkjd8fdsjkjk23kjskjkj2kkjkaj1kjsjfksjlf1sjlsjk3kdjkj5kjkk4kjksdlkldk6sdjfksjfksa6sfksjfksd8sfskf76sfjdsf\nlsajlkasdf0aldkf2903idsflsldd")
# file.close()
with open(filename) as f:
    text=f.read()
print(text)

def countChar(text,char):
    '''
    This is a the function that counts a particular character
    '''
    count=0
    for c in text:
        if c==char:
            count+=1
    return count

print(countChar(text,"j"))

def countChar(text,char):
    return text.count(char)
print(countChar(text,"f"))

sk=0
for char in "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*();:\'\"\\n/\\ABCDEFGHIJKLMNOPQRSTUVWXYZ.,":
    perc=100*countChar(text,char)/len(text)
    print("{0} - {1}%".format(char,round(perc,2)))
    sk+=perc
print(sk)
   


print(text.count("k"))

quest=str(input("Enter: ")) 
print(text.count(quest))

