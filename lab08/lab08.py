# lab08.py
# Brandon Lo and Matt Stafford, 5/26/15
# Function to get a list of strings from the user

                
def getStrings():
    print('Enter items; enter "quit" to quit')
    item2 = input(":")
    i = 0
    item = []
    while item2 != "quit":
        item.insert(i,item2)
        i = i + 1
        item2 = input(":")
    return item
        
                
def getNumbers():
    print('Enter numbers; enter "quit" to quit')
    item2 = input(":")
    i = 0
    item = []
    while item2 != "quit":
        item2 = float(item2)
        item.insert(i,item2)
        i = i + 1
        item2 = input(":")
    return item


import sys 
sys.path.append('/cs/class/cs8c/lib')
from cImage import *

def display(imageName):
    width = imageName.getWidth()
    height = imageName.getHeight()
    ImageWin("windowTitle", width, height)
    image.draw(windowTitle)
