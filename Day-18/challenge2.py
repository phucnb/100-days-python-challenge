from turtle import Turtle, Screen
from random import randint


jimmy = Turtle()
jimmy.shape("arrow")
screen = Screen()

for _ in range(20):
    jimmy.pd()
    jimmy.forward(10)
    jimmy.pu()
    jimmy.forward(10)


screen.exitonclick()