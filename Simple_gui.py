# Creating a Beautifull GUI from turtle Module
import turtle
turtle.bgcolor("white")
t=turtle.Turtle()
colors=['blue','darkblue']
for number in range(500):
    t.forward(number+1)
    t.right(88)
    t.pencolor(colors[number%2])
turtle.done()