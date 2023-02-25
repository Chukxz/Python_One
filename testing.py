data = [{"Word":"average","Offset":51100000,"Duration":4700000},{"Word":"household","Offset":55900000,"Duration":4500000},{"Word":"income","Offset":60500000,"Duration":3700000},{"Word":"is","Offset":64300000,"Duration":1300000},{"Word":"up","Offset":65700000,"Duration":1900000},{"Word":"ten","Offset":67700000,"Duration":2100000},{"Word":"percent","Offset":69900000,"Duration":4200000},{"Word":"from","Offset":74200000,"Duration":1800000},{"Word":"four","Offset":76100000,"Duration":2500000},{"Word":"years","Offset":78700000,"Duration":2300000},{"Word":"ago","Offset":81100000,"Duration":4100000},{"Word":"and","Offset":87700000,"Duration":2300000},{"Word":"our","Offset":90100000,"Duration":900000},{"Word":"customers","Offset":91100000,"Duration":4700000},{"Word":"are","Offset":95900000,"Duration":700000},{"Word":"spending","Offset":96700000,"Duration":4700000},{"Word":"twenty","Offset":101500000,"Duration":3200000},{"Word":"percent","Offset":104800000,"Duration":4000000},{"Word":"more","Offset":108900000,"Duration":2900000},{"Word":"per","Offset":111900000,"Duration":1300000},{"Word":"transaction","Offset":113300000,"Duration":7900000},{"Word":"nearly","Offset":125300000,"Duration":5100000},{"Word":"everyone","Offset":130500000,"Duration":4500000},{"Word":"surveyed","Offset":135100000,"Duration":4500000},{"Word":"is","Offset":139700000,"Duration":1100000},{"Word":"employed","Offset":140900000,"Duration":4700000},{"Word":"in","Offset":145700000,"Duration":900000},{"Word":"a","Offset":146700000,"Duration":700000},{"Word":"professional","Offset":147500000,"Duration":5500000},{"Word":"or","Offset":153100000,"Duration":1500000},{"Word":"managerial","Offset":154700000,"Duration":6300000},{"Word":"occupation","Offset":161100000,"Duration":6900000}]


def show(input):
    newdata = []
    for i in range(0,len(input)):
        word = input[i]["Word"]
        startTime = round(input[i]["Offset"]/10000000,2)
        endTime = round((input[i]["Offset"]/10000000+input[i]["Duration"]/10000000),2)
        newdata.append({"word": word,"startTime": startTime,"endTime":endTime})
    return newdata

print(show(data))

def showwithS(input):
    newdata = []
    for i in range(0,len(input)):
        word = input[i]["Word"]
        startTime = round(input[i]["Offset"]/10000000,2)
        endTime = round((input[i]["Offset"]/10000000+input[i]["Duration"]/10000000),2)
        newdata.append({"word": word,"startTime": str(startTime) + 's',"endTime": str(endTime) + 's'})
    return newdata
print(showwithS(data))

def list(input):
    newdata = []
    for i in range(0,len(input)):
        Word = input[i]["Word"]
        Offset = input[i]["Offset"]
        Duration = input[i]["Duration"]
        newdata.append({"word": Word,"Offset": Offset,"Duration": Duration})
    return newdata

print(list(data))