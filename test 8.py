file=open("C family, Java, Python and others\Python Program\Text1.txt","r")

print(file.read(5))
print(file.read(16))
print(file.read())
print("Re-reading")
print(file.read())
print("Finished")


file.close()
# print(file.readlines()) to read it line by line

# A for loop can also be used like so
# file=open.("filename.extension","mode")

# for line in file:
#     print(line)
# file.close()

file=open("index.js","r")
for line in file:
    print(line,end='')
file.close()

