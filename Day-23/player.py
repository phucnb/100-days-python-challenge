from turtle import Turtle
import time
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.pu()
        self.hideturtle()
        self.goto(STARTING_POSITION)
        self.showturtle()

    def move(self):
        self.forward(MOVE_DISTANCE)
    
    def reset_position(self):
        self.hideturtle()
        self.goto(STARTING_POSITION)
        self.showturtle()
