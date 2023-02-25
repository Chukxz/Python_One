#celsius = int(input())

#def conv(c):
#    c=((9/5*c)+32)
#    return c

#fahrenheit=conv(celsius)
#print(fahrenheit)

file=open("newfile.txt","w")
file.write("This has been written to a file")
file.close()

file=open("newfile.txt",'a')
file.write(" and this has been appended to it.")
file.close()

try:
    file=open("newfile.txt","r")
    print(file.read())
finally:#Making sure that our file is always closed even if exceptions occur
    file.close()

#We can also use the with statement as it will close the file even if exceptions occur
with open("index.html") as f:
    print(f.read())

text="This is a basic calculator! Use it for basic operations"
file=open("Calc.txt",'w')
print(file.write(text))
file.close()
file=open("Calc.txt",'r')
print(file.read())
file.close()

text="This is a basic calculator! Use it for basic operations" + chr(293)
print(text)


