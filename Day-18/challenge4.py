from turtle import Turtle, Screen
from random import randint, choice


jimmy = Turtle()
jimmy.shape("arrow")
jimmy.width(10)
jimmy.speed(0)

screen = Screen()
screen.colormode(255)

directions = [0, 90, 180, 270]


for _ in range(100):
    jimmy.color(randint(0, 255), randint(0, 255), randint(0, 255))
    jimmy.right(choice(directions))
    jimmy.forward(30)

screen.exitonclick()