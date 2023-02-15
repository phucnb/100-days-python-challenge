from turtle import Turtle
from random import choice

POSITION = [num for num in range(-280, 280) if num % 20 == 0]

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.pu()
        self.color('red')
        self.width(10)
        self.refresh_position()

    def refresh_position(self):
        self.goto(choice(POSITION), choice(POSITION))
