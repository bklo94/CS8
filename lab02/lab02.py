#lab02.py
#Name: Brandon Lo and Ryan Meek, 4/14/15
#some functions to draw pictures using Turtle Graphics

#function to draw a rectangle
import turtle
D = input("Turtle Name:")
E = int(input("Rectangle Width:"))
F = int(input("Rectangle Height:"))
def drawRectangle(A,B,C):
    A = turtle.Turtle("turtle")
    A.forward(B)
    A.left(90)
    A.forward(C)
    A.left(90)
    A.forward(B)
    A.left(90)
    A.forward(C)
    A.left(90)

#draw: a rectangle at the position of the turtle
drawRectangle(D,E,F)


#function to draw a house
print("Draws the house")
D = input("Turtle Name:")
E = int(input("House Size:"))
def drawHouse(A,B):
    A = turtle.Turtle("turtle")
    A.forward(B)
    A.left(90)
    A.forward(B)
    A.left(90)
    A.forward(B)
    A.left(90)
    A.forward(B)
    A.left(90)
    A.left(90)
    A.forward(B)
    A.right(30)
    A.forward(B)
    A.right(120)
    A.forward(B)
  

#draw: a rectangle at the position of the turtle
drawHouse(D,E)
