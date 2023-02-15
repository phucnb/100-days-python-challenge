from turtle import Turtle, Screen
from pad import Pad
from ball import Ball
import time

WIDTH = 1200
HEIGHT = 800

# Set up screen
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor('black')
screen.tracer()
screen.listen()

# Set up Divider
devider = Turtle('square')
devider.color('white')
devider.shapesize(40, 0.2, 1)
devider.pu()


# Set up Pads
left_pad = Pad(side='left')
screen.onkey(left_pad.up, 'w')
screen.onkey(left_pad.down, 's')
right_pad = Pad(side='right')
screen.onkey(right_pad.up, 'Up')
screen.onkey(right_pad.down, 'Down')

# Set up ball
ball = Ball()
game_over = False
# screen.onkey(ball.up, 'Up')
# screen.onkey(ball.down, 'Down')
# screen.onkey(ball.left, 'Left')
# screen.onkey(ball.right, 'Right')
# screen.onkey(ball.fw, 'm')
while not game_over:
    ball.move()
    if ball.ycor() > 360 or ball.ycor() < -360:
        ball.bounce('x')
    if ball.xcor() > 580 or ball.xcor() < -580:
        game_over = True
    print(ball.distance(left_pad))
    if ball.distance(left_pad) < 25 or ball.distance(right_pad) < 25:
        ball.bounce('y')
screen.update()
screen.bye()
screen.exitonclick()



