from turtle import Turtle
import time
class Pad(Turtle):

    def __init__(self, side):
        super().__init__()
        self.hideturtle()
        self.shape('square')
        self.color('white')
        self.setheading(90)
        self.shapesize(0.5, 4, 1)
        self.pu()
        if side == 'left':
            self.goto(-580, 0)
        elif side == 'right':
            self.goto(580, 0)
        self.showturtle()
        print(self.xcor(), self.ycor())

    def up(self):
        if self.ycor() < 380:
            self.forward(40)
            time.sleep(0.001)
    
    def down(self):
        if self.ycor() > -380:
            self.backward(40)
            time.sleep(0.001)