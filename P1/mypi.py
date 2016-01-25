# mypi.py
# Brandon Lo, 4/14/15

def mypi(num):
    answer = 0
    i=1
    while (i < num+1):
        v = (3**(i-1))
        n = negative(i)
        answer = answer + 1/(v*n)
        i = i + 1
    return (12**0.5)*(answer)
    
def negative(number):
    if number%2 == 0 :
        a = (-1*number*2)+1
        return a
    elif number == 1:
        a = 1
        return a
    else:
        a = (number*2-1)
        return a


# solution must be above this comment

# do not change any part of the code below
def main():
    num = int( input("enter number of terms: ") )
    print("estimate of pi is {0:.10f}".format(mypi(num)))

main()
