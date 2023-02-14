from turtle import Turtle, Screen
import time
from snake import Snake

WIDTH = 600
HEIGHT = 600
MODE = {'easy' : 1, 'normal' : 0.5, 'hard' : 0.1}


# Initial a snake
snake = Snake()
# Set up Screen 
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor('black')
screen.title("The Snake Game")
screen.tracer(0)
screen.listen()
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')

while True:
    snake.move()

    screen.update()
    time.sleep(MODE['hard'])

    



screen.exitonclick()