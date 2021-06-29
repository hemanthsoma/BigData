import turtle
a=turtle.Turtle()
def square(angle):
    a.forward(100)
    a.right(angle)
    a.forward(100)
    a.right(angle)
    a.forward(100)
    a.right(angle)
    a.forward(100)
    a.right(angle+10)
for i in range(36):
    square(90)