from turtle import Turtle
from random import randint, choice
import time
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.pu()
        self.random_heading = choice([randint(1, 89), randint(91, 179), randint(181, 269), randint(271, 359)])
        self.setheading(self.random_heading)
        self.random_x = choice([10, -10])
        self.random_y = choice([10, -10])
        

    def move(self):
        self.goto(self.xcor() + self.random_x , self.ycor() + self.random_y)
        time.sleep(0.008)

    def bounce(self, side):
        if side == 'x':
            self.random_y *= -1
        if side == 'y':
            self.random_x *= -1

    # def up(self):
    #     self.setheading(90)
    #     self.fw()
    
    # def down(self):
    #     self.setheading(270)
    #     self.fw()
    
    # def right(self):
    #     self.setheading(0)
    #     self.fw()
    
    # def left(self):
    #     self.setheading(180)
    #     self.fw()

    # def fw(self):
    #     self.forward(10)
    #     time.sleep(0.5)
    #     print(self.xcor(), self.ycor())

    
    