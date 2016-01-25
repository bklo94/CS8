#lab09.py
#Brandon Lo and Matt Stafford, 6/2/15
# some image processing functions

import sys
sys.path.append('/cs/class/cs8c/lib')
import cImage
image = cImage.EmptyImage(500,500)
window = cImage.ImageWin("My Image",500,500)

def setPixels(pixel, x, y, w, h):
    for xCoor in range(x, x+w):
        for yCoor in range(y, y+h):
            image.setPixel(xCoor,yCoor,pixel)

def show():
    image.draw(window)


def checkerboard(x,y,w,h):
    black = cImage.Pixel(0,0,0)
    white = cImage.Pixel(255,255,255)
    for q in range(0,h,y):
        if q/y%2==0:
            for p in range(0,w,x):
                if p/x%2 == 0:
                     setPixels(white,q,p,x,y)
                else:
                    setPixels(black,q,p,x,y)
        else:
            for p in range(0,w,x):
                if p/x%2 == 0:
                     setPixels(black,q,p,x,y)
                else:
                    setPixels(white,q,p,x,y)
    show()
    
            


checkerboard(30,30,500,500)

