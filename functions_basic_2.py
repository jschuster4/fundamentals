def countdown(Anumber):
    newList = []
    for i in range(Anumber,-1,-1):
        newList.append(i)
    return newList

print(countdown(5))

def printAndReturn(a_list):
    print(a_list[0])
    return(a_list[1])

printAndReturn([4,10])

def firstPlusLength(a_list):
    return len(a_list) + a_list[0]

print(firstPlusLength([1,2,3,4,5]))

def valuesGreater(aList):
    anotherList = []
    if len(aList) < 2: 
        return False
    for i in aList:
        print(i)
        if (i > aList[1]):
            anotherList.append(i)
    print(len(anotherList))
    return(anotherList)

valuesGreater([5,2,3,2,1,4])

def thisLength(size, value):
    newlist = [value] * size
    return newlist

print(thisLength(4,7))


