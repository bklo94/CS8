#project2.py
#Brandon Lo and Derek Tan, 4/30/15

def isPangram(sentence):
    sentence = sentence.lower()
    length = len(sentence)
    pos = 0
    total = 0
    order = []
    while pos < length:
        if ord(sentence[pos]) >= 97 and ord(sentence[pos]) <=122:
            order.append(sentence[pos])
            pos = pos + 1
        else:
            pos = pos + 1
    start = 0
    len(order)
    for i in range(0, len(order)):
        j = order[i]
        for k in range(0, len(order)):
            l = order.count(j)
            if l > 1:
                order[i] = '\x00'
    for m in range(0, len(order)):
        order[m] = ord(order[m])
    n = sum(order)
    if n == 2847:
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

def convert(text):
    pos = 0
    text2 = text.upper()
    if text2 != text:
        while pos < len(text):
            first = text.lower()[pos]
            if pos == 0:
                if first == "a" or first == "e" or first == "i" or first == "o" or first == "u":
                    a = text + "way"
                    break
                elif first == "q" and text.lower()[pos+1] == "u":
                    a = text [pos+2:] + text[:pos+2] + "ay"
                    break
                else:
                    pos = pos + 1
            elif pos > 0 and ord(text[0]) >= 65 and ord(text[0]) <= 90:
                if first == "a" or first == "e" or first == "i" or first == "o" or first == "u" or first == "y":
                    a = text[pos].upper() + text[pos+1:] + text[:pos].lower() +"ay"
                    break
                elif first == "q" and text.lower()[pos+1] == "u":
                    a = text[pos+2].upper() + text[pos+3:] + text[:pos+2].lower() + "ay"
                    break
                else:
                    pos = pos + 1
            elif pos > 0 and ord(text[0]) <65 or ord(text[0])>90:
                if first == "a" or first == "e" or first == "i" or first == "o" or first == "u" or first == "y":
                    a = text [pos:] + text[:pos] +"ay"
                    break
                elif first == "q" and text.lower()[pos+1] == "u":
                    a = text [pos+2:] + text[:pos+2] + "ay"
                    break
                else:
                    pos = pos + 1
    if text2 == text:
        while pos < len(text):
            first = text.lower()[pos]
            if pos == 0:
                if first == "a" or first == "e" or first == "i" or first == "o" or first == "u":
                    a = text + "WAY"
                    break
                elif first == "q" and text.lower()[pos+1] == "u":
                    a = text [pos+2:] + text[:pos+2] + "AY"
                    break
                else:
                    pos = pos + 1
            elif pos > 0:
                if first == "a" or first == "e" or first == "i" or first == "o" or first == "u" or first == "y":
                    a = text [pos:] + text[:pos] +"AY"
                    break
                elif first == "q" and text.lower()[pos+1] == "u":
                    a = text [pos+2:] + text[:pos+2] + "AY"
                    break
                else:
                    pos = pos + 1
    return (a)

import re
def pigLatin(text):
    position = 0
    length3 = len(text)
    order = []
    order = re.split('(\W+)', text)
    position3 = 0
    final = ""
    length4 = len(order)        
    while position3 < len(order):
        if order[position3].isalpha():
            final = final + convert(order[position3])
        else:
            final = final + order[position3]
        position3 = position3 + 1
    return(final)


