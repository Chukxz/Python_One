# salaries = [2000, 1800, 3100, 4400, 1500]
# bonus = int(input())


# def add_bonus(x):
#     return x + bonus

# result = list(map(add_bonus,salaries))
# print(result)


#your code goes here
# def decor(func):
#     def asterisk(x):
#         print("***")
#         func(x)
#         print("***")
#         print("END OF PAGE")
#     return asterisk

# @decor
# def invoice(num):
#     print("INVOICE #" +num)

# invoice(input());

def convert(num):
    if num == 0:
        return 0
    elif num < 0:
        return("Please input a number equal to or greater than zero")
    else:
        return (num % 2 + 10 * convert(num // 2))

print(convert(int(input("Enter a positive number:"))))


#Do a personal project work to convert from binary back to decimal and to carry out conversions on other bases. 