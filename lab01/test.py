A=input("Age of youself:")
B=input("Age of parent 1:")
C=input("Age of parent 2:")
if int(A+B+C) > 0:
    q = int(A)+int(B)+int(C)
    w = q/3
    print(("Average Age=",w)
else:
    print("0")
    
