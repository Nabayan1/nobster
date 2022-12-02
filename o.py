from turtle import Screen, Turtle
from p import Snake
screen = Screen()
screen.bgcolor("cyan")
nobi = Snake()
nobi.penup()
nobi.generate()
nobi.show()



screen.exitonclick()