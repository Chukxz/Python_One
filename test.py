weight=int(input())
height=float(input())
BMI=weight/(height**2)
if BMI<18.5:
    print("Underweight")
elif BMI>=18.5 and BMI<25:
    print("Normal")
elif BMI>=25 and BMI<30:
    print("Overweight")
elif BMI>30:
    print("Obesity")

total = 0
x=0
while x<5:
    age =int(input())
    if age >3:
        total+=100
    x+=1
print(total)



x=0
while x<10:
    print(x)
    x+=2;

age=int(input())
if age >= 18:
    print("Allowed")
else :
    print("Sorry")

if age >=0 and age<=11:
    print('Child')
elif age>=12 and age<=17:
    print('Teen')
elif age>=18 and age<=64:
    print('Adult')

    

bill=int(input())
tip=(bill*20)/100
print(tip)

temp = int(input())
if temp >= 100:
    print("Boiling")

print("60")


print(65000*1.15)

x="2"
y="4"
z=int(x)+int(y)
print(z)

a=5
b=9
e=str(a)
f=str(b)
print(e+f)

height=float(input("Please input a valid number here: "))
print(height)

x=9.34
y=int(x)
print(y)

age=42
print("His age is "+ str(age))


name=input()
age = input()

print(name + " is " + age)


u=int(input())
v=int(input())
print(u+v)

x=str(input())
y=int(input())
print(x*y)
