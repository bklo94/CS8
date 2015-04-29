# sphere.py
# Brandon Lo, 4/77/1
import math
pi = math.pi

#Circumference
def circumference(radius): 
    return 2*pi*radius

#Circle Area
def area(radius):
    return pi*radius**2

#Surface Area
def surface(radius):
    return 4*pi*(radius**2)

#Volume
def volume(radius):
    return (4*pi*radius**3)/3

# solution must be above this comment

# do not change any part of the code below
def main():
    radius = float( input("enter radius: ") )
    print("circumference: {0:.1f}".format(circumference(radius)))
    print("circle area: {0:.1f}".format(area(radius)))
    print("sphere volume: {0:.1f}".format(volume(radius)))
    print("sphere surface area: {0:.1f}".format(surface(radius)))

main()
