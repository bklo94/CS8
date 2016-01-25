# screensize.py
# Brandon Lo, 4/14/15

def height(D,W,H):
    return ((D**2*H**2)/(W**2+H**2))**0.5

def width(W,H,h):
    return (W/H*h)








# solution must be above this comment

# do not change any part of the code below
def main():
    D, W, H = eval( input("enter D, W, H (separated by commas): ") )
    h = height(D, W, H)
    w = width(W, H, h)
    print("width = {0:.1f}, height = {1:.1f}".format(w, h))

main()
