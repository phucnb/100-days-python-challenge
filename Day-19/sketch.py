from turtle import Turtle, Screen

turtle = Turtle()

screen = Screen()


def move_forward():
    turtle.forward(10)

def move_backward():
    turtle.backward(10)

def head_clockwise():
    turtle.right(10)
 
def head_counter_clockwise():
    turtle.left(10)

def clear():
    turtle.pu()
    turtle.clear()
    turtle.home()
    turtle.pd()

screen.listen()
screen.onkey(move_forward, 'w')
screen.onkey(move_backward, 's')
screen.onkey(head_clockwise, 'a')
screen.onkey(head_counter_clockwise, 'd')
screen.onkey(clear, 'c')







screen.exitonclick()