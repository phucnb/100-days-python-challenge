from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score import Score

WIDTH = 600
HEIGHT = 600
MODE = {'easy' : 1, 'normal' : 0.5, 'hard' : 0.1}



# Set up Screen 
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor('black')
screen.title("The Snake Game")
screen.tracer(0)
screen.listen()
# Initial a snake
snake = Snake()
# Initial a food
food = Food()
# Set up Score
score = Score()

screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
game_over = False
while not game_over:
    snake.move()
    if snake.head.distance(food) < 10:
        food.refresh_position()
        snake.add()
        score.increase_score()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.game_over()
        game_over = True
    for body in range(2, len(snake.snakes)):
        if snake.head.distance(snake.snakes[body]) < 20:
            score.game_over()
            game_over = True

    screen.update()
    time.sleep(MODE['hard'])

    



screen.exitonclick()