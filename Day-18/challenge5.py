from turtle import Turtle, Screen
from random import randint, choice


jimmy = Turtle()
jimmy.shape("arrow")
jimmy.speed(0)

screen = Screen()
screen.colormode(255)

directions = [0, 90, 180, 270]

gap = 3

for i in range(int(360 / gap)):
    jimmy.color(randint(0, 255), randint(0, 255), randint(0, 255))
    jimmy.setheading(i * gap)
    jimmy.circle(200)

screen.exitonclick() 