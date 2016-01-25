#lab05.py
#Brandon Lo and Matt Stafford, 5/4/15
#some list functions and test cases

def printList(aList):
    for n in range (0,len(aList)):
            print( str(n)+" "+ str(aList[n]))

def findMax(aList):
    a = max(aList)
    return (aList.index(a))

def findMin(aList):
    a = min(aList)
    return (aList.index(a))


myList = [-22.5, 1.4, -7.2, 10.9, -30.7, 11.3, 4.0]
printList(myList)
iMax = findMax(myList)
iMin = findMin(myList)
print("maximum is", myList[iMax], "at index", iMax)
print("minimum is", myList[iMin], "at index", iMin)
