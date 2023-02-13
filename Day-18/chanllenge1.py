from turtle import Turtle, Screen
from random import randint


jimmy = Turtle()
jimmy.shape("arrow")
screen = Screen()

for _ in range(4):
    jimmy.forward(50)
    jimmy.right(90)


screen.exitonclick()