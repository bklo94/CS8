#countchars.py
#Brandon Lo and Derek Tan, 6/1/15

# strings that must be used for output:
prompt = "Enter filename: "
titles = "char       count\n----       -----"
itemfmt = "{0:5s}{1:10d}"
totalfmt = "total{0:10d}"
whiteSpace = {' ':'space', '\t':'tab', '\n':'nline', '\r':'crtn'}

#Personal Input Code

import re
import urllib
import urllib.request

prompt = input("Enter filename: ")

def getFileMatches(filename):
    if 'http' in filename:
        myFile = urllib.request.urlopen(filename)
        answer = myFile.readlines()
        for i in range(len(answer)):
            answer[i] = answer[i].decode("utf-8")
        alist = ""
        for i in range(len(answer)):
            alist = alist + answer[i]
        alist = alist.lower()
        order = []
        order = re.split('(\W+)',alist)
        mountaindew = re.split('(\s)',alist)
        return mountaindew
    else:
        myFile = open(filename,"r")
        answer = myFile.readlines()
        alist =""
        for i in range(len(answer)):
            alist = alist + answer[i]
        alist = alist.lower()
        order = []
        order = re.split('(\W+)',alist)
        mountaindew = re.split('(\s)',alist)
        return mountaindew
    
def slashes(gatorade):
    storage = []
    i = 0
    while i < len(gatorade):
        if '\n' in gatorade[i]:
            storage.append(gatorade[i])
            gatorade[i] = ''
        i = i +1
    return storage

def slashes2(gatorade):
    storage = []
    i = 0
    while i < len(gatorade):
        if '\t' in gatorade[i]:
            storage.append(gatorade[i])
            gatorade[i] = ''
        i = i +1
    return len(storage)

def slashes3(gatorade):
    storage = []
    i = 0
    while i < len(gatorade):
        if '\r' in gatorade[i]:
            storage.append(gatorade[i])
            gatorade[i] = ''
        i = i +1
    return len(storage)

#Frequency Table function
def frequencyTable(alist):
    countdict={}
    for item in alist:
        if len(item)>0:
            for i in item:
                if i in countdict:
                    countdict[i] = countdict[i]+1
                else:
                    countdict[i] = 1
        else:
            continue
    itemlist = list(countdict.keys())
    itemlist.sort()
    if '\r' in itemlist:
        countdict['crtn'] = slashes3(alist)
        itemlist.remove('\r')
    if ' ' in itemlist:
        countdict['space'] = countdict.pop(' ')
        itemlist.remove(' ')
    if '\n' in itemlist:
        countdict['nline'] = len(slashes(alist))
        itemlist.remove('\n')
    if '\t' in itemlist:
        countdict['tab'] = slashes2(alist)
        itemlist.remove('\t')
    whiteSpace = {' ':'space', '\t':'tab', '\n':'nline', '\r':'crtn'}
    if 'space' in countdict.keys():
        itemlist.insert(0, whiteSpace[' '])
    if 'tab' in countdict.keys():
        itemlist.insert(0, whiteSpace['\t'])
    if 'crtn' in countdict.keys():
        itemlist.insert(0, whiteSpace['\r'])
    if 'nline' in countdict.keys():
        itemlist.insert(0, whiteSpace['\n'])
    prompt2 = "Enter filename: "
    print( prompt2 + prompt)
    titles = "char       count\n----       -----"
    print(titles)
    for item in itemlist:
        #print(item,"\t",countdict[item])
        print(itemfmt.format(item, countdict[item]))
    countdict['crtn'] = 0
    countdict['nline'] = 0
    countdict['tab'] = 0
    totalfmt = "total{0:10d}"
    print(totalfmt.format(sum(countdict.values())))
    
#RUN THIS FFUCKING THIS WAY
frequencyTable(getFileMatches(prompt))
