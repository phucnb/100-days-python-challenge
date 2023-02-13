from turtle import Turtle, Screen
from random import randint


jimmy = Turtle()
jimmy.shape("arrow")
screen = Screen()
screen.colormode(255)
 
edges = 3

for _ in range(7):
    jimmy.color(randint(0, 255), randint(0, 255), randint(0, 255))
    for _ in range(edges):
        jimmy.forward(100)
        jimmy.right(360 / edges)
    edges += 1

screen.exitonclick()