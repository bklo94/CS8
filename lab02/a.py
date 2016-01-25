#function to draw a house
print("Draws the house"
import turtle
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
    
  

#draw: a rectangle at the position of the turtle
drawHouse(D,E)
