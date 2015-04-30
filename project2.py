#
#
#2847 is sum of all lower case ASCII

def isPangram(sentence):
    sentence = sentence.lower()
    noPunc = ""
    length = len(sentence)
    pos = 0
    total = 0
    while pos < length:
        if ord(sentence[pos]) >= 97 and ord(sentence[pos]) <=122:
            total = total + ord(sentence[pos])
            pos = pos + 1
        else:
            pos = pos + 1
    if total == 2847:
        return('True')
    else:
        return('False')
    


def isPalindrome(sentence):
    sentence = sentence.lower()
    noPunc = ""
    length = len(sentence)
    pos = 0
    while pos < length:
        if ord(sentence[pos]) >= 97 and ord(sentence[pos]) <=122:
            noPunc = noPunc + sentence[pos]
            pos = pos + 1
        else:
            pos = pos + 1
    length2 = len(noPunc)
    pos2 = 1
    reverse =""
    while length2 > 0:
        j = chr(ord(noPunc[length2-1]))
        reverse = reverse + j
        length2 = length2 - 1
    if noPunc == reverse:
        return('True')
    else:
        return('False')
