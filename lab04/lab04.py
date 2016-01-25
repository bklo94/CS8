# lab04.py
# Brandon Lo and Ryan Meek, 4/28/15
# a cipher function and test cases

def rot13(message):
    result = ""   # starts empty; add one character at a time below
    for a in message:
        b = ord(a)+13
        if b > 122:
            c = b - 122 + 97
            result = result + chr(c)
        else:
            result = result + chr(b)
    return result

print(rot13('hello'))

    # loop through each character
       # shift it by 13 places (may wrap around to front of alphabet)
       # add it to the result string

       
def rot(n,string):
    result = ""
    for a in string:
        b = ord(a) + n
        if b > 122:
            c = b - 122 + 97
            result = result + chr(c)
        else:
            result = result + chr(b)
    return result

print(rot(13,'hello'))



       
