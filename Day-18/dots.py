import colorgram
from turtle import Turtle, Screen
from random import randint, choice

number_of_colors = 30
colors_pallet = colorgram.extract('image.jpg', number_of_colors)
colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors_pallet]

width = 1200
height = 700

jimmy = Turtle()
jimmy.shape("arrow")
jimmy.speed(0)
screen = Screen()
screen.setup(.99, .99, 0, 0)
screen.screensize(canvwidth=width, canvheight=height)
screen.colormode(255)

row = 7
column = 12
gap = 100

for y in range(int(row)):
    jimmy.pu()
    jimmy.goto(-width/2, -height / 2 + (y * gap))
    for x in range(column):
        jimmy.color(choice(colors))
        jimmy.dot(40)
        jimmy.forward(gap)
    



screen.exitonclick() 