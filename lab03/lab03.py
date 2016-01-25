#lab03.py
#Brandon Lo and Ryan Meek 4/21/15
#a factorial function and Fibonacci function

#factorial - returns n factorial
#assumes n is greater than or equal to 0
def factorial(n):
        result = 1
        for i in range(2,n+1):
            result = result * i
        return result

#fib returns nth term of Fibonacci sequence:
# 1,1,2,3,5,8,... So fib(6) = 8

def fib(n):
    fib = 0
    a = 1
    b = 1
    if n < 3:
        return (1)
    else:
        for i in range(3,n+1):
            c = a+b
            a = b
            b = c
        return c
