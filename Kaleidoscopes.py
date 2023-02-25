kalv = int(input())

def compute(kal):
    if(kal>1):
        res = kal * 5
        res = res - ((res/100)*10)
    else:
        res = kal * 5

    tax = (res/100)*7
    final = res + tax
    final = round(final,2)
    print(final)

compute(kalv)